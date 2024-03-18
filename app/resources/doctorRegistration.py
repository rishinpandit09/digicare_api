from flask_restful import Resource, reqparse
from app.models.doctor import Doctor


class DoctorRegistration(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('specialization', type=str, required=True)
        parser.add_argument('contact_info', type=dict, required=True)
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('patients', type=list, required=True)
        args = parser.parse_args()

        try:
            new_doctor = Doctor()
            response = new_doctor.create_doctor(**args)
            return {'message': 'Doctor created successfully', 'data': response}, 201
        except Exception as e:
            return {'message': f'Error creating doctor: {str(e)}'}, 500
