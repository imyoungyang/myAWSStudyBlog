# Multi VPC in different AWS Acounts

Some AWS resources that are sharable between accounts allow for the transfer of useful data between accounts. The key mechanisms are:

- EC2 Amazon Machine Images (AMIs)
- AWS EBS volume snapshots
- Amazon RDS backup/snapshots
- Amazon S3 Buckets

For the VPCs, you need to consider VPC-Peering or other strategies.

## AWS Multi Accounts Strategy
* [AWS Multiple Account Security Strategy](https://aws.amazon.com/answers/account-management/aws-multi-account-security-strategy/)
* [AWS Multiple Account Billing Strategy](https://aws.amazon.com/answers/account-management/aws-multi-account-billing-strategy/)
* [Tutorial: Delegate Access Across AWS Accounts Using IAM Roles](http://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)
* [Controlling Access to Amazon VPC Resources](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_IAM.html)

## Connect Multi-VPCs
* [How do I create an AWS IAM policy to restrict access for an IAM user, group, or role to a particular Amazon Virtual Private Cloud?](https://aws.amazon.com/premiumsupport/knowledge-center/iam-policy-restrict-vpc/)
* [From One to Many: Evolving VPC Design](http://awsmedia.s3.amazonaws.com/ARC401.pdf)
* [Single region multi-vpc connectivity](https://d0.awsstatic.com/aws-answers/AWS_Single_Region_Multi_VPC_Connectivity.pdf)
* [Multi regions multi-vpc connectivity](https://d0.awsstatic.com/aws-answers/AWS_Multiple_Region_Multi_VPC_Connectivity.pdf)