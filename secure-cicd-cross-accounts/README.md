# Secure a cross-accounts CI/CD Pipeline

Three AWS Accounts:

* GitEE: 172.17.0.0/16
* DevOps: 172.18.0.0/16
* Beta: 172.19.0.0/16, 

## Setup1

* Deploy from devops account to Beta Account [link](https://aws.amazon.com/blogs/devops/aws-codedeploy-deploying-from-a-development-account-to-a-production-account/) and [link](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-cross-account.html)

* DevOps Account Create ECR
* Grant account Beta to access DevOps ECR. Modify the ECR repsoitory policy [link](https://stackoverflow.com/questions/52914713/aws-ecs-fargate-pull-image-from-a-cross-account-ecr-repo)

```
{
  "Version": "2008-10-17",
  "Statement": [
    {
      "Sid": "AllowCrossAccountPull",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT_Beta_ID:root"
      },
      "Action": [
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchCheckLayerAvailability",
        "ecr:BatchGetImage"
      ]
    }
  ]
}
```

## Step 3 Create a role under beta account for cross account deployment

* pipelines for cross account [link](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create-cross-account.html)
* The artifact was created in the pipeline account for an action in another account.


```
An error occurred (InvalidStructureException) when calling the UpdatePipeline operation: arn:aws:iam::account-devops:role/service-role/AWSCodePipelineServiceRole-us-east-1-sample-website is not authorized to perform AssumeRole on role arn:aws:iam::account-beta:role/codeDeployRoleForECS
```

