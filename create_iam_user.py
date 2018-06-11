import boto3

# Create IAM client
iam = boto3.client('iam')

username = input('Enter UserName: ')

response = iam.create_user(
    UserName=username
)
print("User " + response['User']['UserName'] + " created")

