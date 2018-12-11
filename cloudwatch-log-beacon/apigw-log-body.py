import json

def lambda_handler(event, context):
    print(event['body'])
    return {
        'statusCode': 200
    }
