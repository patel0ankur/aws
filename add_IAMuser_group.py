import boto3

iam = boto3.client('iam')

username = input('Enter UserName: ')
groupname = input('Enter GroupName: ')

response = iam.add_user_to_group(
    GroupName=groupname,
    UserName=username
)

if (response['ResponseMetadata']['HTTPStatusCode']) == 200:
    print("UserName " + username + " added to group " + groupname)

else:
    print("Not Added")
