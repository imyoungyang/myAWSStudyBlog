### Fraud detection on SageMaker
I will use dataset from Kaggle that is used for Credit Card Fraud detection.
In this example, there are two notebooks:

* linear learner: it will use AWS SageMaker linear learner algorithm to get a base line model. The key is to use linear learning weight function and objective function to help us quickly to achieve the gaol. [ref](https://docs.aws.amazon.com/sagemaker/latest/dg/ll_hyperparameters.html)

* xgboost: it will use SageMaker build in xgboost algorithm and HPO to get the model. xgboost notebook is credited to [wmlba](https://github.com/wmlba/Fraud_Detection_Techniques).

