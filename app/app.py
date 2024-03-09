from flask import Flask
from flask_restful import Api

from .utils.config import app
from .resources.patient_resource import PatientResource
from .resources.doctor_resource import DoctorResource
from .resources.alert_resource import AlertResource
from .resources.teleconsultation_resource import TeleconsultationResource
from .resources.health_record_resource import HealthRecordResource

api = Api(app)

# Add API routes
api.add_resource(PatientResource, '/patients')
api.add_resource(DoctorResource, '/doctors')
api.add_resource(AlertResource, '/alerts')
api.add_resource(TeleconsultationResource, '/teleconsultations')
api.add_resource(HealthRecordResource, '/health_records')

if __name__ == '__main__':
    app.run(debug=True)
