from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_restful import reqparse, abort
from app.models.patient import Patient
from app.models.doctor import Doctor
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_token(identity):
    try:
        access_token = create_access_token(identity=identity)
        return access_token
    except Exception as e:
        abort(500, message=f"Error creating access token: {str(e)}")

def verify_password(user_type, username, password):
    try:
        user = None

        if user_type.lower() == 'patient':
            user = Patient.objects(name=username).first()
        elif user_type.lower() == 'doctor':
            user = Doctor.objects(name=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return True
        return False
    except Exception as e:
        abort(500, message=f"Error verifying password: {str(e)}")

def authenticate(user_type):
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='This field cannot be blank', required=True)
        parser.add_argument('password', help='This field cannot be blank', required=True)
        args = parser.parse_args()

        username = args['username']
        password = args['password']

        if verify_password(user_type, username, password):
            access_token = create_token(username)
            return {'access_token': access_token}, 200
        else:
            abort(401, message="Invalid credentials")
    except Exception as e:
        abort(500, message=f"Authentication error: {str(e)}")

def identity():
    try:
        current_user = get_jwt_identity()
        return {'user': current_user}
    except Exception as e:
        abort(500, message=f"Error identifying user: {str(e)}")

def password_hash(password):
    try:
        return bcrypt.generate_password_hash(password).decode('utf-8')
    except Exception as e:
        abort(500, message=f"Error hashing password: {str(e)}")
