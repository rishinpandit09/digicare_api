from flask_mongoengine import Document
from mongoengine import fields


class Patient(Document):
    name = fields.StringField(required=True)
    dob = fields.DateTimeField()
    gender = fields.StringField(choices=['Male', 'Female', 'Other'])
    contact_info = fields.DictField()
    medical_history = fields.ListField(fields.DictField())
    doctors = fields.ListField(fields.ReferenceField('Doctor'))

    # Patient authentication fields
    username = fields.StringField(required=True, unique=True)
    password = fields.StringField(required=True)