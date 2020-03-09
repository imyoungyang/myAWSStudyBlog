import pickle
import xgboost as xgb
import json
import numpy as np

def lambda_handler(event, context):
    transaction = event['queryStringParameters']['transaction'].split(",")
    data = np.asarray(transaction).reshape((1,-1))
    test_matrix = xgb.DMatrix(data)
    filename = "./xgboost-model"
    xgb_loaded = pickle.load(open(filename, 'rb'))
    predictions = xgb_loaded.predict(test_matrix)
    print(predictions)
    response = response = {
        'statusCode': 200,
        'body': str(predictions[0])
    }
    return response
