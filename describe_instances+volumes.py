import boto3

ec2 = boto3.client('ec2')

def insta():

#Filter instaces using Tag Dev env
    response = ec2.describe_instances(Filters=[{'Name': 'tag:ENV', 'Values': ['DEV']}])

    for reservation in response['Reservations']:
        for instances in reservation['Instances']:
            for Tag in instances['Tags']:
                if Tag['Key'] == 'Name':
                    name = Tag['Value']
					
					#Print Instances Details 
                    print ("---------------------------------------------")
                    print ("Instance Name: " + name)
                    print ("Instance IP address: " + instances['PrivateIpAddress'])
                    print ("Instance Type: " + instances['InstanceType'])
                    print ("Instance State: " + instances['State']['Name'])

            for volume in instances['BlockDeviceMappings']:
                status = (volume['Ebs']['Status'])
                vol = (volume['Ebs']['VolumeId'])
				
				#print Volumes details attached to instances
                print ("Volume Name: " + volume['DeviceName'] + " | " + "Status: " + status + " | " + "Volume Id: " + vol)

insta()
