from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required
from sqlalchemy import desc

from control_clinic.forms.patients_form import PatientForm, PatientUpdateForm
from control_clinic.models import db
from control_clinic.models.medical_records_model import MedicalRecords
from control_clinic.models.patients import (Patient, PatientAddress,
                                            PatientPhone)


def init_app(app):
    @app.route(
        "/cadastro/cliente", methods=["GET", "POST"], endpoint="register_patient"
    )
    @login_required
    def register_patient():
        form = PatientForm()

        if request.method == "POST":
            print("Inputs recebidos")
            for fields, value in form.data.items():
                print(f"{fields}: {value}")
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
                        sex=form.sex.data.upper(),
                        name_father=form.name_father.data.upper(),
                        name_mather=form.name_mather.data.upper(),
                        reference_telephone=form.reference_telephone.data,
                        reference_contact=form.reference_contact.data.upper(),
                        document=form.document.data.upper(),
                        email=form.email.data,
                        marital_status=form.marital_status.data.upper(),
                        profession=form.profession.data.upper(),
                        controlled_medicine=form.controlled_medicine.data.upper(),
                        smoker=form.smoker.data,
                        consumes_alcohol=form.consumes_alcohol.data,
                        drug_user=form.drug_user.data,
                        chronic_disease=form.chronic_disease.data.upper(),
                        allergies=form.allergies.data.upper(),
                        blood_type=form.blood_type.data,
                    )
                    print("Patient: linha 46")
                    db.session.add(patient)
                    db.session.commit()

                    phone = PatientPhone(
                        phone=form.phone.data,
                        patient=patient,
                    )
                    print("Phone: linha 54")
                    db.session.add(phone)
                    db.session.commit()

                    addresses = PatientAddress(
                        address=form.address.data.upper(),
                        number=form.number.data,
                        complement=form.complement.data.upper(),
                        neighborhood=form.neighborhood.data.upper(),
                        city=form.city.data.upper(),
                        state=form.state.data,
                        patient=patient,
                    )
                    print("Address: linha66")
                    db.session.add(addresses)
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
        medical_records_dict = {
            record.patient_id: record.id for record in MedicalRecords.query.all()
        }
        return render_template(
            "patients/list_patients.html",
            patients=patients,
            medical_records_dict=medical_records_dict,
        )

    @app.route("/listar/cliente/<int:id>", endpoint="list_patient")
    @login_required
    def list_patient(id):
        patient = Patient.query.get_or_404(id)
        medical_record = MedicalRecords.query.filter_by(
            patient_id=patient.id).first()

        return render_template(
            "patients/list_patient.html", patient=patient, medical_record=medical_record
        )

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

    @app.route(
        "/atualizar/cliente/<int:id>",
        methods=["GET", "POST"],
        endpoint="update_patient",
    )
    @login_required
    def update_patient(id):
        form = PatientUpdateForm()
        patient = Patient.query.get_or_404(id)
        patient_phone = patient.phone
        patient_address = patient.address
        if form.validate_on_submit():
            print(f"Name: {form.firstname.data}")
            if form.firstname.data:
                patient.firstname = form.firstname.data.upper()
            if form.lastname.data:
                patient.lastname = form.lastname.data.upper()
            if form.email.data:
                patient.email = form.email.data
            if form.birtday.data:
                patient.birtday = form.birtday.data
            if form.sex.data:
                patient.sex = form.sex.data.upper()
            if form.name_father.data:
                patient.name_father = form.name_father.data.upper()
            if form.name_mather.data:
                patient.name_mather = form.name_mather.data.upper()
            if form.reference_telephone.data:
                patient.reference_telephone = form.reference_telephone.data
            if form.reference_contact.data:
                patient.reference_contact = form.reference_contact.data.upper()
            if form.document.data:
                patient.document = form.document.data.upper()
            if form.marital_status.data:
                patient.marital_status = form.marital_status.data.upper()
            if form.profession.data:
                patient.profession = form.profession.data.upper()
            if form.controlled_medicine.data:
                patient.controlled_medicine = form.controlled_medicine.data.upper()
            if form.blood_type.data:
                patient.blood_type = form.blood_type.data
            if form.smoker.data:
                patient.smoker = form.smoker.data
            if form.consumes_alcohol.data:
                patient.consumes_alcohol = form.consumes_alcohol.data
            if form.drug_user.data:
                patient.drug_user = form.drug_user.data
            if form.chronic_disease.data:
                patient.chronic_disease = form.chronic_disease.data.upper()
            if form.allergies.data:
                patient.allergies = form.allergies.data.upper()
            if form.address.data:
                patient_address.address = form.address.data.upper()
            if form.number.data:
                patient_address.number = form.number.data
            if form.complement.data:
                patient_address.complement = form.complement.data.upper()
            if form.neighborhood.data:
                patient_address.neighborhood = form.neighborhood.data.upper()
            if form.city.data:
                patient_address.city = form.city.data.upper()
            if form.state.data:
                patient_address.state = form.state.data
            if form.phone.data:
                patient_phone.phone = form.phone.data

            db.session.commit()
            flash("Paciente actualizado exitosamente!", "success")
            return redirect(url_for("index"))
        return render_template(
            "patients/update_patient.html", form=form, patient=patient
        )

    @app.route("/listar/prontuario/paciente/<int:id>", endpoint="list_medical_records")
    def list_medical_records(id):
        patient = Patient.query.get_or_404(id)
        medical_record = MedicalRecords.query.filter_by(
            patient_id=patient.id).first()

        return render_template(
            "patients/list_medical_record.html",
            patient=patient,
            medical_record=medical_record,
        )
