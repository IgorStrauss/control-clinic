from datetime import datetime

from flask_login import UserMixin

from . import db


class Doctor(db.Model, UserMixin):
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
    phone = db.relationship("DoctorPhone", backref="doctor", uselist=False)
    specialty = db.Column(db.ForeignKey("doctor_specialty.id"), nullable=False)

    def __str__(self):
        return self.firstname


class DoctorPhone(db.Model):
    __tablename__ = "doctor_phone"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(14), default=000)
    doctor_id = db.Column(db.ForeignKey("doctor.id"), nullable=False)

    def __str__(self):
        return self.phone

    @property
    def format_doctor_phone(self):
        return f"({self.phone[:3]}) {self.phone[3:7]}-{self.phone[7:]}"


class DoctorSpecialty(db.Model):
    __tablename__ = "doctor_specialty"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), unique=True,
                     nullable=False, default="undefined")

    def __str__(self):
        return self.name
