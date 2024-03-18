import boto3
from boto3.dynamodb.types import TypeDeserializer
from app.utils.auth import password_hash

dynamodb = boto3.resource('dynamodb')
global_table = dynamodb.Table('doctors')


class Doctor:
    def __init__(self):
        self.table = global_table
        self.deserializer = TypeDeserializer()

    def create_doctor(self, name, specialization, contact_info, patients, username, password):
        hashed_password = password_hash(password)
        item = {
            "name": name,
            "specialization": specialization,
            "contact_info": contact_info,
            "username": username,
            "password": hashed_password,
            "patients": patients,
        }
        response = self.table.put_item(Item=item)
        return response

    @classmethod
    def get_doctor_by_username(cls, username):
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
