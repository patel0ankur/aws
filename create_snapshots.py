import boto3
from botocore.exceptions import ClientError

ec2_client = boto3.client("ec2")

try:
   ec2_volumes = ec2_client.describe_volumes(Filters = [
           {
               'Name': "tag-key",
               'Values': ["xxxxx"]
           },
           {
               'Name': "tag-value",
               'Values': ['xxxxx']
           }
       ])

   for volume in ec2_volumes.get('Volumes'):
       volume_id = volume.get('VolumeId')

       try:
           snapshot = ec2_client.create_snapshot(VolumeId=volume_id, Description="Automatic Backup")
           #print("Snapshot ID " + snapshot['SnapshotId'])

       except ClientError as err:
           print("Error in snapshot" + err)

except ClientError as err:
   print("Error in volume describe" + err)
