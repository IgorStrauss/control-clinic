from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required

from control_clinic.models import db
from control_clinic.models.medical_records_model import MedicalRecords
from control_clinic.models.patients import Patient


def init_app(app):
    @app.route(
        "/create_medical_record/<int:patient_id>",
        methods=["POST", "GET"],
        endpoint="create_medical_record",
    )
    @login_required
    def create_medical_record(patient_id):
        patient = Patient.query.get_or_404(patient_id)

        # Verifica se o paciente já possui um prontuário
        if MedicalRecords.query.filter_by(patient_id=patient.id).first() is not None:
            flash("Este paciente já possui um prontuário.", "info")
            return redirect(url_for("index"))
        # Crie o prontuário e associe ao paciente
        medical_record = MedicalRecords(patient_id=patient.id)
        db.session.add(medical_record)
        db.session.commit()
        flash("Prontuário criado com sucesso, agora pode iniciar o atendimento.", "success")
        return redirect(url_for("start__clinic_care_patient"))


# @app.route("/view_medical_record/<int:id>", methods=["GET"], endpoint="view_medical_record")
# @login_required
# def view_medical_record(id):

#     ...
# medical_record = MedicalRecords.query.get_or_404(id)
# return render_template("forms/medical-records.html", medical_record=medical_record)
# TODO: Implementar a visualização do prontuário apos criar o Atendimento
