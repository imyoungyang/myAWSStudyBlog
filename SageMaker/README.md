# Bring your own container on Amazon SageMaker Lab

1. create a [cloud9](https://console.aws.amazon.com/cloud9/home?region=us-east-1) environment in `east-us-1` with name: `sagemaker-container-workshop` and type `t2.micro`.

1. In cloud9, bash shell exec:
`git clone https://github.com/awslabs/amazon-sagemaker-examples.git`

1. `cd amazon-sagemaker-examples/advanced_functionality/scikit_bring_your_own/container/`
2. Build the docker image: `./build_and_push.sh <image-name>`. Image name suggest to use `scikit-<your-id>` format.
	![](images/01-cloud9.png)

3.  

### Reference
* [Blog](https://aws.amazon.com/blogs/machine-learning/train-and-host-scikit-learn-models-in-amazon-sagemaker-by-building-a-scikit-docker-container/)