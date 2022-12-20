import boto3
ids = ['i-0bec2a0bf000bb71c']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).stop() 
