# lib/helpers.py
from models.doctor import add_doctor, get_doctors, delete_doctor
from models.patient import add_patient, get_patients, get_patients_by_doctor, delete_patient, update_patient

def add_doctor_helper():
    name = input("Enter doctor's name: ")
    email = input("Enter doctor's email: ")
    phone = input("Enter doctor's phone: ")
    add_doctor(name, email, phone)
    print("Doctor added successfully.")

def view_doctors_helper():
    doctors = get_doctors()
    if doctors:
        for doctor in doctors:
            print(doctor)
    else:
        print("No doctors found.")

def add_patient_helper():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    gender = input("Enter patient's gender: ")
    doctor_id = input("Enter doctor's ID: ")
    add_patient(name, age, gender, doctor_id)
    print("Patient added successfully.")

def view_patients_helper():
    patients = get_patients()
    if patients:
        for patient in patients:
            print(patient)
    else:
        print("No patients found.")

def view_patients_of_doctor_helper():
    doctor_id = input("Enter doctor's ID: ")
    patients = get_patients_by_doctor(doctor_id)
    if patients:
        for patient in patients:
            print(patient)
    else:
        print(f"No patients found for doctor ID {doctor_id}.")

def delete_doctor_helper():
    doctor_id = input("Enter doctor's ID to delete: ")
    delete_doctor(doctor_id)
    print(f"Doctor with ID {doctor_id} deleted.")

def delete_patient_helper():
    patient_id = input("Enter patient's ID to delete: ")
    delete_patient(patient_id)
    print(f"Patient with ID {patient_id} deleted.")

def update_patient_helper():
    patient_id = input("Enter patient's ID to update: ")
    print("Leave field empty if no change is needed.")
    name = input("Enter new name: ") or None
    age = input("Enter new age: ") or None
    gender = input("Enter new gender: ") or None
    doctor_id = input("Enter new doctor's ID: ") or None
    update_patient(patient_id, name, age, gender, doctor_id)
    print(f"Patient with ID {patient_id} updated.")
