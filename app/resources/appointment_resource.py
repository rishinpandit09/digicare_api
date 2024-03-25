from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import abort

from app.models.appointment import Appointment


class AppointmentResource(Resource):

    def post(self, username):

        parser = reqparse.RequestParser()
        parser.add_argument('date', type=str, required=True)
        parser.add_argument('doctor_username', type=str, required=True)
        parser.add_argument('day', type=str, required=True)
        parser.add_argument('time', type=str, required=True)
        parser.add_argument('description', type=str, required=True)

        args = parser.parse_args()

        try:
            new_appointment = Appointment()
            new_appointment.create_appointment(username,**args)
            return {'message': 'Appointment created successfully'}
                  #  'data': new_appointment.get_patient_by_username(args['username'])}
        except Exception as e:
            return {'message': f'Error creating patient: {str(e)}'}, 500

    def get(self, username):
        try:
            appointments = Appointment.get_appointments_by_patient_username(username)
            if appointments:
                return appointments
            else:
                abort(404, "Appointments not found for this patient")
        except Exception as e:
            abort(500, "Internal Server Error")

