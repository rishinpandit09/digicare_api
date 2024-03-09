from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import abort

from app.models.patient import Patient

class PatientResource(Resource):
    @jwt_required()
    def get(self, patient_id):
        try:
            patient = Patient.objects.get(id=patient_id)
            return {'data': patient.to_json()}
        except Patient.DoesNotExist:
            abort(404, message="Patient not found")

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()

        try:
            new_patient = Patient(**args)
            new_patient.save()
            return {'message': 'Patient created successfully', 'data': new_patient.to_json()}
        except Exception as e:
            return {'message': f'Error creating patient: {str(e)}'}, 500

    @jwt_required()
    def put(self, patient_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()

        try:
            patient = Patient.objects.get(id=patient_id)
            patient.update(**args)
            return {'message': 'Patient updated successfully', 'data': patient.to_json()}
        except Patient.DoesNotExist:
            abort(404, message="Patient not found")
        except Exception as e:
            return {'message': f'Error updating patient: {str(e)}'}, 500

    @jwt_required()
    def delete(self, patient_id):
        try:
            patient = Patient.objects.get(id=patient_id)
            patient.delete()
            return {'message': 'Patient deleted successfully'}
        except Patient.DoesNotExist:
            abort(404, message="Patient not found")
        except Exception as e:
            return {'message': f'Error deleting patient: {str(e)}'}, 500
