import decimal, uuid
import os
import boto3
from boto3.dynamodb.types import TypeDeserializer
from app.models.patient import Patient

aws_region = os.getenv('AWS_DEFAULT_REGION')

dynamodb = boto3.resource('dynamodb', region_name=aws_region)
global_table = dynamodb.Table('appointment')


class Appointment:
    def __init__(self):
        self.table = global_table
        self.deserializer = TypeDeserializer()

    @classmethod
    def create_appointment(cls, patient_username,date,doctor_username, day, time, description):

        patient_record = Patient.get_patient_by_username(patient_username)
        if not patient_record:
         return {'message': 'Patient not found'}

        # Extract room_id from patient record
       # room_id = patient_record.get('room_id')
        appointment_instance = cls()
        appointment_instance.bookTimeSlot(doctor_username,time,day)

        item = {
            "id": str(uuid.uuid4()),
            "patient_username": patient_username,
            "doctor_username": doctor_username,
            "date": date,
            "day": day,
            "time": time,
            "description": description,
            "room_id": "123"
        }
        response = global_table.put_item(Item=item)
        return response

    @classmethod
    def get_appointments_by_patient_username(cls, patient_username):
        response = global_table.scan(
            FilterExpression='patient_username = :val',
            ExpressionAttributeValues={
                ':val': patient_username
            }
        )
        items = response.get('Items', [])
        appointments = [cls.deserialize(item) for item in items]
        return appointments

    @classmethod
    def get_appointments_by_doctor_username(cls, doctor_username):
        response = global_table.scan(
            FilterExpression='doctor_username = :val',
            ExpressionAttributeValues={
                ':val': doctor_username
            }
        )
        items = response.get('Items', [])
        appointments = [cls.deserialize(item) for item in items]
        return appointments

    @classmethod
    def deserialize(cls, item):
        if isinstance(item, dict):
            return {key: cls.deserialize(value) for key, value in item.items()}
        elif isinstance(item, list):
            return [cls.deserialize(value) for value in item]
        elif isinstance(item, decimal.Decimal):
            return float(item)  # Convert Decimal to float
        else:
            return item

    def bookTimeSlot(self, doctor_username, start_time, day):
        # Query the table to find the item with matching attributes
        response = global_table.scan(
            FilterExpression='#d = :day AND doctor_username = :doctor_username AND start_time = :start_time',
            ExpressionAttributeNames={'#d': 'day'},  # Use ExpressionAttributeNames to handle reserved keyword
            ExpressionAttributeValues={
                ':doctor_username': doctor_username,
                ':start_time': start_time,
                ':day': day
            }
        )
        items = response.get('Items', [])

        if not items:
            return {'message': 'Appointment not found'}

        # Assuming there's only one matching item, retrieve its primary key
        appointment_id = items[0]['id']

        # Update the item using its primary key
        response = global_table.update_item(
            Key={
                'id': appointment_id
            },
            UpdateExpression='SET is_booked = :val',
            ExpressionAttributeValues={
                ':val': True
            },
            ReturnValues='UPDATED_NEW'
        )
        return response
