from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required
from sqlalchemy import desc

from control_clinic.forms import PatientForm, PatientUpdateForm
from control_clinic.models import db
from control_clinic.models.patients import Patient, Patient_phone


def init_app(app):
    @app.route(
        "/cadastro/cliente", methods=["GET", "POST"], endpoint="register_patient"
    )
    @login_required
    def register_patient():
        form = PatientForm()
        if form.validate_on_submit():
            try:
                existing_patient = Patient.query.filter_by(
                    document=form.document.data
                ).first()
                if existing_patient:
                    flash("El paciente ya existe.", "error")
                else:
                    patient = Patient(
                        firstname=form.firstname.data.upper(),
                        lastname=form.lastname.data.upper(),
                        birtday=form.birtday.data,
                        sex=form.sex.data,
                        name_father=form.name_father.data.upper(),
                        name_mather=form.name_mather.data.upper(),
                        document=form.document.data.upper(),
                        email=form.email.data,
                    )
                    db.session.add(patient)
                    db.session.commit()

                    phone = Patient_phone(
                        phone=form.phone.data,
                        patient=patient,
                    )
                    db.session.add(phone)
                    db.session.commit()

                    flash("Paciente registrado exitosamente!", "success")
                    return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                for error_message in e.args:
                    print(error_message)
                flash(
                    "Error al intentar registrarme.",
                    "error",
                )
        return render_template("forms/register-patient.html", form=form)

    @app.route("/listar/clientes", endpoint="list_patients")
    @login_required
    def list_patients():
        patients = Patient.query.order_by(desc(Patient.id)).all()
        return render_template("patients/list_patients.html", patients=patients)

    @app.route("/listar/cliente/<int:id>", endpoint="list_patient")
    @login_required
    def list_patient(id):
        patient = Patient.query.get_or_404(id)
        return render_template("patients/list_patient.html", patient=patient)

    @app.route("/buscar/cliente", methods=["GET", "POST"], endpoint="search_patient")
    @login_required
    def search_patient():
        if request.method == "POST":
            documento = request.form.get("document")
            patients = Patient.query.filter(
                Patient.document == documento).all()
            if not patients:
                flash("Cliente no localizado con este número de documento", "info")
        else:
            patients = []

        return render_template("patients/search_patient.html", patients=patients)

    @app.route("/atualizar/cliente/<int:id>", methods=["GET", "POST"], endpoint="update_patient")
    @login_required
    def update_patient(id):
        form = PatientUpdateForm()
        patient = Patient.query.get_or_404(id)
        patient_phone = patient.phone
        if form.validate_on_submit():
            if form.firstname.data:
                patient.firstname = form.firstname.data.upper()
            if form.lastname.data:
                patient.lastname = form.lastname.data.upper()
            if form.email.data:
                patient.email = form.email.data
            if form.birtday.data:
                patient.birtday = form.birtday.data
            if form.sex.data:
                patient.sex = form.sex.data
            if form.name_father.data:
                patient.name_father = form.name_father.data.upper()
            if form.name_mather.data:
                patient.name_mather = form.name_mather.data.upper()
            if form.document.data:
                patient.document = form.document.data.upper()
            if form.phone.data:
                if patient_phone:
                    patient_phone.phone = form.phone.data
                else:
                    phone = Patient_phone(
                        phone=form.phone.data,
                        patient=patient,
                    )
                    db.session.add(phone)
            db.session.commit()
            flash("Paciente actualizado exitosamente!", "success")
            return redirect(url_for("index"))
        return render_template(
            "patients/update_patient.html", form=form, patient=patient
        )
