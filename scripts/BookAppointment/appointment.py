import os

import boto3

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_DEFAULT_REGION')

# Configure Boto3 client for DynamoDB
dynamodb = boto3.client("dynamodb",
                          region_name="us-east-1",
                          aws_access_key_id="AKIAQ3EGQAJIBP3ZY2IM",
                          aws_secret_access_key="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")
table_name = 'appointment'

# Create table
try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'  # String
            },
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