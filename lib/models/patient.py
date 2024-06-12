# lib/models/patient.py
import sqlite3

DB_PATH = 'hospital.db'

def create_patient_table():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Patient (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            doctor_id INTEGER,
            FOREIGN KEY (doctor_id) REFERENCES Doctor (doctor_id)
        )''')

def add_patient(name, age, gender, doctor_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Patient (name, age, gender, doctor_id) VALUES (?, ?, ?, ?)",
                       (name, age, gender, doctor_id))
        conn.commit()

def get_patients():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Patient")
        return cursor.fetchall()

def get_patients_by_doctor(doctor_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Patient WHERE doctor_id = ?", (doctor_id,))
        return cursor.fetchall()

def delete_patient(patient_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Patient WHERE id = ?", (patient_id,))
        conn.commit()

def update_patient(patient_id, name=None, age=None, gender=None, doctor_id=None):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE Patient SET name = ? WHERE id = ?", (name, patient_id))
        if age:
            cursor.execute("UPDATE Patient SET age = ? WHERE id = ?", (age, patient_id))
        if gender:
            cursor.execute("UPDATE Patient SET gender = ? WHERE id = ?", (gender, patient_id))
        if doctor_id:
            cursor.execute("UPDATE Patient SET doctor_id = ? WHERE id = ?", (doctor_id, patient_id))
        conn.commit()
