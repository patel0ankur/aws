import boto3

ec2 = boto3.client('ec2')

print("\n =================================  \n")

#Filter instaces using Tag Dev env
response = ec2.describe_instances(Filters=[{'Name': 'tag:ENV', 'Values': ['DEV']}])
for reservation in response['Reservations']:
    for instances in reservation['Instances']:
        print("Instance IP address: " + instances['PrivateIpAddress'])
        print("Instance Type: " + instances['InstanceType'])
        print("Instance State: " + instances['State']['Name'])
        print("\n ================================ \n")