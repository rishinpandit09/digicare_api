import os

import boto3

# Initialize Boto3 DynamoDB resource
# Configure AWS credentials and region
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_DEFAULT_REGION')

# Configure Boto3 client for DynamoDB
dynamodb = boto3.resource("dynamodb",
                          region_name=aws_region,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)

# Define table configurations for each model
table_configurations = [
    {
        'TableName': 'alerts',
        'KeySchema': [{'AttributeName': 'alert_id', 'KeyType': 'HASH'}],
        'AttributeDefinitions': [{'AttributeName': 'alert_id', 'AttributeType': 'S'}],
        'BillingMode': 'PAY_PER_REQUEST'
    },
    {
        'TableName': 'doctors',
        'KeySchema': [{'AttributeName': 'username', 'KeyType': 'HASH'}],
        'AttributeDefinitions': [{'AttributeName': 'username', 'AttributeType': 'S'}],
        'BillingMode': 'PAY_PER_REQUEST'
    },
    {
        'TableName': 'health_records',
        'KeySchema': [{'AttributeName': 'record_id', 'KeyType': 'HASH'}],
        'AttributeDefinitions': [{'AttributeName': 'record_id', 'AttributeType': 'S'}],
        'BillingMode': 'PAY_PER_REQUEST'
    },
    {
        'TableName': 'patients',
        'KeySchema': [{'AttributeName': 'username', 'KeyType': 'HASH'}],
        'AttributeDefinitions': [{'AttributeName': 'username', 'AttributeType': 'S'}],
        'BillingMode': 'PAY_PER_REQUEST'
    },
    {
        'TableName': 'teleconsultation',
        'KeySchema': [{'AttributeName': 'record_id', 'KeyType': 'HASH'}],
        'AttributeDefinitions': [{'AttributeName': 'record_id', 'AttributeType': 'S'}],
        'BillingMode': 'PAY_PER_REQUEST'
    }
]

# Create tables
for table_config in table_configurations:
    try:
        table = dynamodb.create_table(**table_config)
        print(f"Table '{table.table_name}' created successfully.")
    except Exception as e:
        print(f"Failed to create table '{table_config['TableName']}': {e}")
