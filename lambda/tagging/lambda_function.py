import boto3
import os

def lambda_handler(event, context):
    # Captura os recursos que precisam ser tagueados
    resource_ids = event.get('resource_ids', [])
    
    ec2 = boto3.client('ec2')
    
    # Aplica tags em cada recurso
    for resource_id in resource_ids:
        ec2.create_tags(
            Resources=[resource_id],
            Tags=[
                {'Key': 'Project', 'Value': 'Nome do Projeto'},
                {'Key': 'Owner', 'Value': 'Seu Nome'},
                {'Key': 'Environment', 'Value': 'Produção'}
            ]
        )
        
    return {
        'statusCode': 200,
        'body': 'Tags aplicadas com sucesso!'
    }
