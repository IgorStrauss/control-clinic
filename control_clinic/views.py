from flask import redirect, render_template, url_for
from flask_login import current_user, login_required

from control_clinic.models.medical_records_model import (ClinicCare,
                                                         MedicalRecords)
from control_clinic.models.patients import Patient


def init_app(app):
    @app.route("/", endpoint="index")
    def index():
        if login_required and current_user.is_anonymous:
            return redirect(url_for("login"))

        clinic_care = ClinicCare.query.all()
        patients = Patient.query.all()
        medical_records = MedicalRecords.query.all()
        return render_template("dash/dash_initial_page.html", clinic_care=clinic_care, patients=patients, medical_records=medical_records)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("error_404.html"), 404
