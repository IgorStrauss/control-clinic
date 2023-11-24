from flask import flash, redirect, render_template, request, url_for
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
        "/iniciar/atendimento/paciente",
        methods=["GET", "POST"],
        endpoint="start__clinic_care_patient",
    )
    @login_required
    def start_clinic_care_patient_search():
        if request.method == "POST":
            documento = request.form.get("document")
            patients = Patient.query.filter(
                Patient.document == documento).all()
            if not patients:
                flash("Cliente no localizado con este número de documento", "info")
        else:
            patients = []

        return render_template("patients/start_clinic_care.html", patients=patients)

    @app.route(
        "/iniciar/atendimento/paciente/<int:id>",
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
                print("linha 30")
                if patient.medical_records is None:
                    flash("Este paciente não possui um prontuário.", "info")
                    print("linha 33")
                    return redirect(url_for("index"))
                else:
                    print("Dados recebidos:", form.data)

                    start_service = ClinicCare(
                        medical_rec_id=form.medical_rec_id.data,
                        patient_id=form.patient_id.data,
                        doctor_id=form.doctor_id.data,
                        # exams=form.exams.data,
                        medical_exams=[
                            MedicalExam.query.get(exam_id)
                            for exam_id in form.selected_exams.data
                        ],
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

                    print("linha 68")
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

    @app.route(
        "/listar/atendimentos/paciente/<int:id>",
        methods=["GET"],
        endpoint="list_clinic_care",
    )
    def list_clinic_care(id):
        patient = Patient.query.get_or_404(id)
        clinic_care_list = ClinicCare.query.filter_by(
            patient_id=patient.id).all()
        medical_record = MedicalRecords.query.filter_by(
            patient_id=patient.id).first()

        return render_template(
            "patients/list_clinic_care.html",
            patient=patient,
            clinic_care_list=clinic_care_list,
            medical_record=medical_record,
        )

    @app.route(
        "/detalhes/atendimento/paciente/consulta/<int:id>",
        methods=["GET"],
        endpoint="clinic_care_id",
    )
    def view_clinic_care(id):
        clinic_care = ClinicCare.query.get_or_404(id)
        patient = Patient.query.get_or_404(clinic_care.patient_id)

        return render_template(
            "patients/view_clinic_care.html",
            clinic_care=clinic_care,
            patient=patient
        )

    @app.route(
        "/listar/historico/atendimento/paciente",
        methods=["GET", "POST"],
        endpoint="historical__clinic_care_patient",
    )
    @login_required
    def historical_clinic_care_patient_search():
        """Lista historico de pacientes medicante consulta por numero de documento"""
        if request.method == "POST":
            documento = request.form.get("document")
            patients = Patient.query.filter(
                Patient.document == documento).all()
            if not patients:
                flash("Cliente no localizado con este número de documento", "info")
        else:
            patients = []

        return render_template("patients/historical_clinic_care.html", patients=patients)
