from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

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
