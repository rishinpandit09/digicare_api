from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import abort

from app.models.appointment import Appointment


class AppointmentDoctorResource(Resource):

    def get(self, doctor_username):
        try:
            appointments = Appointment.get_appointments_by_doctor_username(doctor_username)
            return appointments
        except Exception as e:
            abort(500)