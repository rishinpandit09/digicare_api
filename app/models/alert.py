from flask_mongoengine import Document
from mongoengine import fields

class Alert(Document):
    patient = fields.ReferenceField('Patient', required=True)
    doctor = fields.ReferenceField('Doctor', required=True)
    timestamp = fields.DateTimeField()
    severity = fields.StringField()
    description = fields.StringField()
