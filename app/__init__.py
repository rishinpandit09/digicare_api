from flask import Flask
from flask_mongoengine import MongoEngine
# from flask_jwt_extended import JWTManager
from app.utils.config import Config
app = Flask(__name__)
# app.config.from_object('app.utils.config')
app.config.from_object(Config)
db = MongoEngine(app)
# jwt = JWTManager(app)

# Import your resources to register them with the app
from app.resources import (
    patient_resource, doctor_resource,
    alert_resource, teleconsultation_resource, health_record_resource
)
from app.utils.auth import authenticate, identity


app.config['JWT_AUTH_URL_RULE'] = '/api/auth'
# jwt.authentication_callback_loader(authenticate)
# jwt.identity_loader(identity)

