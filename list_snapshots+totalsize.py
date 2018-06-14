import boto3

ec2 = boto3.client('ec2')

#Filter snapshots of Dev Env 
response = ec2.describe_snapshots(Filters=[{'Name': 'tag:ENV','Values': ['DEV']}])

total = 0

for snap in response['Snapshots']:
    size = snap['VolumeSize']
	
	#Print Snapshot ID of volume with size
    print ("Snapshot ID for Volume " + snap['VolumeId'] + " is " + snap['SnapshotId'] + " of Size " + str(size))

    total = total + size

print("===================================================================================")

#Print total size of all snapshots
print("Total size: " + str(total) + " GB")
