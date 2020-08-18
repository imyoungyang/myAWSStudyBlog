# AWS Step Functions Data Science SDK Workshop

## Why?

### Reduce the step function complexity
1. Before, we need to use a low-level AWS SDK to construct the request parameters, call the Lambda Amazon SageMaker Processing job APIs (create_processing_job(), describe_processing_job(), list_processing_jobs(), or stop_processing_job()), and read the response objects returned.
2. Add workflow steps:  Wait state, Choice state, and Task states to create a processing job and check the job status

## Workshop

1. launch a t2.medium notebook
2. in the terminal

```
bash
cd SageMaker
git clone https://github.com/awslabs/amazon-sagemaker-examples.git
cp -r amazon-sagemaker-examples/step-functions-data-science-sdk/ .
```

### Get Starting
1. `hello_world_work` notebook
2. `training_pipeline_pytorch_mnist` 
	- using template.TrainingPipeline to simplify this procedure
		- training
		- create model
		- configure endpoint
		- deploy 
3. `step_functions_mlworkflow_processing` (scikit-learn)
	- using Chain to define the ML pipeline
		- pre-processing job
		- training job
		- model evaluation job
4. `machine_learning_workflow_abalone` (xgboost, libsvm format)
	- using Chain to define the ML pipeline
		- train
		- save model
		- batch transform
		- endpoint configuration
		- endpoint
5. `automate_model_retraining_workflow`
	- customized the ml pipeline via "Chain"
		- glue-etl
		- training (xgboost)
		- create model
		- lambda - get the training matrix:accuracy
		- check accuracy - choice state
		- Success or fail

# References
* [github: aws-step-functions-data-science-sdk-python](https://github.com/aws/aws-step-functions-data-science-sdk-python)
* [SDK documents](https://aws-step-functions-data-science-sdk.readthedocs.io/en/stable/readmelink.html)
* [101 example](https://docs.aws.amazon.com/step-functions/latest/dg/sample-preprocess-feature-transform.html)
* [AWS Blogs about step functions data science sdk](https://aws.amazon.com/blogs/machine-learning/building-machine-learning-workflows-with-amazon-sagemaker-processing-jobs-and-aws-step-functions/)
* [Amazon States Language](https://states-language.net/spec.html)