import boto3
import io
import pandas as pd
import itertools

# Set below parameters
bucket = '<s3 bucket name: sagemaker-iris-dataset>'
key = 'data/training/iris.csv'
endpointName = 'scikit-<your-id>-yyyymmdd'

# Pull our data from S3
s3 = boto3.client('s3')
f = s3.get_object(Bucket=bucket, Key=key)

# Make a dataframe
shape = pd.read_csv(io.BytesIO(f['Body'].read()), header=None)

# Take a random sample
a = [50*i for i in range(3)]
b = [40+i for i in range(10)]
indices = [i+j for i,j in itertools.product(a,b)]
test_data=shape.iloc[indices[:-1]]
test_X=test_data.iloc[:,1:]
test_y=test_data.iloc[:,0]

# Convert the dataframe to csv data
test_file = io.StringIO()
test_X.to_csv(test_file, header=None, index=None)

# Talk to SageMaker
client = boto3.client('sagemaker-runtime')
response = client.invoke_endpoint(
    EndpointName=endpointName,
    Body=test_file.getvalue(),
    ContentType='text/csv',
    Accept='Accept'
)

print(response['Body'].read().decode('ascii'))
