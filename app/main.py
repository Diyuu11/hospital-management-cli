import argparse
from crud import add_patient, view_patients, update_patient, delete_patient, \
    add_medical_staff, view_medical_staff, update_medical_staff, delete_medical_staff, \
    add_hospital, view_hospitals, update_hospital, delete_hospital
from config import create_db
from datetime import datetime


# Function to display a simple menu and take input from the user
def show_menu():
    print("\n--- Hospital Management System ---")
    print("1. Manage Patients")
    print("2. Manage Medical Staff")
    print("3. Manage Hospitals")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    return choice

# Function to handle patient managementfrom datetime import datetime

def manage_patients():
    print("\n--- Patient Management ---")
    print("1. Add a new patient")
    print("2. View all patients")
    print("3. Update patient details")
    print("4. Delete a patient")
    print("5. Back to main menu")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        name = input("Enter patient name: ")
        email = input("Enter patient email: ")
        dob = input("Enter patient date of birth (YYYY-MM-DD): ")

        # Validate and convert the date of birth
        try:
            dob = datetime.strptime(dob, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        add_patient(name, email, dob)
    elif choice == '2':
        view_patients()
    elif choice == '3':
        patient_id = int(input("Enter patient ID to update: "))
        name = input("Enter new name: ")
        dob = input("Enter new date of birth (YYYY-MM-DD): ")

        # Validate and convert the date of birth
        try:
            dob = datetime.strptime(dob, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        update_patient(patient_id, name, dob)
    elif choice == '4':
        patient_id = int(input("Enter patient ID to delete: "))
        delete_patient(patient_id)
    elif choice == '5':
        return
    else:
        print("Invalid choice, please try again.")

# Function to handle medical staff management
def manage_medical_staff():
    print("\n--- Medical Staff Management ---")
    print("1. Add a new medical staff")
    print("2. View all medical staff")
    print("3. Update medical staff details")
    print("4. Delete a medical staff")
    print("5. Back to main menu")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        title = input("Enter staff title: ")
        name = input("Enter staff name: ")
        email = input("Enter staff email: ")
        add_medical_staff(title, name, email)
    elif choice == '2':
        view_medical_staff()
    elif choice == '3':
        staff_id = int(input("Enter staff ID to update: "))
        title = input("Enter new title: ")
        name = input("Enter new name: ")
        update_medical_staff(staff_id, title, name)
    elif choice == '4':
        staff_id = int(input("Enter staff ID to delete: "))
        delete_medical_staff(staff_id)
    elif choice == '5':
        return
    else:
        print("Invalid choice, please try again.")

# Function to handle hospital management
def manage_hospitals():
    print("\n--- Hospital Management ---")
    print("1. Add a new hospital")
    print("2. View all hospitals")
    print("3. Update hospital details")
    print("4. Delete a hospital")
    print("5. Back to main menu")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        name = input("Enter hospital name: ")
        email = input("Enter hospital email: ")
        add_hospital(name, email)
    elif choice == '2':
        view_hospitals()
    elif choice == '3':
        hospital_id = int(input("Enter hospital ID to update: "))
        name = input("Enter new hospital name: ")
        email = input("Enter new hospital email: ")
        update_hospital(hospital_id, name, email)
    elif choice == '4':
        hospital_id = int(input("Enter hospital ID to delete: "))
        delete_hospital(hospital_id)
    elif choice == '5':
        return
    else:
        print("Invalid choice, please try again.")

# Main function to run the CLI
def main():
    create_db()  # Create the database and tables if they don't exist

    while True:
        choice = show_menu()

        if choice == '1':
            manage_patients()
        elif choice == '2':
            manage_medical_staff()
        elif choice == '3':
            manage_hospitals()
        elif choice == '4':
            print("Exiting Hospital Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
