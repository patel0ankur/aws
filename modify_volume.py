import boto3

ec2 = boto3.client("ec2")

#Read Instances ID from inst.txt file
nodes = open("instances.txt").read().replace("\n", "").split(',')

#List volumes of attached instace id
response = ec2.describe_volumes(Filters = [{'Name': 'attachment.instance-id','Values': nodes}])

#Print Volume Id of Intances 
for vol in response["Volumes"]:
    for attach in vol['Attachments']:
        vol = [(attach['VolumeId'])]
		#print(vol)

#Increase volume size of Volumes
    for vol_id in vol:
        response = ec2.modify_volume(VolumeId=vol_id, Size=30)
        print(response)
