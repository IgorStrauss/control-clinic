from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .service import SEX_CHOICES
db = SQLAlchemy()


class Employees(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now())
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.relationship("Employee_phone", backref="employee", uselist=False)

    def __str__(self):
        return self.firstname


class Employee_phone(db.Model):
    __tablename__ = "employee_phone"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, default=000)
    employee_id = db.Column(db.ForeignKey("employee.id"), nullable=False)

    def __str__(self):
        return self.phone


class Doctor(db.Model):
    __tablename__ = "doctor"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45), nullable=False,)
    lastname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    register = db.Column(db.String(45), nullable=False, default="undefined")
    password = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now())
    phone = db.relationship("Doctor_phone", backref="doctor", uselist=False)
    specialty = db.relationship(
        "Doctor_specialty", backref="doctor", uselist=True)

    def __str__(self):
        return self.firstname


class Doctor_phone(db.Model):
    __tablename__ = "doctor_phone"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, default=000)
    doctor_id = db.Column(db.ForeignKey("doctor.id"), nullable=False)

    def __str__(self):
        return self.phone


class Doctor_specialty(db.Model):
    __tablename__ = "doctor_specialty"
    id = db.Column(db.Integer, primary_key=True)
    specialty = db.Column(db.String(90), nullable=False, default="undefined")
    doctor_id = db.Column(db.ForeignKey("doctor.id"), nullable=False)

    def __str__(self):
        return self.specialty


class Patient(db.Model):
    __tablename__ = "patient"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    birtday = db.Column(db.String(10), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    name_father = db.Column(db.String(45), nullable=True)
    name_mather = db.Column(db.String(45), nullable=True)
    phone = db.relationship("Patient_phone", backref="patient", uselist=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now())

    def __str__(self):
        return self.firstname
    

    def __init__(self, firstname, lastname, birtday, sex):
        if sex not in [choice[0] for choice in SEX_CHOICES]:
            raise ValueError("Invalid sex value")
        self.firstname = firstname
        self.lastname = lastname
        self.birtday = birtday
        self.sex = sex


class Patient_phone(db.Model):
    __tablename__ = "patient_phone"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, default=000)
    patient_id = db.Column(db.ForeignKey("patient.id"), nullable=False)

    def __str__(self):
        return self.phone
