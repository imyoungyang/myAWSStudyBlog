# AWS IAM Policy Ninja Workshop - Lambda

In AWS Lambda, the primary resources are a Lambda function and an event source mapping.

## Lambda fuction

|  Resource Type | ARN Format  |   
|---|---|
| Function | arn:aws:lambda:region:account-id:function:function-name |
| Function alias	| arn:aws:lambda:region:account-id:function:function-name:alias-name |
| Function version | arn:aws:lambda:region:account-id:function:function-name:version |

## Event source mapping

|  Resource Type | ARN Format  | 
|---|---|
| Event source mapping	| arn:aws:lambda:region:account-id:event-source-mapping:event-source-mapping-id |


## Lambda Envoke Modes

Lambda event source, which means invoke lambda modes. The common modes are:

1. AWS services:
2. AWS poll-based services
3. Custom Applications

### AWS services
**AWS services**: such as s3 trigger lambda when an object puts into a bucket:

* Event source mappings are maintained within the event source.  For example, Amazon S3 provides the bucket notification configuration API.
*  you need to grant the event source (e.g. S3) the necessary permissions using a resource-based policy (referred to as the Lambda function policy).

	For exmaple:
	<pre>
	aws lambda add-permission \
	--region region \
	--function-name helloworld \
	--statement-id 5 \
	--principal apigateway.amazonaws.com \
	--action lambda:InvokeFunction \
	--source-arn arn:aws:execute-api:region:account-id:api-id/stage/method/resource-path \
	--profile adminuser
	</pre>

	Example 2: Allow Amazon API Gateway to Invoke a Lambda Function

	<pre>
	aws lambda add-permission \
	--region region \
	--function-name helloworld \
	--statement-id 5 \
	--principal apigateway.amazonaws.com \
	--action lambda:InvokeFunction \
	--source-arn arn:aws:execute-api:region:account-id:api-id/stage/method/resource-path \
	--profile adminuser
	</pre>

### AWS poll-based services
**AWS poll-based services**: The following three services are poll-based:

* Amazon Kinesis
* Amazon DynamoDB
* Amazon SQS

The key different from 1st mode-AWS services is:

* The event source mappings are maintained within the AWS Lambda, which uses `create-event-source-mapping` API.
* AWS Lambda needs your permission to poll Kinesis and DynamoDB streams or Amazon SQS queues and read records.

	For example: Amazon Kinesis Data Stream trigger lambda
	<pre>
	$ aws lambda create-event-source-mapping \
	--function-name my-function --no-enabled \
	--batch-size 500 --starting-position AT_TIMESTAMP \
	--starting-position-timestamp 1541139109 \
	--event-source-arn arn:aws:kinesis:us-east-2:123456789012:stream/	my-stream
	{
	    "UUID": "2b733gdc-8ac3-cdf5-af3a-1827b3b11284",
	    "BatchSize": 500,
	    "EventSourceArn": "arn:aws:kinesis:us-east-2:123456789012:stream/lambda-kinesis-stream",
	    "FunctionArn": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
	    "LastModified": 1541139209.351,
	    "LastProcessingResult": "No records processed",
	    "State": "Creating",
	    "StateTransitionReason": "User action"
	}
	</pre>

	Second step: setup the execution role of lamdba to access kinesis resoucres:
	
	* kinesis:DescribeStream
	* kinesis:DescribeStreamSummary
	* kinesis:GetRecords
	* kinesis:GetShardIterator
	* kinesis:ListShards
	* kinesis:ListStreams
	* kinesis:SubscribeToShard
	
	The AWSLambdaKinesisExecutionRole managed policy includes these permissions

### Custom Applications
**Custom Applications**: If you have custom applications that publish and process events, you can create a Lambda function to process these events. In this case, there is no preconfiguration required—you don't have to set up an event source mapping. Instead, the event source uses the AWS Lambda Invoke API.

For example: Allow a User Application Created by Another AWS Account to Invoke a Lambda Function (Cross-Account Scenario):
	
	<pre>
	aws lambda add-permission \
	--region region \
	--function-name helloworld \
	--statement-id 3 \
	--principal 111111111111 \
	--action lambda:InvokeFunction \
	--profile adminuser
	</pre>

Please reference the [lambda invocation modes](https://docs.aws.amazon.com/lambda/latest/dg/intro-invocation-modes.html#custom-app-event-source-mapping)

## Lambda Execution Role

Permissions you grant to this role determine what AWS Lambda can do when it assumes the role. The user that creates the IAM role needs to pass the role to the lambda. This requires the user to have permissions for the `iam:PassRole` action.

* AWSLambdaBasicExecutionRole – Grants permissions only for the Amazon CloudWatch Logs actions to write logs. You can use this policy if your Lambda function does not access any other AWS resources except writing logs.

* AWSLambdaKinesisExecutionRole – Grants permissions for Amazon Kinesis Data Streams actions, and CloudWatch Logs actions. If you are writing a Lambda function to process Kinesis stream events you can attach this permissions policy.

* AWSLambdaDynamoDBExecutionRole – Grants permissions for DynamoDB streams actions and CloudWatch Logs actions. If you are writing a Lambda function to process DynamoDB stream events you can attach this permissions policy.

* AWSLambdaVPCAccessExecutionRole – Grants permissions for Amazon Elastic Compute Cloud (Amazon EC2) actions to manage elastic network interfaces (ENIs). If you are writing a Lambda function to access resources in a VPC in the Amazon Virtual Private Cloud (Amazon VPC) service, you can attach this permissions policy. The policy also grants permissions for CloudWatch Logs actions to write logs.

## Lambda Console

* Reference the document [link](https://docs.aws.amazon.com/lambda/latest/dg/console-specific-permissions.html#console-permissions-api-gateway)