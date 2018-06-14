import boto3

# Create IAM client
iam = boto3.client('iam')

#Enter username 
username = input('Enter UserName: ')

#Create Username
response = iam.create_user(
    UserName=username
)

#Print Created UserName
print("User " + response['User']['UserName'] + " created")

