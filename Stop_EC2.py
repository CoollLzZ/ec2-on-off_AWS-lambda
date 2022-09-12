import boto3

# AWS_REGION = "us-east-1"
# EC2_RESOURCE = boto3.resource('ec2'region_name=AWS_REGION)

# Todo: Filtering the resource ID's for specific Tag
EC2_RESOURCE = boto3.resource('ec2')
INSTANCE_NAME_TAG_VALUE = 'True'
INSTANCE_LIST = []


def lambda_handler(event, context):
    instances = EC2_RESOURCE.instances.filter(
        Filters=[
            {
                'Name': 'tag:Bootsequence',
                'Values': [
                    INSTANCE_NAME_TAG_VALUE
                ]
            }
        ]
    )

    # Todo: Making list of all instances together

    ec2_client = boto3.client("ec2")
    for instance in instances:
        INSTANCE_LIST.append(instance.id)

    # Todo: Stopping Instances by making sure if it is running
    for inst_id in INSTANCE_LIST:
        instance = EC2_RESOURCE.Instance(inst_id)
        state = instance.state
        if state['Name'] == 'running':
            ec2_client.stop_instances(InstanceIds=INSTANCE_LIST)
