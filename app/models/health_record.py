from flask_mongoengine import Document
from mongoengine import fields

class HealthRecord(Document):
    patient = fields.ReferenceField('Patient', required=True)
    doctor = fields.ReferenceField('Doctor', required=True)
    timestamp = fields.DateTimeField()
    parameters = fields.ListField(fields.DictField())
    notes = fields.StringField()