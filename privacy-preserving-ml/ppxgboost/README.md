# Privacy Preserving XGBoost

This Sample provide an example to run [PPXGBoost](https://github.com/awslabs/privacy-preserving-xgboost-inference.git) directly in SageMaker without any manual data preparation.

Note that PPXGBoost is using [OPE (Order Preserving Encryption)](https://github.com/tonyo/pyope) which is a subset of [FHE (Fully Homomorphic Encryption)](https://en.wikipedia.org/wiki/Homomorphic_encryption).

## Examples

1. Multi-class example with confined value range
2. Binary-class example with the value range retrived from the testing data

## XGBoost

One of the most popular and effective ML libraries. The algorithm uses gradient residue to combine decision trees.

## Order Preserving Encryption (OPE)

Literally, OPE make sure the order of numerical values will stay the same after encryption. Since XGBoost use decision trees as it core classifier, OPE will keep all the necessary information the algorithm require to perform the prediction.

## XGBoost + OPE

After combining XGBoost and OPE, there are 2 ways that we can assemble these 2 algorithms.

#### 1. Apply OPE to all data and then train the XGBoost model

In this case, we just use the [OPE (Order Preserving Encryption)](https://github.com/tonyo/pyope) library first, and do XGBoost after as the normal dataset.

However, this is hard for data exploration since we will want to know the value that we are working on when we first train the model.

#### 2. Train the XGBoost model with training data and apply OPE to the model and testing data

In this case, we train the XGBoost model first while exploring the solution. Extract the tree parameters from the model, apply OPE to the model. Encrypt the testing data and use the encrypted model to get the predicted result.

This provides the flexibility for the model to handle the encrypted and decrypted data.
