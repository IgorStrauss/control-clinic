from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from .service import SEX_CHOICES

db = SQLAlchemy()


class Employees(db.Model):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(64), nullable=False)
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
    firstname = db.Column(
        db.String(45),
        nullable=False,
    )
    lastname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    register = db.Column(db.String(45), nullable=False, default="undefined")
    password = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )
    phone = db.relationship("Doctor_phone", backref="doctor", uselist=False)
    specialty = db.Column(db.ForeignKey("doctor_specialty.id"), nullable=False)

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
    name = db.Column(db.String(90), unique=True,
                     nullable=False, default="undefined")

    def __str__(self):
        return self.name


class Patient(db.Model):
    __tablename__ = "patient"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    birtday = db.Column(db.String(10), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    name_father = db.Column(
        db.String(45), nullable=False, default="No informado")
    name_mather = db.Column(
        db.String(45), nullable=False, default="No informado")
    document = db.Column(db.String(45), unique=True, nullable=False)
    email = db.Column(db.String(45), nullable=True)
    phone = db.relationship("Patient_phone", backref="patient", uselist=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )

    def __str__(self):
        return self.firstname

    def __init__(
        self,
        firstname,
        lastname,
        birtday,
        sex,
        name_father,
        name_mather,
        document,
        email,
    ):
        if sex not in [choice[0] for choice in SEX_CHOICES]:
            raise ValueError("Invalid sex value")
        self.firstname = firstname
        self.lastname = lastname
        self.birtday = birtday
        self.sex = sex
        self.name_father = name_father
        self.name_mather = name_mather
        self.document = document
        self.email = email


class Patient_phone(db.Model):
    __tablename__ = "patient_phone"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, default=000)
    patient_id = db.Column(db.ForeignKey("patient.id"), nullable=False)

    def __str__(self):
        return self.phone
