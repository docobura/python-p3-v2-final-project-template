# lib/models/doctor.py
import sqlite3

DB_PATH = 'hospital.db'

def create_doctor_table():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Doctor (
            doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            doctor_name TEXT NOT NULL,
            doctor_email TEXT,
            doctor_phone INTEGER
        )''')

def add_doctor(name, email, phone):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Doctor (doctor_name, doctor_email, doctor_phone) VALUES (?, ?, ?)",
                       (name, email, phone))
        conn.commit()

def get_doctors():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Doctor")
        return cursor.fetchall()

def delete_doctor(doctor_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Doctor WHERE doctor_id = ?", (doctor_id,))
        conn.commit()
