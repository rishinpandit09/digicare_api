from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import abort

from app.models.doctor import Doctor

class DoctorResource(Resource):
    @jwt_required()
    def get(self, doctor_id):
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            return {'data': doctor.to_json()}
        except Doctor.DoesNotExist:
            abort(404, message="Doctor not found")

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()

        try:
            new_doctor = Doctor(**args)
            new_doctor.save()
            return {'message': 'Doctor created successfully', 'data': new_doctor.to_json()}
        except Exception as e:
            return {'message': f'Error creating doctor: {str(e)}'}, 500

    @jwt_required()
    def put(self, doctor_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        args = parser.parse_args()

        try:
            doctor = Doctor.objects.get(id=doctor_id)
            doctor.update(**args)
            return {'message': 'Doctor updated successfully', 'data': doctor.to_json()}
        except Doctor.DoesNotExist:
            abort(404, message="Doctor not found")
        except Exception as e:
            return {'message': f'Error updating doctor: {str(e)}'}, 500

    @jwt_required()
    def delete(self, doctor_id):
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            doctor.delete()
            return {'message': 'Doctor deleted successfully'}
        except Doctor.DoesNotExist:
            abort(404, message="Doctor not found")
        except Exception as e:
            return {'message': f'Error deleting doctor: {str(e)}'}, 500
