from datetime import datetime

from control_clinic import db

from .doctors import Doctor
from .patients import Patient


class MedicalRecords(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey(Patient.id), unique=True)
    patient = db.relationship(
        "Patient",
        back_populates="medical_record",
        uselist=False,
        lazy="joined",
    )
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )

    def __str__(self):
        return self.patient.firstname


class MedicalExam(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exam = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )

    def __str__(self):
        return self.exam


class ClinicCare(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    medical_records_id = db.Column(
        db.Integer, db.ForeignKey(MedicalRecords.id))
    doctor_id = db.Column(db.Integer, db.ForeignKey(Doctor.id))
    exams = db.relationship(
        "MedicalExam", secondary="clinic_care_medical_exams", backref="clinic_care"
    )
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )
    in_service = db.Column(db.Boolean, default=True)
    blood_pressure = db.Column(db.String(10))
    heart_rate = db.Column(db.Float, default=0.0, nullable=False)
    respiratory_frequency = db.Column(db.String(10))
    weight = db.Column(db.Float, default=0.0, nullable=False)
    length = db.Column(db.Float, default=0.0, nullable=False)
    temperature = db.Column(db.Float, default=0.0, nullable=False)
    initial_report = db.Column(db.String(255), nullable=False)
    diagnosis = db.Column(db.String(255), nullable=False)
    treatment = db.Column(db.String(255), nullable=False)
    laboratory_results = db.Column(db.String(255), default="No informado")
    doctors_prescription = db.Column(db.String(255), default="No informado")

    def __str__(self):
        return self.medical_records_id


class ClinicCareMedicalExams(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    medical_exam_id = db.Column(db.Integer, db.ForeignKey(MedicalExam.id))
    clinic_care_id = db.Column(db.Integer, db.ForeignKey(ClinicCare.id))
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )

    def __str__(self):
        return self.clinic_care_id
