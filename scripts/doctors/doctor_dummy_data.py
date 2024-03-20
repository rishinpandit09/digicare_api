import os

import boto3

# Configure AWS credentials and region
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_DEFAULT_REGION')

# Configure Boto3 client for DynamoDB
dynamodb = boto3.resource("dynamodb",
                          region_name=aws_region,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)

table = dynamodb.Table('doctors')

doctor_data = {
    "user_name": "john_smith",
    "name": "Dr. John Smith",
    "contact_number": "+1(555)-123-4567",
    "email": "john.smith@example.com",
    "role": "doctor",
    "DOB": "1980-10-20",
    "gender": "Male",
    "address": "789 Maple Avenue, Townsville, USA",
    "start_year_of_practice": "2005",
    "availability_hours": ["Tuesday: 8:00 AM - 4:00 PM", "Thursday: 9:00 AM - 6:00 PM"],
    "specialization": ["Orthopedics", "Sports Medicine"],
    "study_history": ["MD from University of Health Sciences", "Residency at Townsville General Hospital"],
    "patients": ["patient6", "patient7", "patient8"],
    "Hospital": "Townsville General Hospital",
    "password": "password"
}


table.put_item(Item=doctor_data)

print("Data inserted successfully!")
