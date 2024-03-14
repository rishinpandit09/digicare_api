from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask import abort

from app.models.alert import Alert


class AlertResource(Resource):
    @jwt_required()
    def get(self, alert_id):
        try:
            alert = Alert.objects.get(id=alert_id)
            return {'data': alert.to_json()}
        except Alert.DoesNotExist:
            abort(404, message="Alert not found")

    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('patient_id', type=str, required=True)
        parser.add_argument('doctor_id', type=str, required=True)
        args = parser.parse_args()

        try:
            new_alert = Alert(**args)
            new_alert.save()
            return {'message': 'Alert created successfully', 'data': new_alert.to_json()}
        except Exception as e:
            return {'message': f'Error creating alert: {str(e)}'}, 500

    @jwt_required()
    def put(self, alert_id):
        parser = reqparse.RequestParser()
        parser.add_argument('patient_id', type=str, required=True)
        parser.add_argument('doctor_id', type=str, required=True)
        args = parser.parse_args()

        try:
            alert = Alert.objects.get(id=alert_id)
            alert.update(**args)
            return {'message': 'Alert updated successfully', 'data': alert.to_json()}
        except Alert.DoesNotExist:
            abort(404, message="Alert not found")
        except Exception as e:
            return {'message': f'Error updating alert: {str(e)}'}, 500

    @jwt_required()
    def delete(self, alert_id):
        try:
            alert = Alert.objects.get(id=alert_id)
            alert.delete()
            return {'message': 'Alert deleted successfully'}
        except Alert.DoesNotExist:
            abort(404, message="Alert not found")
        except Exception as e:
            return {'message': f'Error deleting alert: {str(e)}'}, 500
