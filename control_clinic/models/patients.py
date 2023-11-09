from datetime import datetime

from control_clinic.service import SEX_CHOICES

from . import db


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
    phone = db.Column(db.String(14), default=000)
    patient_id = db.Column(db.ForeignKey("patient.id"), nullable=False)

    def __str__(self):
        return self.phone

    @property
    def format_patient_phone(self):
        return f"({self.phone[:3]}) {self.phone[3:7]}-{self.phone[7:]}"
