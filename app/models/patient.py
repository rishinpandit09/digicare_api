import os

import boto3
from boto3.dynamodb.types import TypeDeserializer
from app.utils.auth import password_hash

aws_region = os.getenv('AWS_DEFAULT_REGION')

dynamodb = boto3.resource('dynamodb',region_name=aws_region)
global_table = dynamodb.Table('patients')


class Patient:
    def __init__(self):
        self.table = global_table
        self.deserializer = TypeDeserializer()

    def create_patient(self, name, dob, gender, contact_info, medical_history, doctors, username, password):
        hashed_password = password_hash(password)
        item = {
            "name": name,
            "dob": str(dob),
            "gender": gender,
            "contact_info": contact_info,
            "medical_history": medical_history,
            "doctors": doctors,
            "username": username,
            "password": hashed_password
        }
        response = global_table.put_item(Item=item)
        return response

    @classmethod
    def get_patient_by_username(cls, username):
        response = global_table.query(
            KeyConditionExpression="username = :val",
            ExpressionAttributeValues={
                ":val": username
            }
        )
        items = response.get('Items', [])
        if items:
            return cls().deserialize(items[0])
        return None

    @classmethod
    def deserialize(cls, item):
        if isinstance(item, dict):
            return {key: cls.deserialize(value) for key, value in item.items()}
        elif isinstance(item, list):
            return [cls.deserialize(value) for value in item]
        else:
            return item

    @classmethod
    def get_all_patients(cls):
        response = global_table.scan()
        items = response.get('Items', [])
        return [cls().deserialize(item) for item in items]
