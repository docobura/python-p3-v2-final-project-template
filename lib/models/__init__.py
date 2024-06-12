# lib/models/__init__.py
from .doctor import create_doctor_table
from .patient import create_patient_table

def create_tables():
    create_doctor_table()
    create_patient_table()
