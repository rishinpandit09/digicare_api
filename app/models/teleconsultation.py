from flask_mongoengine import Document
from mongoengine import fields

class Teleconsultation(Document):
    patient = fields.ReferenceField('Patient', required=True)
    doctor = fields.ReferenceField('Doctor', required=True)
    platform = fields.StringField(choices=['Teams', 'Zoom', 'Google Meet'])
    scheduled_time = fields.DateTimeField()
