from control_clinic.models import db
from control_clinic.models.doctors import DoctorSpecialty
from control_clinic.models.medical_records_model import MedicalExam

from .populate_datas import exams_data_populate, specialty_data_populate


def populate_medical_exams():
    if MedicalExam.query.count() == 0:
        for exam, description in exams_data_populate():
            medical_exam = MedicalExam(exam=exam, description=description)
            db.session.add(medical_exam)

        db.session.commit()


def populate_specialty_data():
    if DoctorSpecialty.query.count() == 0:
        for specialty in specialty_data_populate():
            doctor_specialty = DoctorSpecialty(name=specialty)
            db.session.add(doctor_specialty)

        db.session.commit()
