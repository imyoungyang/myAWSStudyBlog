# MLOps Workshop

* Working at us-east-2 (Ohio)

# MLOps DevOps Account
1. create org and developers aws account
2. create repo: `scikit-learn-iris`
git clone https://git-codecommit.us-east-2.amazonaws.com/v1/repos/scikit-learn-iris
3. create `mlops-developers` IAM user and security credentials for `HTTPS Git credentials for AWS CodeCommit`
4. Switch role: Admin @ mlops-developers

# MLOps Developers

## Create an IAM user
1. Change the IAM sign-in url: beyoung-mlops-developers
2. Create IAM user: `beyoung` @ aws account`beyoung-mlops-developers`

## mlops-developers

Suggest to use different browser such as safari for this account login.

1. Sign-in new url: beyoung-mlops-developers
2. Cloud9: `mlops-dev` @ `us-east-2`

### Config the credit

**MUST Turn off aws cloud9 credentials**

1. `vim ~/.aws/config`

	```
	[profile mlops-devops]
	output = json
	region = us-east-2
	[default]
	output = json
	region = us-east-2
	```

2. `vim ~/.aws/credentials` Put the profile `mlops-devops` access and secret key, which is created in the `mlops` account IAM user ``mlops-developers`.

	```
	[default]
	aws_access_key_id = xxxxx
	aws_secret_access_key = xxxx
	[mlops-devops]
	aws_access_key_id = xxxx
	aws_secret_access_key = xxxx
	```

### Change `~/.gitconfig`

Let aws git profile use `mlops-devops` account.

```
[credential]
        helper = !aws --profile mlops-devops codecommit credential-helper $@
        UseHttpPath = true
[core]
        editor = /usr/bin/vim
```

### Clone sagemaker example and push to devops account repos

3. git clone https://github.com/awslabs/amazon-sagemaker-examples
mkdir mlops-devops
4. `cp -r amazon-sagemaker-examples/advanced_functionality/scikit_bring_your_own/ .`
5. `cd ./scikit_bring_your_own`
6. `git init`
7. `git remote add origin https://git-codecommit.us-east-2.amazonaws.com/v1/repos/scikit-learn-iris`
8. `git remote -v`
9. git add .
9. git commit -m "init"
10. `git push origin master -u`

### Call SageMaker Training with bring your own container

We use the SageMaker estimator. The most effective way to call remote training at DevOps account.

```
tree = sage.estimator.Estimator(image,
    role, 1, 'ml.c4.2xlarge',
    output_path=output_location,
    sagemaker_session=sess)
tree.fit(inputs=data_location, wait=False)
```

### Create training jobs at beta account

1. secrets manager to keep the creditials of beta account
2. `buildspec.yml` access the secrets managers.
3. ERC in devops account grant permission to beta. [ref1](https://aws.amazon.com/premiumsupport/knowledge-center/secondary-account-access-ecr/) [ref2](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html#IAM_allow_other_accounts)
4. beta account sagemaker execution role add policy to access devops account ecr. [ref](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr_managed_policies.html)

### Create models from beta account results into devops account

* s3 cross account access [ref](https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/)
* SageMaker Execution Role can access s3 bucket in beta

### Create models from beta account results into PRD account

* s3 cross account access [ref](https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/)
* Create group: `SageMaker`
* SageMaker Execution Role can access s3 bucket in beta
* Create IAM user: `beyoung-prod-sagemaker`
* Create role: `SageMakerExecutionRole` and attach policy `s3:GetObject`
* 

# Reference
* [aws git cross accounts](https://aws.amazon.com/blogs/devops/using-git-with-aws-codecommit-across-multiple-aws-accounts/)
* [Training job json](https://docs.aws.amazon.com/sagemaker/latest/dg/API_CreateTrainingJob.html)
* [MLOps Workshop](https://github.com/awslabs/amazon-sagemaker-mlops-workshop)
* [SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/estimators.html)
* [SageMaker Python SDK example](https://github.com/awslabs/amazon-sagemaker-examples/blob/master/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.ipynb)
* [Use API JSON example](https://github.com/awslabs/amazon-sagemaker-examples/blob/master/ground_truth_labeling_jobs/object_detection_augmented_manifest_training/object_detection_augmented_manifest_training.ipynb)
