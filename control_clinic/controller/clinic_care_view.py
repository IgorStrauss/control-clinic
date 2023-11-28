from datetime import datetime, timedelta

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
            "patients/view_clinic_care.html", clinic_care=clinic_care, patient=patient
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

        return render_template(
            "patients/historical_clinic_care.html", patients=patients
        )

    @app.route(
        "/encerrar/atendimento/<int:id>", methods=["POST"], endpoint="end_clinic_care"
    )
    @login_required
    def end_clinic_care(id):
        clinic_care = ClinicCare.query.get_or_404(id)

        clinic_care.in_service = False

        db.session.commit()

        flash("Atendimento encerrado com sucesso!", "success")

        return redirect(url_for("index"))

    @app.route("/listar/atendimentos", methods=["GET"], endpoint="list_clinic_care_all")
    @login_required
    def list_clinic_care_all():
        """Listar todas as consultas, com filtros opcionais de data."""

        # Obtenha os parâmetros da data inicial e final da consulta de URL
        start_date_str = request.args.get("start_date")
        end_date_str = request.args.get("end_date")

        # Converte as strings de data para objetos datetime se fornecidas
        start_date = (
            datetime.strptime(
                start_date_str, "%Y-%m-%d") if start_date_str else None
        )
        end_date = datetime.strptime(
            end_date_str, "%Y-%m-%d") if end_date_str else None

        # Obtenha a página e o número de registros por página
        page = request.args.get("page", 1, type=int)
        per_page = 5

        # Crie a consulta base sem filtro de data
        query = ClinicCare.query.order_by(ClinicCare.id.desc())

        # Adicione o filtro de data, se fornecido
        if start_date and end_date:
            end_date += timedelta(days=1)
            query = query.filter(
                ClinicCare.created_at.between(start_date, end_date))
        elif start_date:
            query = query.filter(ClinicCare.created_at >= start_date)
        elif end_date:
            end_date += timedelta(days=1)
            query = query.filter(ClinicCare.created_at <= end_date)

        # Execute a consulta
        clinic_care_data = (
            query.all()
            if start_date
            else query.paginate(page=page, per_page=per_page, error_out=False)
        )

        # Verifica se retorna uma lista vazia baseado na consulta
        no_records_message = (
            "NENHUM ATENDIMENTO ENCONTRADO NESTE PERÍODO"
            if start_date and not clinic_care_data
            else None
        )

        return render_template(
            "dash/dash_list_clinic_care.html",
            clinic_care_data=clinic_care_data,
            no_records_message=no_records_message,
        )

    @app.route(
        "/limpar/consultas/", methods=["POST", "GET"], endpoint="clear_clinic_care"
    )
    @login_required
    def clear_clinic_care():
        """Limpar a lista de consultas, após filtro aplicado."""
        return redirect(url_for("list_clinic_care_all"))

    @app.route("/listar/atendimentos/medico", methods=["GET"], endpoint="list_clinic_care_doctor")
    def list_clinic_care_doctor():
        doctors = Doctor.query.all()
        selected_doctor_id = request.args.get('doctor_id')

        if selected_doctor_id:
            clinic_care_doctor = ClinicCare.query.filter_by(
                doctor_id=selected_doctor_id).all()
        else:
            clinic_care_doctor = []

        return render_template("dash/dash_list_clinic_care_doctor.html",
                               clinic_care_doctor=clinic_care_doctor,
                               doctors=doctors,
                               selected_doctor_id=selected_doctor_id)

    @app.route(
        "/limpar/consultas/filtro/medicos", methods=["POST", "GET"], endpoint="clear_clinic_care_doctor"
    )
    @login_required
    def clear_clinic_care_doctor():
        """Limpar a lista de consultas, após filtro aplicado."""
        return redirect(url_for("list_clinic_care_doctor"))
