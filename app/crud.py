from config import get_session
from models import Patient, MedicalStaff, Hospital

# Function to add a new patient
def add_patient(name, email, dob):
    session = get_session()
    new_patient = Patient(name=name, email=email, dob=dob)
    session.add(new_patient)
    session.commit()
    print(f"Patient {name} added successfully.")
    session.close()

# Function to view all patients
def view_patients():
    session = get_session()
    patients = session.query(Patient).all()
    for patient in patients:
        print(f"{patient.id}. {patient.name}, DOB: {patient.dob}")
    session.close()

# Function to update patient details
def update_patient(patient_id, name=None, dob=None):
    session = get_session()
    patient = session.query(Patient).get(patient_id)
    if patient:
        if name:
            patient.name = name
        if dob:
            patient.dob = dob
        session.commit()
        print(f"Patient {patient_id} updated.")
    else:
        print("Patient not found.")
    session.close()

# Function to delete a patient
def delete_patient(patient_id):
    session = get_session()
    patient = session.query(Patient).get(patient_id)
    if patient:
        session.delete(patient)
        session.commit()
        print(f"Patient {patient_id} deleted.")
    else:
        print("Patient not found.")
    session.close()

# Functions for Medical Staff CRUD
def add_medical_staff(title, name, email):
    session = get_session()
    new_staff = MedicalStaff(title=title, name=name, email=email)
    session.add(new_staff)
    session.commit()
    print(f"Medical Staff {name} added successfully.")
    session.close()

def view_medical_staff():
    session = get_session()
    staffs = session.query(MedicalStaff).all()
    for staff in staffs:
        print(f"{staff.id}. {staff.name}, {staff.title}")
    session.close()

def update_medical_staff(staff_id, title=None, name=None):
    session = get_session()
    staff = session.query(MedicalStaff).get(staff_id)
    if staff:
        if title:
            staff.title = title
        if name:
            staff.name = name
        session.commit()
        print(f"Medical Staff {staff_id} updated.")
    else:
        print("Staff not found.")
    session.close()

def delete_medical_staff(staff_id):
    session = get_session()
    staff = session.query(MedicalStaff).get(staff_id)
    if staff:
        session.delete(staff)
        session.commit()
        print(f"Medical Staff {staff_id} deleted.")
    else:
        print("Staff not found.")
    session.close()

# Functions for Hospital CRUD
def add_hospital(name, email):
    session = get_session()
    new_hospital = Hospital(name=name, email=email)
    session.add(new_hospital)
    session.commit()
    print(f"Hospital {name} added successfully.")
    session.close()

def view_hospitals():
    session = get_session()
    hospitals = session.query(Hospital).all()
    for hospital in hospitals:
        print(f"{hospital.id}. {hospital.name}, Email: {hospital.email}")
    session.close()

def update_hospital(hospital_id, name=None, email=None):
    session = get_session()
    hospital = session.query(Hospital).get(hospital_id)
    if hospital:
        if name:
            hospital.name = name
        if email:
            hospital.email = email
        session.commit()
        print(f"Hospital {hospital_id} updated.")
    else:
        print("Hospital not found.")
    session.close()

def delete_hospital(hospital_id):
    session = get_session()
    hospital = session.query(Hospital).get(hospital_id)
    if hospital:
        session.delete(hospital)
        session.commit()
        print(f"Hospital {hospital_id} deleted.")
    else:
        print("Hospital not found.")
    session.close()
