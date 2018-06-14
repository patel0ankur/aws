import boto3

ec2 = boto3.client("ec2")

nodes = open("instances.txt").read().replace("\n", "").split(',')

response = ec2.describe_volumes(Filters = [{'Name': 'attachment.instance-id','Values': nodes}])

for vol in response["Volumes"]:
    for attach in vol['Attachments']:
        vol = [(attach['VolumeId'])]

    for vol_id in vol:
        response = ec2.modify_volume(VolumeId=vol_id, Size=30)
        print(response)
