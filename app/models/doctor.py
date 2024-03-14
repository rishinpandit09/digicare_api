from flask_mongoengine import Document
from mongoengine import fields

class Doctor(Document):
    name = fields.StringField(required=True)
    specialization = fields.StringField()
    contact_info = fields.DictField()
    username = fields.StringField(required=True, unique=True)
    password = fields.StringField(required=True)
    # Reference to patients
    patients = fields.ListField(fields.ReferenceField('Patient'))
    # Reference to emergency alerts
    emergency_alerts = fields.ListField(fields.ReferenceField('Alert'))