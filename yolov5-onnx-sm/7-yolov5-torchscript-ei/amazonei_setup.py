
#*****************************************************************************
# Copyright 2019 Amazon.com, Inc. and its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# or in the "license" file accompanying this file. This file is distributed 
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
# express or implied. See the License for the specific language governing 
# permissions and limitations under the License.
#******************************************************************************

import os
import argparse

import logging
import json


try:
    import boto3
    from botocore.exceptions import ClientError

except ImportError:
    logging.error("This utility requires 'boto3'. Please install it and run the utility again. Command to install boto3 - 'sudo pip install --upgrade boto3'")
    quit()


try:
    import requests

except ImportError:
    logging.error("This utility requires 'requests' module. Please install it and run the utility again. Command to install requests - 'sudo pip install requests'")
    quit()


from distutils.version import StrictVersion

if hasattr(__builtins__, 'raw_input'):
    input = raw_input



def logErrorAndQuit(msg):
    logging.error(msg)
    quit()



class AWSSession:
    """
    A helper class to manage sessions with boto3, the python API for AWS
    """
    def __init__(self, region):
        try:
            self._session = boto3.session.Session(region_name=region)
            assert self._session is not None
            self.region_ = region

        except Exception as awsException:
            print("Error : Exception in AWSSession {}".format(str(awsException)))
            self._session = None

    def getClient(self,clientName):
        return self._session.client(clientName,region_name = self.region_)

    def get_default_region(self):
        return self._session.region_name


class IAM:
    """
    Helper class to manage Instance Profile
    The script will create a role with the name "Amazon-Elastic-Inference-Instance-Profile" and reuse it in subsequent runs
    It will also create the connect role and attach a policy to it
    """

    def __init__(self, awsSession ):
        try:
            self._aws_Session = awsSession
            self._iam_Client = self._aws_Session.getClient('iam')
            self._wizard_role_name = "Amazon-Elastic-Inference-Connect-Role"
            self._wizard_policy_name = "Amazon-Elastic-Inference-Connect-Policy"
            self._wizard_instance_profile_name = "Amazon-Elastic-Inference-Instance-Profile"
            self._role_doc = {
            "Version": "2012-10-17",
            "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": [
                    "sts:AssumeRole"
                ]
            }
            ]
            }

            self._policy_doc = {
            "Version": "2012-10-17",
            "Statement": [
            {
            "Effect": "Allow",
            "Action": [
                "elastic-inference:Connect",
                "iam:List*",
                "iam:Get*",
                "ec2:Describe*",
                "ec2:Get*"
            ],
            "Resource": "*"
            }
            ]
            }

        except Exception as ex:
            self._aws_Session = None
            self._iam_Client = None

    def get_instance_profile_name(self):
        return self._wizard_instance_profile_name

    def create_instance_profile(self):
        profile = self.find_instance_profile()
        if len(profile['InstanceProfiles']) != 0:
            return profile
        profile = self._iam_Client.create_instance_profile(InstanceProfileName=self._wizard_instance_profile_name)
        self._iam_Client.add_role_to_instance_profile(InstanceProfileName=self._wizard_instance_profile_name,RoleName= self._wizard_role_name)
        return profile


    def find_instance_profile(self):
        return self._iam_Client.list_instance_profiles_for_role(RoleName = self._wizard_role_name)


    def create_wizard_role(self):
        self.create_eia_connect_role()
        policy_reponse = self.create_eia_connect_policy()
        policy_arn = policy_reponse['Policy']['Arn']
        self._iam_Client.attach_role_policy(PolicyArn=policy_arn,RoleName=self._wizard_role_name)
        return self._wizard_role_name


    def create_eia_connect_role(self):
        policy_json = json.dumps(self._role_doc)
        return  self._iam_Client.create_role(AssumeRolePolicyDocument=policy_json,Path='/',RoleName=self._wizard_role_name)

    def create_eia_connect_policy(self):
        policy_json = json.dumps(self._policy_doc)
        return  self._iam_Client.create_policy(PolicyName=self._wizard_policy_name,Path='/',PolicyDocument = policy_json,Description="Policy for connecting to Amazon EI service")


    def find_wizard_role(self):
        roles_reponse = self._iam_Client.list_roles()
        index = 0
        if (roles_reponse):
            for role in roles_reponse['Roles']:
                if(role['RoleName'] == self._wizard_role_name):
                    return role
        return None

    def get_ei_role(self):
        roles_reponse = self._iam_Client.list_roles()

        for index, role in enumerate(roles_reponse['Roles']):
            for statement in role['AssumeRolePolicyDocument']['Statement']:
                if(statement['Action']) == 'elastic-inference:Connect':
                    return role
                else :
                    index = index + 1
                    print("{} Role : {}\n".format(index, statement['Action']))

            return  None


