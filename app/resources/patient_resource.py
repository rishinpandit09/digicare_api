from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import abort

from app.models.patient import Patient


class PatientResource(Resource):

    # @jwt_required()
    def get(self, patient_id=None):
        if patient_id:
            # Retrieve patient by ID
            try:
                patient = Patient.get_patient_by_username(patient_id)
                if patient:
                    return {'data': patient}
                else:
                    abort(404, message="Patient not found")
            except Exception as e:
                return {'message': f'Error retrieving patient: {str(e)}'}, 500
        else:
            # Retrieve all patients
            try:
                patients = Patient.get_all_patients()
                return {'data': patients}
            except Exception as e:
                return {'message': f'Error retrieving patients: {str(e)}'}, 500

    # @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()

        try:
            new_patient = Patient()
            new_patient.create_patient(**args)
            return {'message': 'Patient created successfully',
                    'data': new_patient.get_patient_by_username(args['username'])}
        except Exception as e:
            return {'message': f'Error creating patient: {str(e)}'}, 500

    # @jwt_required()
    def put(self, patient_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()

        try:
            patient = Patient.get_patient_by_username(patient_id)
            if patient:
                patient.update_patient(**args)
                return {'message': 'Patient updated successfully', 'data': patient}
            else:
                abort(404, message="Patient not found")
        except Exception as e:
            return {'message': f'Error updating patient: {str(e)}'}, 500

    # @jwt_required()
    def delete(self, patient_id):
        try:
            patient = Patient.get_patient_by_username(patient_id)
            if patient:
                patient.delete_patient()
                return {'message': 'Patient deleted successfully'}
            else:
                abort(404, message="Patient not found")
        except Exception as e:
            return {'message': f'Error deleting patient: {str(e)}'}, 500
