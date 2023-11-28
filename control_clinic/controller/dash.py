from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from control_clinic.models.medical_records_model import (ClinicCare,
                                                         MedicalRecords)
from control_clinic.models.patients import Patient


def init_app(app):
    @app.route("/", endpoint="index")
    def index():
        if login_required and current_user.is_anonymous:
            return redirect(url_for("login"))

        """Paginacao da tabela ClinicCare"""
        page = request.args.get("page", 1, type=int)
        per_page = 5

        clinic_care = ClinicCare.query.filter_by(in_service=True).paginate(
            page=page, per_page=per_page, error_out=False
        )
        patients = Patient.query.all()
        medical_records = MedicalRecords.query.all()
        return render_template("dash/dash_initial_page.html",
                               clinic_care=clinic_care, patients=patients,
                               medical_records=medical_records)