class EC2:
    """
    A wrapper class encapsulating EC2 client. This class is the workhorse of this script
    Some of the key functions provided by this class
    1. Query latest AMI, launch and wait for instance to reach running state
    2. It filters out the AZs that do not have Amazon EI service available
    3. Create AWS private link endpoint, if it is not found in a given VPC

    """
    def __init__(self, awsSession ):
        try:
            self._aws_Session = awsSession
            self._ec2_Client = self._aws_Session.getClient('ec2')

        except Exception as ex:
            self._aws_Session = None
            self._ec2_Client = None

    def get_ami(self,ami_name):
        response = self._ec2_Client.describe_images(
            Owners=['amazon'],
            Filters=[
                {'Name': 'name', 'Values': [ami_name]},
                {'Name': 'architecture', 'Values': ['x86_64']},
                {'Name': 'root-device-type', 'Values': ['ebs']},
            ],
        )
        return  sorted(response['Images'],
              key=lambda x: x['CreationDate'],
              reverse=True)

    def get_ubuntu_ami(self):
        return self.get_ami('Deep Learning AMI (Ubuntu*')[0]


    def get_linux_ami(self):
        return self.get_ami('Deep Learning AMI (Amazon Linux)*')[0]

    def get_keypairs(self):
        return self._ec2_Client.describe_key_pairs()


    def launch_instance(self,image_id,instance_type,key_name,security_group,subnet_id,instance_profile, accelerator_type):

        launch_response = self._ec2_Client.run_instances(ImageId=image_id,
                                       InstanceType =instance_type,
                                       KeyName=key_name,
                                       MaxCount=1,
                                       MinCount=1,
                                       IamInstanceProfile =
                                       {
                                        'Name':instance_profile
                                       },
                                       ElasticInferenceAccelerators =
                                       [
                                           {
                                               'Type' : accelerator_type
                                           }
                                       ],

                                        NetworkInterfaces=[{'SubnetId': subnet_id, 'DeviceIndex': 0,
                                                            'AssociatePublicIpAddress': True,
                                                            'Groups': [security_group]}]

                                       )
        return launch_response

    def get_instance_ssh_command(self,instance_id,platform,key_pair):

        waiter = self._ec2_Client.get_waiter('instance_running')
        waiter.wait(InstanceIds=[instance_id])

        response = self._ec2_Client.describe_instances(InstanceIds=[instance_id])
        dns = response["Reservations"][0]["Instances"][0]['PublicDnsName']

        user = None

        if(platform == 'Linux'):
            user = 'ec2-user'
        else:
             user = 'ubuntu'

        ssh_command = 'ssh -i "{}.pem" {}@{}'.format(key_pair,user,dns)

        return ssh_command


    def create_endpoint(self,region_name,vpc_id,security_group,subnet_id):
        assert self.is_ei_service_available(region_name) == True

        ei_service_name = "com.amazonaws.{}.elastic-inference.runtime".format(region_name)
        response = self._ec2_Client.describe_vpc_endpoints(Filters= [
                {
                    'Name': 'service-name',
                    'Values': [
                        ei_service_name,
                    ]
                },
                {
                    'Name': 'vpc-id',
                    'Values': [
                    vpc_id,
                    ]
                },

                ] )

        if len(response['VpcEndpoints']) == 0:
            print("\n Creating VPC endpoint for service: {}".format(ei_service_name))

            vpc_reponse_dns = self._ec2_Client.modify_vpc_attribute(
                EnableDnsSupport={
                    'Value': True
                },
                VpcId=vpc_id)

            vpc_reponse_host = self._ec2_Client.modify_vpc_attribute(
                EnableDnsHostnames={
                    'Value': True
                },
                VpcId=vpc_id)


            endpoint_response = self._ec2_Client.create_vpc_endpoint(VpcEndpointType='Interface',VpcId=vpc_id,
                                                ServiceName=ei_service_name,
                                                SubnetIds = [subnet_id],
                                                SecurityGroupIds=[security_group],
                                                PrivateDnsEnabled=True)

            return True

        else :
            print("\n Discovered VPC endpoint for Amazon EI service, ID: {}".format(response['VpcEndpoints'][0]['VpcEndpointId']))
            self.synch_vpc_endpoint_safe(response,security_group,subnet_id)

            return False

    def synch_vpc_endpoint_safe(self,vpc_endpoint_description,security_group,subnet_id):
        """
        Modifies VPC endpoint by adding the security group and subnet if these are not already added
        :param vpc_endpoint_description: the response for describe_vpc_endpoints from boto3
        :param security_group: the security group to be added to this VPC endpoint
        :param subnet_id: the subnet to be added to this VPC endpoint
        :return:
        """

        vpc_ep_id = vpc_endpoint_description['VpcEndpoints'][0]['VpcEndpointId']

        subnet_list = vpc_endpoint_description['VpcEndpoints'][0]['SubnetIds']

        add_subnet = True
        if subnet_id in subnet_list:
            add_subnet = False


        groups = vpc_endpoint_description['VpcEndpoints'][0]['Groups']

        add_group = True
        for group in groups:
            if group['GroupId'] == security_group:
                add_group = False
                break

        private_dns = vpc_endpoint_description['VpcEndpoints'][0]['PrivateDnsEnabled']

        if add_subnet == True:
            print("\n Adding subnet {} to VPC endpoint.".format(subnet_id))
            self._ec2_Client.modify_vpc_endpoint(VpcEndpointId= vpc_ep_id, AddSubnetIds=[subnet_id])


        if add_group:
            print("\n Adding Security Group {} to VPC endpoint.".format(security_group))
            self._ec2_Client.modify_vpc_endpoint(VpcEndpointId=vpc_ep_id, AddSecurityGroupIds=[security_group])

        if private_dns == False:
            print("\n Enabling Private DNS for VPC endpoint.")
            self._ec2_Client.modify_vpc_endpoint(VpcEndpointId=vpc_ep_id,PrivateDnsEnabled=True)



    def is_ei_service_available(self, region_name):
        """
        checks if Amazon EI service is available, in the supplied region name, and what AZs have it
        :param region_name: the region to check availability of Amazon EI service in
        :return: return True if at lease one AZ has EI service in this region, false otherwise
        """

        try:
            ei_service_name = "com.amazonaws.{}.elastic-inference.runtime".format(region_name)
            ei_services = self._ec2_Client.describe_vpc_endpoint_services(Filters=
            [
                {
                    'Name': 'service-name',
                    'Values': [
                        ei_service_name,
                    ]
                }
            ] )

            if len(ei_services['ServiceNames']) >0:
                self._availability_zones = ei_services['ServiceDetails'][0]['AvailabilityZones']
                return True
            else:
                return False

        except Exception as ex:
            raise Exception("\n Failed to retrieve VPC endpoints for {} : {}".format(region_name, ex))

    def get_availability_zones(self):
        return self._availability_zones

    def get_vpcs(self):
        try:
            vpc_response = self._ec2_Client.describe_vpcs()['Vpcs']
        except Exception as ex:
            print(" Error retrieving VPCs.Details :{}".format(ex))


        vpc_result = []

        for vpc_index in range(len(vpc_response)):
            if(vpc_response[vpc_index]['IsDefault'] is True):
                vpc_result.insert(0,vpc_response[vpc_index]['VpcId'])
            else :
                vpc_result.append(vpc_response[vpc_index]['VpcId'])

        return vpc_result

    def get_subnets_for_vpc(self,vpc_id):
        """
        returns the subnets in given VPC filtered by AZs that have Amazon EI service available
        :param vpc_id: the ID of the VPC to use
        :return: list of subnets that have Amazon EI service
        """

        try:
            available_subnets = []
            for az in   self._availability_zones:
                query_filter = [
                {
                'Name': 'vpc-id',
                'Values': [
                    vpc_id,
                ]
                },
                {
                    'Name': 'availability-zone',
                    'Values': [
                    az,
                ]
                }
                ]

                subnets =   self._ec2_Client.describe_subnets(Filters = query_filter)['Subnets']

                for subnet in subnets:
                    if(subnet['State'] == 'available'):
                        available_subnets.append(subnet)

            return available_subnets

        except Exception as ex:
            print (" Error retrieving subnets for VPC ID {}, error :{}".format(vpc_id,ex))
            quit(1)

    def create_security_group(self,group_name,description,vpc_id, service_port):
        """
        enables inbound rules for Amazon EI service, including SSH port 22
        the outbound rules are left to be default - all ports
        """

        sec_group =  self._ec2_Client.create_security_group(GroupName=group_name, Description=description, VpcId=vpc_id)

        self.authorize_security_group_ingress(sec_group['GroupId'],service_port)

        self.authorize_security_group_ingress(sec_group['GroupId'],22)


        return sec_group

    def authorize_security_group_ingress(self,sg_id,port):
        self._ec2_Client.authorize_security_group_ingress(GroupId=sg_id, IpProtocol="tcp",
                                                          CidrIp="0.0.0.0/0",
                                                          FromPort=port, ToPort=port)

    def describe_security_groups(self, filters):
        return self._ec2_Client.describe_security_groups(Filters=filters)




