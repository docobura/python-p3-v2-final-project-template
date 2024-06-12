# lib/cli.py
import sys
from models import create_tables
import helpers

def print_menu():
    print("Select an option:")
    print("1. Add Doctor")
    print("2. View Doctors")
    print("3. Add Patient")
    print("4. View Patients")
    print("5. View Patients of a Doctor")
    print("6. Delete Doctor")
    print("7. Delete Patient")
    print("8. Update Patient")
    print("9. Exit")

def main():
    create_tables()
    while True:
        print_menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            helpers.add_doctor_helper()
        elif choice == '2':
            helpers.view_doctors_helper()
        elif choice == '3':
            helpers.add_patient_helper()
        elif choice == '4':
            helpers.view_patients_helper()
        elif choice == '5':
            helpers.view_patients_of_doctor_helper()
        elif choice == '6':
            helpers.delete_doctor_helper()
        elif choice == '7':
            helpers.delete_patient_helper()
        elif choice == '8':
            helpers.update_patient_helper()
        elif choice == '9':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
