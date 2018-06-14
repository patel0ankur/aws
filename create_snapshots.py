import boto3
from botocore.exceptions import ClientError

ec2_client = boto3.client("ec2")

#Filter volumes using Tags Dev Env
try:
   volumes = ec2_client.describe_volumes(Filters=[{'Name': 'tag:ENV','Values': ['DEV']}])

   for vol in volumes.get('Volumes'):
       volume_id = vol.get('VolumeId')

       try:

           # Create Snapshots of Volumes and put description
           snapshot = ec2_client.create_snapshot(VolumeId=volume_id, Description="Automatic Backup")
           #print("Snapshot ID " + snapshot['SnapshotId'])

#Error handling if snapshots fails
       except ClientError as err:
           print("Error in snapshot" + err)
           
#Error handling if Describe volumes fails
except ClientError as err:
   print("Error in volume describe" + err)
