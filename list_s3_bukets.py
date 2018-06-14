import boto3

s3client = boto3.client('s3')

#List S3 buckets
response = s3client.list_buckets()
for bucket in response["Buckets"]:
    print(bucket['Name'])