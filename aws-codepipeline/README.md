# Steps
1. Create github organization
2. Create api gateway with labmda to get the webhook payload
3. Create webhook in the github organization [link](https://developer.github.com/webhooks/creating/). Content type use `application/json`

# Codebuild or CodePipeline

## CodeBuild
AWS CodeBuild is a fully managed **continuous integration** service that compiles source code, runs tests, and **produces software packages that are ready to deploy**.

## CodePipeline
AWS CodePipeline is a **continuous delivery** service you can use to model, visualize, and automate the steps required to release your software. The service currently supports GitHub (github.com), AWS CodeCommit, and Amazon S3 as source providers. CodePipeline integrates continuous integration and continuous delivery services, making it simple to automatically deploy your updated application.

**Important**: Code pipeline source did not support customized GitHub address ie. enterprise GitHub.

# Git Authentication

Which remote URL should I use? HTTPS or SSH [link](https://help.github.com/en/articles/which-remote-url-should-i-use)


## Personal access token (HTTPS)
A personal access token is required to authenticate to GitHub in the following situations:

* When you're using two-factor authentication
* To access protected content in an organization that uses SAML single sign-on (SSO). Tokens used with organizations that use SAML SSO must be authorized.

Create a personal access token step by step is [here](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)

**important**
	
Personal access tokens can only be used for **HTTPS Git operations**. If your repository uses an SSH remote URL, you will need to switch the remote from SSH to HTTPS. The step is [here](https://help.github.com/en/articles/changing-a-remotes-url#switching-remote-urls-from-ssh-to-https)

## Git ssh
SSH URLs provide access to a Git repository via SSH, a secure protocol. To use these URLs, you must generate an SSH keypair on your computer and add the public key to your GitHub account. For information on setting up an SSH keypair, see [Generating an SSH key](https://help.github.com/en/articles/connecting-to-github-with-ssh) or [here](https://build-me-the-docs-please.readthedocs.io/en/latest/Using_Git/SetUpSSHForGit.html)


# Lambda handle git, aws-cli, and ssh
* [Lambda runtime environment](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) does not have git command.
* [Running git in lambda function](https://cloudbriefly.com/post/running-git-in-aws-lambda/)
* Use the [sh.git()](https://amoffat.github.io/sh/index.html#subcommands) in python is the easy way. Can reference [stockoverflow](https://stackoverflow.com/questions/1456269/python-git-module-experiences)
* git ssh lambda layer [here](https://github.com/lambci/git-lambda-layer)
* aws-cli lambda layer [here](https://github.com/aws-samples/aws-lambda-layer-awscli)
* gitPullS3-lambda [here](./others/gitPullS3-lambda.zip)

# Git flow
* [Implementing gitflow using codepipeline, codecommit, codebuild and codedeploy](https://aws.amazon.com/blogs/devops/implementing-gitflow-using-aws-codepipeline-aws-codecommit-aws-codebuild-and-aws-codedeploy/)

# CDK
* [CDK APP Delivery](https://github.com/awslabs/aws-cdk/tree/master/packages/%40aws-cdk/app-delivery)
* [CDK Codebuild soure github enterprise](https://awslabs.github.io/aws-cdk/refs/_aws-cdk_aws-codebuild.html#githubsource-and-githubenterprisesource)
* [CDK connect github with personal token](https://github.com/awslabs/aws-cdk/issues/1844)
* [Codebuild create webhook](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_CreateWebhook.html) and cli [command line](https://docs.aws.amazon.com/cli/latest/reference/codebuild/create-webhook.html)

# Git Webhook
* [Create webhook via console](https://developer.github.com/webhooks/creating/)
* [Create webhook via API](https://developer.github.com/v3/repos/hooks/#create-a-hook)
* 1st setup the webhook in Org or repo. It will trigger [ping event](https://developer.github.com/webhooks/#ping-event). The sample payload is [here](./others/1st-create-webhook-ping-event-payload.json)
* 1st create the repo. Git will trigger [create event](https://developer.github.com/v3/activity/events/types/#createevent). The sample payload is [here](./others/1st-create-repo-payload.json)

## Authetication of webhook api
* Must read github [developer guide](https://developer.github.com/v3/#authentication)
* When you get `404 Not Found` or body with `"message": "Not Found"`, it means the api need authetication.
* Suggestion use `OAuth2 token` in the header. Such as 

	```
	curl -H "Authorization: token OAUTH-TOKEN" https://api.github.com
	```

# Reference
* [Integrating Git with AWS CodePipeline]
(https://aws.amazon.com/blogs/devops/integrating-git-with-aws-codepipeline/)
* [git to s3 using webhooks]
(https://aws.amazon.com/quickstart/architecture/git-to-s3-using-webhooks/)
* [AWS CodeBuild Support for GitHub Enterprise as a Source Type and Shallow Cloning]
(https://aws.amazon.com/blogs/devops/codebuild-support-for-github-enterprise/)
* [Git enterprise on AWS](https://aws.amazon.com/quickstart/architecture/github-enterprise/)
* [Serverless CI/CD for enterprises](https://aws.amazon.com/quickstart/architecture/serverless-cicd-for-enterprise/), which follow AWS multi-account best practices for isolation of resources.
* [Git personal access token for command line](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
* [Lambda GitPulltoS3](http://aws-quickstart.s3.amazonaws.com/quickstart-git2s3/functions/packages/GitPullS3/lambda.zip)
* [Access s3 bucket url](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#access-bucket-intro)