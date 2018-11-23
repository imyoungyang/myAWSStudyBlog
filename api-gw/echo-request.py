from __future__ import print_function

import json

print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    #print("Request ID:", context.aws_request_id)
    print("userArn:", event['requestContext']['identity']['userArn'])
    userArn = event['requestContext']['identity']['userArn']
    userName = userArn.split(":")[-1] if (userArn != None and ":" in userArn) else ''
    print("userName:", userName)
    event['userName'] = userName
    return {
        'statusCode': '200',
        'body': json.dumps(event, indent=2),
        'headers': {
            'Content-Type': 'application/json',
        }
    }