class UserInput:
    """
    A utility class to manage user inputs, including the command line params

    """

    def get_session(self):

        parser = argparse.ArgumentParser()

        parser.add_argument(
            '--region',
            dest='region',
            help='Region name in which the instance is to be launched',
            required=True)


        parser.add_argument(
            '--instance-type',
            dest='instance_type',
            help='Instance Type for example, m5.large',
            required=True)



        args = parser.parse_args()
        self._region_name = args.region
        self._instance_type= args.instance_type

        self._aws_Session = AWSSession(self._region_name)
        self._ec2 = EC2(self._aws_Session)

        if self.is_ei_service_available(self._region_name) == False:
            raise Exception("\n Amazon Elastic Inference service is not available in the specified region: '{}' ".format(self._region_name))

        return self._aws_Session



    def get_region(self):
        return self._region_name

    def get_image_id(self):
        platforms = ['Amazon Linux', 'Ubuntu']

        print("\nThis script launches Amazon EC2 instances with Amazon Elastic Inference accelerators. This script performs the following functions:"
                "\n 1. It uses the Deep Learning AMIs preconfigured with EI-enabled deep learning frameworks to launch the instances."
                "\n 2. It creates security groups for the instance and VPC endpoint."
                "\n 3. It creates the VPC endpoint needed for your instances to communicate with EI accelerators."
                "\n 4. It creates an IAM Instance Role and Policy with the permissions needed to connect to accelerators."
              "\n\n To begin, please choose the Operating System for your instance by typing its index :\n")

        for index, platform in enumerate(platforms):
            print(" {}: {}".format(index,platform))

        selection = self._get_selection(0,len(platforms)-1)

        if(selection == 0):
            self._platform = 'Linux'
            return self._ec2.get_linux_ami()
        else:
            self._platform = 'Ubuntu'
            return self._ec2.get_ubuntu_ami()


    def get_platform(self):
        return self._platform

    def get_instance_type(self):
        return self._instance_type


    def get_key_pair(self):

        response = self._ec2.get_keypairs()
        key_pairs = response['KeyPairs']

        if len(key_pairs) == 0:
            print("\nNo key pair found. Please create a key pair and run the setup script again.\n")
            quit(1)

        selection = 0
        if len(key_pairs) > 1 :
            print("\nPlease type index of the key pair type to use:\n")


            for index, key_pair in enumerate(key_pairs):
                print(" {}: {}".format(index,key_pair['KeyName']))

            selection = self._get_selection(0, len(key_pairs)-1)

        return key_pairs[selection]['KeyName']


    def is_ei_service_available(self,region_name):
        return self._ec2.is_ei_service_available(region_name)


    def get_accelerator_type(self):
        accel_types = ['eia2.medium','eia2.large','eia2.xlarge','eia1.medium','eia1.large','eia1.xlarge']
        accel_memory = ['2 GB of accelerator memory','4 GB of accelerator memory','8 GB of accelerator memory','1 GB of accelerator memory','2 GB of accelerator memory','4 GB of accelerator memory']

        print("\nPlease type index of the accelerator type to use: (Note: Please select eia2. This is our latest family of accelerators with double the memory and lower costs than eia1. Note that you will have to use eia1 in ap-northeast-1 Region)\n")
        
        for index, accel in enumerate(accel_types):
            print(" {}: {} ({})".format(index,accel,accel_memory[index]))

        selection = self._get_selection(0,len(accel_types)-1)
        return accel_types[selection]

    def get_vpc_id(self):

        vpc_id_list = self._ec2.get_vpcs()

        if(len(vpc_id_list)==0):
            return None

        selection = 0
        if (len(vpc_id_list) > 1):
            print("\nPlease select the VPC to use by typing the desired VPC index. Type 0 for default VPC.\n")

            for vpc_index, vpc_id in enumerate(vpc_id_list):
                print(" {}: VPC Id '{}'".format(vpc_index, vpc_id))

            selection = self._get_selection(0, len(vpc_id_list)-1)

        return vpc_id_list[selection]

    def get_subnet(self,vpc_id):
        """
        This is critical validation - we need a subnet that is in an AZ where Amazon EI is supported
        :param vpc_id: The VPC ID chosen by the user
        :return: all the subnets associated with the zones in this VPC where Amazon EI service is available
        """

        subnets = self._ec2.get_subnets_for_vpc(vpc_id)

        if len(subnets) == 0:
            print("\nNo subnet found. Please create a Subnet in one of the following AZs for VPC ID: {}, and run this utility again:".format(vpc_id))

            availability_zones = self._ec2.get_availability_zones()
            for az_index, az in enumerate(availability_zones):
                print(" {}: {}".format(az_index,az))

            quit()

        selection = 0
        if len(subnets) > 1:
            print("\nPlease select the Subnet to use by typing the index of the desired Subnet:\n")

            for subnet_index, subnet in enumerate(subnets):
                print(" {}: SubnetID '{}', AvailabilityZone '{}'".format( subnet_index,subnet['SubnetId'],subnet['AvailabilityZone']))

            selection = self._get_selection(0, len(subnets) - 1)

        return subnets[selection]

    def get_security_groups(self,vpc_id,service_port):
        Filters = [
            {
                'Name': 'ip-permission.from-port',
                'Values': [service_port]
            },
            {
                'Name': 'ip-permission.to-port',
                'Values': [service_port]
            },
            {
                'Name': 'ip-permission.from-port',
                'Values': ['22']
            },
            {
                'Name': 'ip-permission.to-port',
                'Values': ['22']
            },

            {
                'Name': 'vpc-id',
                'Values': [vpc_id]
            }
        ]


        sg_response = self._ec2.describe_security_groups(Filters)

        if len(sg_response['SecurityGroups']) == 0:
            return None

        selection = 0

        if len(sg_response['SecurityGroups'])  > 1:
            print("\nPlease select the Security Group to use by typing the index of the desired Security Group:\n")

            for sg_index, sg in enumerate(sg_response['SecurityGroups']):
                print(" {}: GroupID  '{}', GroupName  '{}'".format(sg_index,sg['GroupId'],sg['GroupName']))

            selection = self._get_selection(0, len(sg_response['SecurityGroups'])-1)

        return sg_response['SecurityGroups'][selection]['GroupId']

    def create_security_group(self, group_name, description, vpc_id, service_port):
        return self._ec2.create_security_group(group_name,description,vpc_id,service_port)


    def _get_selection(self,low_index,high_index):

        selection = input("\nType 'q' to quit.\namazonei-wizard>")
        while selection.isdigit() == False or int(selection) < low_index or int(selection) > high_index:
            if selection =='q' or selection =='Q':
                quit()
            print("Please enter a number from {} to {}, inclusive. Type 'q' to quit.\n".format(low_index,high_index))
            selection = input("\namazonei-wizard>")

        return  int(selection)


    def get_confirmation(self):
        selection = input("\nType 'y' to continue. Type 'q' to quit.\namazonei-wizard>")
        while selection != 'y' and selection != 'q' and selection != 'Y' and selection != 'Q':
            selection = input("\nType 'y' to continue. Type 'q' to quit.\namazonei-wizard>")

        if selection == 'q' or selection == 'Q':
            quit()

        return selection


