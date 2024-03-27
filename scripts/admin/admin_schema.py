import os

import boto3

from app.utils.auth import password_hash

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
table_name = 'Admin'

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

try:
    # Put dummy data into the table
    table = dynamodb.Table('Admin')
    hashed_password = password_hash("admin123")
    response = table.put_item(
        Item={
            'user_name': 'admin',
            'password': hashed_password
            # Add more attributes as needed
        }
    )

    print("Dummy data added successfully!")

except Exception as e:
    print(f"Error adding dummy data: {e}")