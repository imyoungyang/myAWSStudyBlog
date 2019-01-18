# Enable APIGW CloudWatch Logs

In this article, you will learn how to setup the API logs and Cloudwatch group.

## General Setting for Admin

* Enable Settings

![](images/apigw-01.png)

* input cloudwatch log arn. Reference the setting documents [link](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html#set-up-access-logging-permissions)

![](images/apigw-02.png)

* open IAM in the new tab. Create new role.

![](images/apigw-03.png)

* click on the service 'api gateway'

![](images/apigw-04.png)

* use default list policy

![](images/apigw-05.png)

* add tag name with value `AmazonAPIGatewayPushToCloudWatchLogs`

![](images/apigw-06.png)

* Role name `AmazonAPIGatewayPushToCloudWatchLogs` then create role.

![](images/apigw-07.png)

* Copy role name arn and input into the api gateway settings.

![](images/apigw-08.png)

## Create a cloud watch group

* In the cloudwatch console, create the log group

![](images/apigw-09.png)

* Input log group name `/aws/apigw/beacon`

![](images/apigw-10.png)

* Click on the setting and turn on the arn field

![](images/apigw-12.png)
![](images/apigw-13.png)