if __name__ == "__main__":
    #check boto3 version
    if StrictVersion(boto3.__version__)<StrictVersion('1.9.71'):
        logErrorAndQuit("Minimum boto3 version required is 1.9.71. Found version - " + boto3.__version__ + ". Please update it using command - 'sudo pip install --upgrade boto3'")

    try:
        user_input = UserInput()
        aws_session = user_input.get_session()

        if aws_session == None:
            quit()

        region = user_input.get_region()
        image_id = user_input.get_image_id()

        ec2_client = EC2(aws_session)

        iam_client = IAM(aws_session)

        print(" Using Image ID: {},Image Name: {}".format(image_id['ImageId'],image_id['Name']))

        instance_type = user_input.get_instance_type()

        print(" Using instance type: {}".format(instance_type))

        key_pair = user_input.get_key_pair()

        print(" Using Key Pair: {}".format(key_pair))

        accel_type = user_input.get_accelerator_type()

        print(" Using Amazon EI accelerator type: {}".format(accel_type))

        wizard_role = iam_client.find_wizard_role()

        if(wizard_role == None):
            print("\n Did not discover any pre-existing role configured with policy for connecting to Amazon EI service. This script will now create required role and policies.")
            role = iam_client.create_wizard_role()
            print("\n Successfully created role: {}".format(role))
        else:
            print("\n Found an IAM role configured for connecting to Amazon EI service. Name - {}, ARN - {}".format(wizard_role['RoleName'],wizard_role['Arn']))

        iam_client.create_instance_profile()

        vpc_id = user_input.get_vpc_id()

        if vpc_id == None:
            raise Exception("\n No VPC found for the given region")

        print(" Using VPC ID: {}".format(vpc_id))

        sg_id = user_input.get_security_groups(vpc_id,'443')

        if sg_id == None:
            print(" The EC2 instance and the private link endpoint require a security group with TCP port 443 enabled. This script will now create a security group with the required inbound rules.")
            sg_response = user_input.create_security_group('amazon_ei_security_group','Security Group for accessing Amazon EI service',vpc_id,443)
            print(" Successfully Created Security Group to be used.\n Security Group ID: {}".format(sg_response['GroupId']))
            sg_id = sg_response['GroupId']

        else :
            print(" Using Security Group: {}".format(sg_id))

        subnet_id = user_input.get_subnet(vpc_id)['SubnetId']

        print(" Using Subnet: {}".format(subnet_id))


        ec2_client.create_endpoint(region,vpc_id,sg_id,subnet_id)


        summary = "\n The script will now launch new instance with following configuration. Type 'y' to continue. \n\n Accelerator Type: {}\n Region: {}\n Image-ID: {} - ({})\n Instance Type: {}\n Key Pair: {}\n Security Group ID: {}\n Subnet ID: {}\n Instance Profile: {}".format\
                (
            accel_type,region,image_id['ImageId'],image_id['Name'],instance_type,key_pair,sg_id,subnet_id,iam_client.get_instance_profile_name()
        )
        print(summary)
        confirmation = user_input.get_confirmation()
        if(confirmation == 'y' or confirmation == 'Y'):

            print("\n Launching Instance ..")
            launch_response = ec2_client.launch_instance(image_id['ImageId'],instance_type,key_pair,sg_id,subnet_id,iam_client.get_instance_profile_name(),accel_type)


            instance_id = launch_response['Instances'][0]['InstanceId']
            print("\n Launched instance successfully. The instance ID is '{}'.".format(instance_id))
            print("\n Waiting for instance to reach running state ...")

            login_command = ec2_client.get_instance_ssh_command(instance_id, user_input.get_platform(),key_pair)

            print("\n You can use the following sample SSH command to connect to your instance: {}\n".format(login_command))


            print("\n Note: Please wait until instance is fully initialized and ready to accept SSH connections. You may check instance status at EC2 console.\n Also please locate " 
                  "your private key file '{}.pem'.\n".format(key_pair))


    except Exception as ex:
        print("Error setting up Amazon EI configuration - {}".format(ex))

