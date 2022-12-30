import boto3
ids = ['i-00d2588d7385b6b20']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).stop() 
