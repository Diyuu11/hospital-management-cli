from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from config import Base  # Assuming Base is defined in the config file

# Junction table to represent the Many-to-Many relationship between Patients and Hospitals
enrollments = Table('enrollments', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('hospital_id', Integer, ForeignKey('hospitals.id')),
    Column('patient_id', Integer, ForeignKey('patients.id'))
)

class MedicalStaff(Base):
    __tablename__ = 'medical_staffs'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Foreign key linking MedicalStaff to a Hospital
    hospital_id = Column(Integer, ForeignKey('hospitals.id'), nullable=False)

    # Relationship back to the Hospital
    hospital = relationship('Hospital', back_populates='medical_staffs')

    patients = relationship('Patient', back_populates='doctor')

class Hospital(Base):
    __tablename__ = 'hospitals'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # Many-to-Many relationship with Patients via Enrollments table
    patients = relationship('Patient', secondary=enrollments, back_populates='hospitals')

    # One-to-Many relationship with MedicalStaff
    medical_staffs = relationship('MedicalStaff', back_populates='hospital')

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    dob = Column(Date, nullable=False)  # Use Date type for Date of Birth

    # Many-to-Many relationship with Hospitals via Enrollments table
    hospitals = relationship('Hospital', secondary=enrollments, back_populates='patients')

    # One-to-Many relationship with MedicalStaff (a patient is assigned to a doctor)
    doctor_id = Column(Integer, ForeignKey('medical_staffs.id'))
    doctor = relationship('MedicalStaff', back_populates='patients')
