import os
import random
import uuid
from datetime import datetime

import boto3

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_DEFAULT_REGION')

# Configure Boto3 client for DynamoDB
dynamodb = boto3.resource("dynamodb",
                          region_name=aws_region,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)
# Define the table name and attribute definitions
table_name = 'realtime-recording'
# attribute_definitions = [
#     {
#         'AttributeName': 'Recording_id',
#         'AttributeType': 'S'
#     },
#     {
#         'AttributeName': 'patient_username',
#         'AttributeType': 'S'
#     },
#     {
#         'AttributeName': 'timeStamp',
#         'AttributeType': 'S'
#     }
# ]
#
# # Define the key schema
# key_schema = [
#     {
#         'AttributeName': 'Recording_id',
#         'KeyType': 'HASH'
#     },
#     {
#         'AttributeName': 'patient_username',
#         'KeyType': 'RANGE'
#     }
# ]
#
# # Define the provisioned throughput settings
# provisioned_throughput = {
#     'ReadCapacityUnits': 5,
#     'WriteCapacityUnits': 5
# }
#
# # Define the global secondary index for timeStamp attribute
# global_secondary_indexes = [
#     {
#         'IndexName': 'timeStampIndex',
#         'KeySchema': [
#             {
#                 'AttributeName': 'timeStamp',
#                 'KeyType': 'HASH'
#             }
#         ],
#         'Projection': {
#             'ProjectionType': 'ALL'
#         },
#         'ProvisionedThroughput': {
#             'ReadCapacityUnits': 5,
#             'WriteCapacityUnits': 5
#         }
#     }
# ]
# # Create the table
# response = dynamodb.create_table(
#     TableName=table_name,
#     AttributeDefinitions=attribute_definitions,
#     KeySchema=key_schema,
#     ProvisionedThroughput=provisioned_throughput,
#     GlobalSecondaryIndexes=global_secondary_indexes
# )

# # Dummy data for records
# dummy_data = {
#     'Recording_id': str(uuid.uuid4()),
#     'patient_username': '1p',
#     'timeStamp': str(datetime.now()),
#     'records': [
#         {
#             '_id': '1r',
#             'name': 'blood_pressure',
#             'reading': '130/80',
#             'unit': 'mmHg',
#             'min_value': '90/60',
#             'max_value': '120/80',
#         },
#         {
#             '_id': '2r',
#             'name': 'heart_rate',
#             'reading': str(random.randint(60, 185)),
#             'unit': 'bpm',
#             'min_value': '60',
#             'max_value': '100',
#         },
#         {
#             '_id': '3r',
#             'name': 'bmi',
#             'reading': str(random.uniform(18.5, 24.9)),
#             'unit': 'kg/msq',
#             'min_value': '18.5',
#             'max_value': '24.9',
#         },
#         {
#             '_id': '4r',
#             'name': 'weight',
#             'reading': str(random.randint(40, 200)),
#             'unit': 'Kg',
#             'min_value': '40',
#             'max_value': '100',
#         },
#         {
#             '_id': '5r',
#             'name': 'o2',
#             'reading': str(random.randint(90, 100)),
#             'unit': '%',
#             'min_value': '90',
#             'max_value': '100',
#         },
#         {
#             '_id': '6r',
#             'name': 'sugar_level',
#             'reading': str(random.randint(70, 125)),
#             'unit': 'mg/dL',
#             'min_value': '70',
#             'max_value': '125',
#         }
#     ]
# }
# table = dynamodb.Table(table_name)
# response = table.put_item(Item=dummy_data)
# # Insert dummy data into the table
# # response = dynamodb.put_item(
# #     TableName=table_name,
# #     Item={
# #         'Recording_id': {'S': str(uuid.uuid4())},
# #         'patient_username': {'S': dummy_data['patient_username']},
# #         'timeStamp': {'S': dummy_data['timeStamp']},
# #         'records': {'L': [
# #             {'M': {
# #                 '_id': {'S': record['_id']},
# #                 'name': {'S': record['name']},
# #                 'reading': {'S': record['reading']},
# #                 'unit': {'S': record['unit']},
# #                 'min_value': {'S': record['min_value']},
# #                 'max_value': {'S': record['max_value']}
# #             }} for record in dummy_data['records']
# #         ]}
# #     }
# # )
#
# # Print the response
# print(response)
# # Print the response
# print(response)