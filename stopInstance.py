import boto3
ids = ['i-03248fa11bac2f0c2']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).stop() 
