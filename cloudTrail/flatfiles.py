from __future__ import print_function
import json
import urllib
import boto3
import gzip

s3 = boto3.resource('s3')
client = boto3.client('s3')

def convertColumntoLowwerCaps(obj):
    for key in obj.keys():
        new_key = key.lower()
        if new_key != key:
            obj[new_key] = obj[key]
            del obj[key]
    return obj


def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    print(bucket)
    print(key)
    try:
        newKey = 'flatfiles/' + key.replace("/", "")
        client.download_file(bucket, key, '/tmp/file.json.gz')
        with gzip.open('/tmp/out.json.gz', 'w') as output, gzip.open('/tmp/file.json.gz', 'rb') as file:
            i = 0
            for line in file:
                for record in json.loads(line,object_hook=convertColumntoLowwerCaps)['records']:
            		if i != 0:
            		    output.write("\n")
            		output.write(json.dumps(record))
            		i += 1
        client.upload_file('/tmp/out.json.gz', bucket,newKey)
        return "success"
    except Exception as e:
        print(e)
        print('Error processing object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
