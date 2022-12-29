import boto3
ids = ['i-05032a4800d112798']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).stop() 
