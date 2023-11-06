from flask import flash, redirect, render_template, request, url_for
from sqlalchemy import desc
from werkzeug.security import generate_password_hash

from .forms import DoctorForm, EmployeeForm, PatientForm, SpecialtyForm
from .models import (Doctor, Doctor_phone, Doctor_specialty, Employee_phone,
                     Employees, Patient, Patient_phone, db)


def init_app(app):
    @app.route("/", endpoint="index")
    def index():
        return render_template("base.html")

    @app.route(
        "/cadastro/funcionario", methods=["GET", "POST"], endpoint="register_employee"
    )
    def register_employee():
        """Register employee with form"""
        form = EmployeeForm()
        if form.validate_on_submit():
            try:
                # Verifique se o email já existe
                existing_employee = Employees.query.filter_by(
                    email=form.email.data
                ).first()
                if existing_employee:
                    flash("Este correo electrónico ya está en uso.", "error")
                else:
                    employee = Employees(
                        firstname=form.firstname.data.upper(),
                        lastname=form.lastname.data.upper(),
                        email=form.email.data,
                        password=generate_password_hash(form.password.data),
                    )
                    db.session.add(employee)
                    db.session.commit()

                    # Adicionando telefone
                    phone = Employee_phone(
                        phone=form.phone.data,
                        employee=employee,
                    )
                    db.session.add(phone)
                    db.session.commit()

                    flash("Empleado registrado exitosamente!", "success")
                    return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                for error_message in e.args:
                    print(error_message)
                flash(
                    "Error al intentar registrarme.",
                    "error",
                )
        return render_template("forms/register-employee.html", form=form)

    @app.route("/listar/funcionarios", endpoint="list_employees")
    def list_employees():
        employees = Employees.query.all()
        return render_template("employees/list_employees.html", employees=employees)

    @app.route("/cadastro/medico", methods=["GET", "POST"], endpoint="register_doctor")
    def register_doctor():
        specialidads = Doctor_specialty.query.all()
        form = DoctorForm()

        if form.validate_on_submit():
            try:
                # Verifique se o email já existe
                existing_doctor = Doctor.query.filter_by(
                    email=form.email.data).first()
                if existing_doctor:
                    flash("Este correo ya estaba registrado.", "error")
                else:
                    doctor = Doctor(
                        firstname=form.firstname.data.upper(),
                        lastname=form.lastname.data.upper(),
                        email=form.email.data,
                        register=form.register.data,
                        password=generate_password_hash(form.password.data),
                        specialty=form.specialty.data,
                    )
                    db.session.add(doctor)
                    db.session.commit()

                    phone = Doctor_phone(
                        phone=form.phone.data,
                        doctor=doctor,
                    )
                    db.session.add(phone)
                    db.session.commit()
                    flash("Médico registrado exitosamente!", "success")
                    return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                for error_message in e.args:
                    print(error_message)
                flash(
                    "Error al intentar registrarme.",
                    "error",
                )
        return render_template(
            "forms/register-doctor.html", specialidads=specialidads, form=form
        )

    @app.route("/listar/medicos", endpoint="list_medicos")
    def list_medicos():
        medicos = Doctor.query.all()
        return render_template("doctors/list_medicos.html", medicos=medicos)

    @app.route(
        "/cadastro/especialidade",
        methods=["GET", "POST"],
        endpoint="register_specialty",
    )
    def register_specialty():
        form = SpecialtyForm()
        if form.validate_on_submit():
            try:
                existing_specialty = Doctor_specialty.query.filter_by(
                    name=form.name.data
                ).first()
                if existing_specialty:
                    flash("La especialidad ya existe.", "error")
                else:
                    specialty = Doctor_specialty(
                        name=form.name.data.upper(),
                    )
                    print(form.name.data)
                    db.session.add(specialty)
                    db.session.commit()
                    flash("Especialidad registrada con éxito!", "success")
                    return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                for error_message in e.args:
                    print(error_message)
                flash(
                    "Error al intentar registrarme.",
                    "error",
                )

        return render_template("forms/register-specialty.html", form=form)

    @app.route(
        "/cadastro/paciente", methods=["GET", "POST"], endpoint="register_patient"
    )
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

    @app.route("/listar/pacientes", endpoint="list_patients")
    def list_patients():
        pacientes = Patient.query.order_by(desc(Patient.id)).all()
        return render_template("patients/list_patients.html", pacientes=pacientes)

    @app.route("/buscar/paciente", methods=["GET", "POST"], endpoint="search_patient")
    def search_patient():
        if request.method == "POST":
            documento = request.form.get("document")
            pacientes = Patient.query.filter(
                Patient.document == documento).all()
            if not pacientes:
                flash("Cliente no localizado con este número de documento", "info")
        else:
            pacientes = []

        return render_template("patients/update_patient.html", pacientes=pacientes)
