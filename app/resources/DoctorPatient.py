from flask_restful import Resource, reqparse
from flask import abort
from app.models.doctor import Doctor


class DoctorPatientResource(Resource):
    # @jwt_required()
    def post(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('patient_username', type=str, required=True)
        args = parser.parse_args()

        try:
            doctor = Doctor.get_doctor_by_username(username)
            if doctor is not None:
                # Add the patient to the list of patients
                patients = doctor.get('patients', [])
                patients.append(args['patient_username'])

                # Update the doctor record with the new list of patients
                response = Doctor.update_doctor(username, patients=patients)
                return {'message': 'Patient added successfully', 'data': response}
            else:
                abort(404, message="Doctor not found")
        except Exception as e:
            abort(500, message=str(e))

    # @jwt_required()
    # @jwt_required()
    def delete(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('patient_username', type=str, required=True)
        args = parser.parse_args()
        try:
            doctor = Doctor.get_doctor_by_username(username)
            if doctor is not None:
                # Remove the patient from the list of patients
                patients = doctor.get('patients', [])
                patient = args['patient_username']
                if patient in patients:
                    patients.remove(patient)
                    # Update the doctor record with the updated list of patients
                    response = Doctor.update_doctor(username, patients=patients)
                    return {'message': 'Patient deleted successfully', 'data': response}
                else:
                    abort(404)  # Just abort with the status code
            else:
                abort(404)  # Just abort with the status code
        except Exception as e:
            abort(500)  # Just abort with the status code