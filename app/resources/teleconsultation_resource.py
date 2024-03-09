from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import abort

from app.models.teleconsultation import Teleconsultation

class TeleconsultationResource(Resource):
    @jwt_required()
    def get(self, teleconsultation_id):
        try:
            teleconsultation = Teleconsultation.objects.get(id=teleconsultation_id)
            return {'data': teleconsultation.to_json()}
        except Teleconsultation.DoesNotExist:
            abort(404, message="Teleconsultation not found")

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('patient_id', type=str, required=True)
        parser.add_argument('doctor_id', type=str, required=True)
        parser.add_argument('platform', type=str, choices=['Teams', 'Zoom', 'Google Meet'])
        parser.add_argument('scheduled_time', type=str, required=True)
        args = parser.parse_args()

        try:
            new_teleconsultation = Teleconsultation(**args)
            new_teleconsultation.save()
            return {'message': 'Teleconsultation created successfully', 'data': new_teleconsultation.to_json()}
        except Exception as e:
            return {'message': f'Error creating teleconsultation: {str(e)}'}, 500

    @jwt_required()
    def put(self, teleconsultation_id):
        parser = reqparse.RequestParser()
        parser.add_argument('patient_id', type=str, required=True)
        parser.add_argument('doctor_id', type=str, required=True)
        parser.add_argument('platform', type=str, choices=['Teams', 'Zoom', 'Google Meet'])
        parser.add_argument('scheduled_time', type=str, required=True)
        args = parser.parse_args()

        try:
            teleconsultation = Teleconsultation.objects.get(id=teleconsultation_id)
            teleconsultation.update(**args)
            return {'message': 'Teleconsultation updated successfully', 'data': teleconsultation.to_json()}
        except Teleconsultation.DoesNotExist:
            abort(404, message="Teleconsultation not found")
        except Exception as e:
            return {'message': f'Error updating teleconsultation: {str(e)}'}, 500

    @jwt_required()
    def delete(self, teleconsultation_id):
        try:
            teleconsultation = Teleconsultation.objects.get(id=teleconsultation_id)
            teleconsultation.delete()
            return {'message': 'Teleconsultation deleted successfully'}
        except Teleconsultation.DoesNotExist:
            abort(404, message="Teleconsultation not found")
        except Exception as e:
            return {'message': f'Error deleting teleconsultation: {str(e)}'}, 500
