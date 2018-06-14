import boto3

iam = boto3.client('iam')

#Enter name of group and ARN of policy to attach 
groupname = input('Enter GroupName: ')
policyARN = input('Enter Policy ARN: ')

#Split / from Policy ARN
arn = (policyARN.split('/'))

#Attach Policy to Group
response = iam.attach_group_policy(
    GroupName=groupname,
    PolicyArn=policyARN
)

# if Response is 200, Print attaced policy to group
if (response['ResponseMetadata']['HTTPStatusCode']) == 200:
    print("Policy " + arn[1] + " attached to group " + groupname)

# Else print error
else:
    print("Not Attached")
