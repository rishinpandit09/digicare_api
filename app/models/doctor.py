from flask_mongoengine import Document
from mongoengine import fields

class Doctor(Document):
    name = fields.StringField(required=True)
    specialization = fields.StringField()
    contact_info = fields.DictField()
    patients = fields.ListField(fields.ReferenceField('Patient'))
    emergency_alerts = fields.ListField(fields.ReferenceField('Alert'))
