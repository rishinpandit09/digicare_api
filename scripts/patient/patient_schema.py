import os

import boto3

# Initialize DynamoDB client

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_DEFAULT_REGION')

# Configure Boto3 client for DynamoDB
dynamodb = boto3.resource("dynamodb",
                          region_name=aws_region,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)

# Define table name
table_name = 'Patients'

# Create table
try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'user_name',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user_name',
                'AttributeType': 'S'  # String
            },
            # Add more attribute definitions as needed
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists
    dynamodb.get_waiter('table_exists').wait(TableName=table_name)

    print("Table created successfully!")

except Exception as e:
    print(f"Error creating table: {e}")