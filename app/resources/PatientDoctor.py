from flask_restful import Resource, reqparse, abort

from app.models import Patient


class PatientDoctor(Resource):
    # @jwt_required()
    def post(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('doctor_username', type=str, required=True)
        args = parser.parse_args()

        try:
            patient = Patient.get_patient_by_username(username)
            if patient is not None:
                # Add the doctor to the list of doctor
                doctors = patient.get('doctors', [])
                doctors.append(args['doctor_username'])

                # Update the patient record with the new list of doctors
                response = Patient.update_doctors(username, patients=doctors)
                return {'message': 'Doctor added successfully', 'data': response}
            else:
                abort(404, message="Patient not found")
        except Exception as e:
            abort(500, message=str(e))

    # @jwt_required()
    def delete(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('doctor_username', type=str, required=True)
        args = parser.parse_args()

        try:
            patient = Patient.get_patient_by_username(username)
            if patient is not None:
                # Remove the doctor from the list of doctor
                doctors = patient.get('doctors', [])
                doctor = args['doctor_username']
                if doctor in doctors:
                    doctors.remove(doctor)
                    # Update the patient record with the updated list of doctors
                    response = Patient.update_doctors(username, doctors=doctors)
                    return {'message': 'Patient deleted successfully', 'data': response}
                else:
                    abort(404)  # Just abort with the status code
            else:
                abort(404)  # Just abort with the status code
        except Exception as e:
            abort(500)  # Just abort with the status code