from flask import flash, redirect, render_template, url_for
from flask_login import login_required

from control_clinic.forms.clinic_care_forms import ClinicCareForm
from control_clinic.models import db
from control_clinic.models.doctors import Doctor
from control_clinic.models.medical_records_model import (ClinicCare,
                                                         MedicalExam,
                                                         MedicalRecords)
from control_clinic.models.patients import Patient


def init_app(app):
    @app.route(
        "/iniciar-atendimento/<int:id>",
        methods=["GET", "POST"],
        endpoint="start_clinic_care",
    )
    @login_required
    def start_clinic_care(id):
        patient = Patient.query.get_or_404(id)
        medical_record = MedicalRecords.query.filter_by(
            patient_id=patient.id).first()
        doctors = Doctor.query.all()
        exams = MedicalExam.query.all()

        form = ClinicCareForm()

        # Adicione dinamicamente as escolhas para o campo 'exams' do formulário
        form.selected_exams.choices = [(exam.id, exam.exam) for exam in exams]

        if form.validate_on_submit():
            try:
                print('linha 30')
                if patient.medical_records is None:
                    flash("Este paciente não possui um prontuário.", "info")
                    print('linha 33')
                    return redirect(url_for("index"))
                else:
                    print('Dados recebidos:', form.data)

                    start_service = ClinicCare(
                        medical_rec_id=form.medical_rec_id.data,
                        patient_id=form.patient_id.data,
                        doctor_id=form.doctor_id.data,
                        # exams=form.exams.data,
                        medical_exams=[MedicalExam.query.get(
                            exam_id) for exam_id in form.selected_exams.data],
                        blood_pressure=form.blood_pressure.data,
                        heart_rate=form.heart_rate.data,
                        respiratory_frequency=form.respiratory_frequency.data,
                        weight=form.weight.data,
                        length=form.length.data,
                        temperature=form.temperature.data,
                        initial_report=form.initial_report.data,
                        diagnosis=form.diagnosis.data,
                        treatment=form.treatment.data,
                        laboratory_results=form.laboratory_results.data,
                        doctors_prescription=form.doctors_prescription.data,
                    )

                    print('linha 68')
                    db.session.add(start_service)
                    db.session.commit()
                    flash("Atendimento iniciado com sucesso!", "success")
                    return redirect(url_for("index"))

            except Exception as e:
                db.session.rollback()
                for error_message in e.args:
                    print(error_message)
                flash("Erro ao tentar registrar.", "error")

        return render_template(
            "forms/clinic-care.html",
            form=form,
            patient=patient,
            medical_record=medical_record,
            doctors=doctors,
            exams=exams,
        )
    # def start_clinic_care(id):
    #     patient = Patient.query.get_or_404(id)
    #     medical_record = MedicalRecords.query.filter_by(
    #         patient_id=patient.id).first()
    #     doctors = Doctor.query.all()
    #     exams = MedicalExam.query.all()
    #     form = ClinicCareForm()

    #     if form.validate_on_submit():
    #         try:
    #             print('linha 30')
    #             if patient.medical_record is None:
    #                 flash("Este paciente não possui um prontuario.", "info")
    #                 print('linha 33')
    #                 return redirect(url_for("index"))
    #             else:
    #                 print('Datos recebidos:', form.data)

    #                 start_service = ClinicCare(
    #                     medical_records_id=form.medical_records_id.data,
    #                     doctor_id=form.doctor_id.data,
    #                     exams=form.exams.data,
    #                     blood_pressure=form.blood_pressure.data,
    #                     heart_rate=form.heart_rate.data,
    #                     respiratory_frequency=form.respiratory_frequency.data,
    #                     weight=form.weight.data,
    #                     length=form.length.data,
    #                     temperature=form.temperature.data,
    #                     initial_report=form.initial_report.data,
    #                     diagnosis=form.diagnosis.data,
    #                     treatment=form.treatment.data,
    #                     laboratory_results=form.laboratory_results.data,
    #                     doctors_prescription=form.doctors_prescription.data,
    #                 )
    #                 print('linha 68')
    #                 db.session.add(start_service)
    #                 db.session.commit()
    #                 flash("Atendimento iniciado com sucesso!", "success")
    #                 return redirect(url_for("index"))
    #         except Exception as e:
    #             db.session.rollback()
    #             for error_message in e.args:
    #                 print(error_message)
    #             flash(
    #                 "Error al intentar registrarme.",
    #                 "error",
    #             )
    #             return render_template(
    #                 "forms/clinic-care.html",
    #                 form=form,
    #                 patient=patient,
    #                 medical_record=medical_record,
    #                 doctors=doctors,
    #                 exams=exams,
    #             )

    #     return render_template(
    #         "forms/clinic-care.html",
    #         form=form,
    #         patient=patient,
    #         medical_record=medical_record,
    #         doctors=doctors,
    #         exams=exams,
    #     )