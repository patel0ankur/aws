import boto3

ec2 = boto3.client('ec2')

#Create Volume
vol = ec2.create_volume(AvailabilityZone='us-east-1a', Size=10, VolumeType='standard')
#print(vol)

#Tag the volume
ec2.create_tags(Resources=[vol['VolumeId']], Tags=[{'Key':'name', 'Value':'testvolume'}])

#List Created volume id
print("Created Vol Id: " + vol['VolumeId'])
