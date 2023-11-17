from datetime import datetime

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
    reference_telephone = db.Column(
        db.String(14), nullable=False, default="No informado"
    )
    reference_contact = db.Column(
        db.String(45), nullable=False, default="No informado")
    document = db.Column(db.String(45), unique=True, nullable=False)
    email = db.Column(db.String(45), nullable=True)
    marital_status = db.Column(
        db.String(45), nullable=False, default="Soltero")
    profession = db.Column(db.String(45), nullable=False,
                           default="No informado")
    controlled_medicine = db.Column(
        db.String(255), nullable=False, default="No informado"
    )
    blood_type = db.Column(db.String(45), nullable=False,
                           default="No informado")
    smoker = db.Column(db.Boolean, default=False)
    consumes_alcohol = db.Column(db.Boolean, default=False)
    drug_user = db.Column(db.Boolean, default=False)
    chronic_disease = db.Column(
        db.String(255), nullable=False, default="No informado")
    allergies = db.Column(db.String(255), nullable=False,
                          default="No informado")
    phone = db.relationship(
        "PatientPhone",
        back_populates="patient",
        uselist=False,
        lazy="joined",
        cascade="all, delete-orphan",
    )
    address = db.relationship(
        "PatientAddress",
        back_populates="patient",
        uselist=False,
        lazy="joined",
        cascade="all, delete-orphan",
    )
    medical_record = db.relationship(
        "MedicalRecords",
        back_populates="patient",
        uselist=False,
        lazy="joined",
        cascade="all, delete-orphan",
    )
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )

    @property
    def age(self):
        if self.birtday:
            birth_date = datetime.strptime(self.birtday, "%Y-%m-%d")
            today = datetime.now()
            age = (
                today.year
                - birth_date.year
                - ((today.month, today.day) < (birth_date.month, birth_date.day))
            )
            return age
        return None

    @property
    def format_patient_reference_phone(self):
        return f"({self.reference_telephone[:3]}) {self.reference_telephone[3:7]}-{self.reference_telephone[7:]}"

    @property
    def formatted_created_at(self):
        return (
            self.created_at.strftime(
                "%d/%m/%Y %H:%M:%S") if self.created_at else None
        )

    @property
    def formatted_updated_at(self):
        return (
            self.updated_at.strftime(
                "%d/%m/%Y %H:%M:%S") if self.updated_at else None
        )

    def __str__(self):
        return self.firstname


class PatientPhone(db.Model):
    __tablename__ = "patient_phone"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(14), default="000")
    patient_id = db.Column(db.ForeignKey("patient.id"), nullable=False)
    patient = db.relationship("Patient", back_populates="phone")

    def __str__(self):
        return self.phone

    @property
    def format_patient_phone(self):
        return f"({self.phone[:3]}) {self.phone[3:7]}-{self.phone[7:]}"


class PatientAddress(db.Model):
    __tablename__ = "patient_address"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    complement = db.Column(db.String(45), nullable=False, default="Não")
    neighborhood = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    patient_id = db.Column(db.ForeignKey("patient.id"), nullable=False)
    patient = db.relationship("Patient", back_populates="address")

    def __str__(self):
        return self.address
