import json
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    rds = boto3.client('rds')
    
    # Tagueamento de Instância EC2
    ec2.create_tags(Resources=[event['ec2_instance_id']], Tags=[
        {'Key': 'Project', 'Value': 'TaggingDemo'},
        {'Key': 'CostCenter', 'Value': '10000'}
    ])
    
    # Tagueamento de Instância RDS
    rds.add_tags_to_resource(
        ResourceName=event['rds_instance_arn'],
        Tags=[
            {'Key': 'Project', 'Value': 'TaggingDemo'},
            {'Key': 'CostCenter', 'Value': '10000'}
        ]
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Tags aplicadas com sucesso!')
    }
