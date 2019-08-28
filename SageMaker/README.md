# Bring your own container on Amazon SageMaker Lab

1. create a [cloud9](https://console.aws.amazon.com/cloud9/home?region=us-east-1) environment in `east-us-1` with name: `sagemaker-container-workshop` and type `t2.micro`.

1. In cloud9, bash shell exec:
`git clone https://github.com/awslabs/amazon-sagemaker-examples.git`

1. `cd amazon-sagemaker-examples/advanced_functionality/scikit_bring_your_own/container/`
2. Build the docker image: `./build_and_push.sh <image-name>`. Image name suggest to use `scikit-<your-name>` format.
	![](images/01-cloud9.png)

3. `docker images`: you will see `scikit-<your-name>` with `latest` TAG in your cloud9 and ecr respository.
	![](images/02-cloud9.png)

## local training
1. `cd local_test`
2. `chmod +x *.sh`
3. ` ./train_local.sh scikit-<your-name>`
   	![](images/03-cloud9.png)
4. `ls test_dir/model/` to check the model output.

### error debug
1. `mv test_dir/input/config/hyperparameters.json test_dir/input/config/hyperparameters.json.bak`
2. `./train_local.sh  sckit-<your-name>` You will see error in the console
3. `cat test_dir/output/failure` to see failure
   ![](images/04-cloud9.png)
4. `mv test_dir/input/config/hyperparameters.json.bak test_dir/input/config/hyperparameters.json`
5. `./train_local.sh  scikit-<your-name>`

## Local Server Inference
1. `./serve_local.sh <image-name> > output.log`
    ![](images/05-cloud9.png)
2. Open new shell terminal in cloud9
3. `cd amazon-sagemaker-examples/advanced_functionality/scikit_bring_your_own/container/local_test/`
4. ` ./predict.sh payload.csv text/csv`
    ![](images/06-cloud9.png)

## Train and deploy using the Amazon SageMaker console

### Upload full data set to s3

* download [Iris data set](https://raw.githubusercontent.com/awslabs/amazon-sagemaker-examples/master/advanced_functionality/scikit_bring_your_own/data/iris.csv) to your computer. Then upload the data set into your s3 bucket. s3 bucket name as `sagemaker-iris-dataset-<your-id>/data/training/`
	![](images/01-s3.png)


### Create Training Job
* Job name: `scikit-<your-name>-yyyymmdd`
* Algorithm: `Custom`
* Input mode: `File`
* Training image: `<Amazon ECR path>:<tag>`. Can get it from `docker images`
	![](images/07-cloud9.png)
* Hyperparameters: `max_leaf_nodes` value: `8`
* Training
	* channel name: `training`
	* s3 location: `sagemaker-iris-dataset-<your-id>/data/training/`
	![](images/08-SageMaker.png)
* Output data configuration: s3 output path: `s3://sagemaker-iris-dataset-<your-id>/models/`
	![](images/09-SageMaker.png)
* create training job.
* After training job complete, you will see model in `s3://<bucket name>/models/<job name>/output/model.tar.gz` You can get it from trainig jobs detail page.
	![](images/10-SageMaker.png)

### Deploy an endpoint
#### Create model 
* model name: `scikit-<your-name>-yyyymmdd`
	![](images/11-SageMaker.png)
* Primary container: 
	* `<your container path>:<tag>`
	* model artifacts: s3 path with output file `s3://<bucket name>/models/<job name>/output/model.tar.gz`
	![](images/12-SageMaker.png)
* click create the model

#### Create endpoint configuration
* name: `scikit-<your-name>-yyyymmdd`
* add model: `scikit-<your-name>-yyyymmdd`
	![](images/13-SageMaker.png)

#### Create an endpoint
* name: `scikit-<your-name>-yyyymmdd`
* select endpoint configuration `scikit-<your-name>-yyyymmdd`
	![](images/14-SageMaker.png)
* create endpoint

### Test the endpoint
In cloud9, install pip3:

* `sudo easy_install-3.6 pip`
* `sudo /usr/local/bin/pip3 install boto3 pandas`

Download the `test-endpoint-sample.py` in the same github folder.

* modify the bucket name and endpoint
* run `python3 test-endpoint-sample.py`
	![](images/15-SageMaker.png)

### Clean Up
* SageMaker Endpoint
* s3
* cloud9

### Reference
* [AWS Blog](https://aws.amazon.com/blogs/machine-learning/train-and-host-scikit-learn-models-in-amazon-sagemaker-by-building-a-scikit-docker-container/)