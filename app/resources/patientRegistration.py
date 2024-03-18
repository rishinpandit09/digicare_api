from flask_restful import Resource, reqparse
from app.models.patient import Patient


class PatientRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('dob', type=str, required=True)
        parser.add_argument('gender', type=str, choices=['Male', 'Female', 'Other'], required=True)
        parser.add_argument('contact_info', type=dict, required=True)
        parser.add_argument('medical_history', type=list, required=True)
        parser.add_argument('doctors', type=list, required=True)
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        try:
            new_patient = Patient()
            response = new_patient.create_patient(**args)
            return {'message': 'Patient created successfully', 'data': response}, 201
        except Exception as e:
            return {'message': f'Error creating patient: {str(e)}'}, 500



