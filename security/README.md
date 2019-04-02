# Cloud Security
* [Data Safe Cloud Checklist](https://aws.amazon.com/campaigns/cloud-security/data-safe-cloud-checklist/)

# Multi-Account
* [Multi-Account Workshop](http://multiaccount.reinvent-workshop.com/)

# Parameter Stores

#### Blogs
* [The right way to store secrets using parameter store](https://aws.amazon.com/tw/blogs/mt/the-right-way-to-store-secrets-using-parameter-store/)
* [Managing Secrets for Amazon ECS Applications Using Parameter Store and IAM Roles for Tasks](https://aws.amazon.com/tw/blogs/compute/managing-secrets-for-amazon-ecs-applications-using-parameter-store-and-iam-roles-for-tasks/)
* [How to Manage Secrets for Amazon EC2 Container Service–Based Applications by Using Amazon S3 and Docker](https://aws.amazon.com/tw/blogs/security/how-to-manage-secrets-for-amazon-ec2-container-service-based-applications-by-using-amazon-s3-and-docker/)

#### Webinar
* [Managing Secrets for Containers with Amazon ECS](https://www.youtube.com/watch?v=5gBk6TZJ3jo)

# ECS CI/CD Deploy

* [Blue/Green Deployments with Amazon EC2 Container Service](https://aws.amazon.com/tw/blogs/compute/bluegreen-deployments-with-amazon-ecs/)
* Hands on CI/CD reference architecutres
	* [ecs-refarch-continuous-deployment](https://github.com/awslabs/ecs-refarch-continuous-deployment)
	* [ecs-canary-blue-green-deployment](https://github.com/awslabs/ecs-canary-blue-green-deployment)
	* [ecs-blue-green-deployment](https://github.com/awslabs/ecs-blue-green-deployment)

# Cognito

* Demo [link](https://s3-ap-northeast-1.amazonaws.com/tsukada-aws/demos/cognito-user-pools-custom-auth/index.html)

# Docker Network Modes

* The Docker networking mode to use for the containers in the task. The valid values are `none, bridge, awsvpc, and host`. 
* The default Docker network mode is `bridge`. If using the Fargate launch type, the `awsvpc` network mode is required. If using the EC2 launch type, any network mode can be used.
* The `host` and `awsvpc` network modes offer **the highest networking performance** for containers because they use the Amazon EC2 network stack.
*  