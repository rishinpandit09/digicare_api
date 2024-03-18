from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import abort

from app.models.doctor import Doctor

class DoctorResource(Resource):
    # @jwt_required()
    def get(self, doctor_id):
        try:
            doctor = Doctor.get_doctor_by_id(doctor_id)
            return {'data': doctor}
        except ValueError as e:
            abort(400, message=str(e))
        except Exception as e:
            abort(500, message=str(e))

    # @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('specialization', type=str, required=True)
        parser.add_argument('contact_info', type=dict, required=True)
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        try:
            new_doctor = Doctor()
            response = new_doctor.create_doctor(**args)
            return {'message': 'Doctor created successfully', 'data': response}
        except Exception as e:
            abort(500, message=str(e))

    # @jwt_required()
    def put(self, doctor_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('specialization', type=str, required=True)
        parser.add_argument('contact_info', type=dict, required=True)
        args = parser.parse_args()

        try:
            doctor = Doctor.get_doctor_by_username(doctor_id)
            if doctor:
                response = doctor.update_doctor(**args)
                return {'message': 'Doctor updated successfully', 'data': response}
            else:
                abort(404, message="Doctor not found")
        except Exception as e:
            abort(500, message=str(e))

    # @jwt_required()
    def delete(self, doctor_id):
        try:
            doctor = Doctor.get_doctor_by_username(doctor_id)
            if doctor:
                response = doctor.delete_doctor()
                return {'message': 'Doctor deleted successfully', 'data': response}
            else:
                abort(404, message="Doctor not found")
        except Exception as e:
            abort(500, message=str(e))

