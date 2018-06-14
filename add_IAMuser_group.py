import boto3

iam = boto3.client('iam')

#Enter Name of User and Group
username = input('Enter UserName: ')
groupname = input('Enter GroupName: ')

# Add user to group
response = iam.add_user_to_group(
    GroupName=groupname,
    UserName=username
)

# If response is 200, print Username added to group
if (response['ResponseMetadata']['HTTPStatusCode']) == 200:
    print("UserName " + username + " added to group " + groupname)

# Print error
else:
    print("Not Added")
