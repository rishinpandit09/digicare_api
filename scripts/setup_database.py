# setup_database.py

from app import app, db
from app.models import Patient, Doctor
from app.utils.auth import password_hash

import sys

print(sys.path)

# Initialize the Flask app
with app.app_context():
    # Drop existing tables
    db.connection.drop_database(app.config['MONGODB_SETTINGS']['db'])

    # # Create tables
    # db.create_all()

    # Add dummy data
    # Add Patients
    patient1 = Patient(
    name='John Doe',
    dob='1990-05-15',
    gender='Male',
    contact_info={
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    },
    medical_history=[
        {
            "condition": "Hypertension",
            "diagnosis_date": "2010-01-01",
            "treatment": "Medication"
        },
        {
            "condition": "Allergies",
            "diagnosis_date": "2015-03-10",
            "treatment": "Antihistamines"
        }
        # Add more medical history items as needed
    ],
    doctors=[],  # Initially, the patient doesn't have any assigned doctors
    username='john_doe',
    password=password_hash('secure_password')
)
    patient2 =Patient(
    name="Jane Smith",
    dob="1985-08-22",
    gender="Female",
    contact_info={
        "email": "jane.smith@example.com",
        "phone": "987-654-3210"
    },
    medical_history=[
        {
            "condition": "Asthma",
            "diagnosis_date": "2000-07-15",
            "treatment": "Inhaler"
        },
        {
            "condition": "Migraines",
            "diagnosis_date": "2012-02-20",
            "treatment": "Prescription Medication"
        }
        # Add more medical history items as needed
    ],
    doctors=[],  # Initially, the patient doesn't have any assigned doctors
    username="jane_smith",
    password=password_hash("strong_password")
)
    patient1.save()
    patient2.save()
    # Add Doctors
    doctor1 = Doctor(name='Dr. Smith', specialization='Cardiology', username='drsmith',
                     password=password_hash('password'))
    doctor2 = Doctor(name='Dr. Johnson', specialization='Dermatology', username='drjohnson',
                     password=password_hash('password'))

    # Add Alerts, Teleconsultations, HealthRecords, etc.
    doctor1.save()
    doctor2.save()

    # Add more data as needed...

print("Database setup completed.")
