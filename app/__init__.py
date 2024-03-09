from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from app.utils.auth import identity, authenticate

app = Flask(__name__)

# MongoDB Configuration
app.config['MONGODB_SETTINGS'] = {
    'db': 'health_monitoring',
    'host': 'mongodb://localhost:27017/health_monitoring'
}
db = MongoEngine(app)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

# Bcrypt Configuration
bcrypt = Bcrypt(app)

# Add the authentication endpoints
app.config['JWT_AUTH_URL_RULE'] = '/api/auth'  # Change the URL endpoint as needed

# Add authentication view functions
jwt.authentication_callback_loader(authenticate)
jwt.identity_loader(identity)
# Import your resources to register them with the app
from app.resources import patient_resource, doctor_resource, alert_resource, teleconsultation_resource, health_record_resource
