from datetime import datetime

from control_clinic import db

from .doctors import Doctor
from .employees import Employees
from .patients import Patient

clinical_care_medical_exams = db.Table(
    "clinical_care_medical_exams",
    db.Column("clinical_care_id", db.Integer,
              db.ForeignKey("clinical_care.id")),
    db.Column("medical_exams_id", db.Integer,
              db.ForeignKey("medical_exam.id")),
)


class MedicalRecords(db.Model):
    __tablename__ = "medical_records"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.ForeignKey(Patient.id), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )

    def __str__(self):
        return str(self.medical_record_id)


class MedicalExam(db.Model):
    __tablename__ = "medical_exam"
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
    __tablename__ = "clinical_care"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    medical_rec_id = db.Column(db.ForeignKey(
        MedicalRecords.id), nullable=False)
    attendant_id = db.Column(db.ForeignKey(Employees.id), nullable=False)
    attendant = db.relationship(
        "Employees", back_populates="clinic_care_attended")
    doctor_id = db.Column(db.ForeignKey(Doctor.id), nullable=False)
    doctor = db.relationship("Doctor", back_populates="clinical_care_records")
    patient_id = db.Column(db.ForeignKey(Patient.id), nullable=False)
    patient = db.relationship(
        "Patient", back_populates="clinical_care")
    medical_exams = db.relationship(
        MedicalExam, secondary="clinical_care_medical_exams", lazy="dynamic", backref="clinical_care"
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
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )

    def __str__(self):
        return str(self.medical_record_id)

    @property
    def formatted_clinic_care_created_at(self):
        return (
            self.created_at.strftime(
                "%d/%m/%Y %H:%M:%S") if self.created_at else None
        )
