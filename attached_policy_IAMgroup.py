import boto3

iam = boto3.client('iam')

groupname = input('Enter GroupName: ')
policyARN = input('Enter Policy ARN: ')

arn = (policyARN.split('/'))

response = iam.attach_group_policy(
    GroupName=groupname,
    PolicyArn=policyARN
)

if (response['ResponseMetadata']['HTTPStatusCode']) == 200:
    print("Policy " + arn[1] + " attached to group " + groupname)

else:
    print("Not Attached")
