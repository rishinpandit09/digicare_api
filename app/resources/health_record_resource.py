from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import abort

from app.models.health_record import HealthRecord


class HealthRecordResource(Resource):
    # @jwt_required()
    def get(self, health_record_id):
        try:
            health_record = HealthRecord.get_health_record_by_id(health_record_id)
            return {'data': health_record}
        except Exception as e:
            abort(500, message=str(e))

    # @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('patient', type=str, required=True)
        parser.add_argument('doctor', type=str, required=True)
        parser.add_argument('timestamp', type=str, required=True)
        parser.add_argument('parameters', type=list, required=True)
        parser.add_argument('notes', type=str)
        args = parser.parse_args()

        try:
            new_health_record = HealthRecord()
            response = new_health_record.create_health_record(**args)
            return {'message': 'Health Record created successfully', 'data': response}
        except Exception as e:
            abort(500)

    # @jwt_required()
    def put(self, health_record_id):
        parser = reqparse.RequestParser()
        parser.add_argument('patient_id', type=str, required=True)
        parser.add_argument('doctor_id', type=str, required=True)
        parser.add_argument('timestamp', type=str, required=True)
        parser.add_argument('parameters', type=list, required=True)
        parser.add_argument('notes', type=str)
        args = parser.parse_args()

        try:
            health_record = HealthRecord.get_health_record_by_id(health_record_id)
            if health_record:
                response = health_record.update_health_record(**args)
                return {'message': 'Health Record updated successfully', 'data': response}
            else:
                abort(404, message="Health Record not found")
        except Exception as e:
            abort(500, message=str(e))

    # @jwt_required()
    def delete(self, health_record_id):
        try:
            health_record = HealthRecord.get_health_record_by_id(health_record_id)
            if health_record:
                response = health_record.delete_health_record()
                return {'message': 'Health Record deleted successfully', 'data': response}
            else:
                abort(404, message="Health Record not found")
        except Exception as e:
            abort(500, message=str(e))
