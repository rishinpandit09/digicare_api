from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import abort

from app.models.health_record import HealthRecord

class HealthRecordResource(Resource):
    @jwt_required()
    def get(self, health_record_id):
        try:
            health_record = HealthRecord.objects.get(id=health_record_id)
            return {'data': health_record.to_json()}
        except HealthRecord.DoesNotExist:
            abort(404, message="Health Record not found")

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('patient_id', type=str, required=True)
        parser.add_argument('doctor_id', type=str, required=True)
        parser.add_argument('timestamp', type=str, required=True)
        parser.add_argument('parameters', type=list, required=True)
        parser.add_argument('notes', type=str)
        args = parser.parse_args()

        try:
            new_health_record = HealthRecord(**args)
            new_health_record.save()
            return {'message': 'Health Record created successfully', 'data': new_health_record.to_json()}
        except Exception as e:
            return {'message': f'Error creating Health Record: {str(e)}'}, 500

    @jwt_required()
    def put(self, health_record_id):
        parser = reqparse.RequestParser()
        parser.add_argument('patient_id', type=str, required=True)
        parser.add_argument('doctor_id', type=str, required=True)
        parser.add_argument('timestamp', type=str, required=True)
        parser.add_argument('parameters', type=list, required=True)
        parser.add_argument('notes', type=str)
        args = parser.parse_args()

        try:
            health_record = HealthRecord.objects.get(id=health_record_id)
            health_record.update(**args)
            return {'message': 'Health Record updated successfully', 'data': health_record.to_json()}
        except HealthRecord.DoesNotExist:
            abort(404, message="Health Record not found")
        except Exception as e:
            return {'message': f'Error updating Health Record: {str(e)}'}, 500

    @jwt_required()
    def delete(self, health_record_id):
        try:
            health_record = HealthRecord.objects.get(id=health_record_id)
            health_record.delete()
            return {'message': 'Health Record deleted successfully'}
        except HealthRecord.DoesNotExist:
            abort
