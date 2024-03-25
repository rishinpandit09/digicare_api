from flask_restful import Resource, reqparse
from flask import request
from app.models.TimeSlot import TimeSlot
from flask import abort


class TimeSlots(Resource):

    def post(self, username):
        data = request.get_json()

        # Ensure data is a list
        if not isinstance(data, list):
            return {'message': 'Invalid data format. Expected a list.'}, 400

        for item in data:
            parser = reqparse.RequestParser()

            parser.add_argument('day_name', type=str, required=True)
            parser.add_argument('start_time', type=str, required=True)
            parser.add_argument('end_time', type=str, required=True)

            args = item

            try:
                timeslot = TimeSlot()
                timeslot.createTimeSlot(username, **args)
                # return {'message': 'Time slot created successfully',
                #     'data': args}
            except Exception as e:
                return {'message': f'Error creating patient: {str(e)}'}, 500

    def get(self, username):
        try:
            slots = TimeSlot.get_time_slots_by_doctor_username(username)
            if slots:
                return slots
            else:
                abort(404, "Time slots not found for this doctor")
        except Exception as e:
            abort(500, "Internal Server Error")