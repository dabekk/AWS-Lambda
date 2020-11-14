import boto3
# get all instance IDs
ec2 = boto3.resource('ec2')
ec2_list = []
for instance in ec2.instances.all():
    ec2_list.append(instance.id)

boto = boto3.client('ec2')

def lambda_handler(event, context):
    boto.stop_instances(InstanceIds=ec2_list) # stop all instances by instance ID
    print('stopped your instances: ' + str(ec2_list))
