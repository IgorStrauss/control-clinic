from flask import flash, redirect, render_template, request, url_for
from sqlalchemy import desc
from werkzeug.security import generate_password_hash

from .forms import (DoctorForm, EmployeeForm, EmployeeUpdateForm, PatientForm,
                    SpecialtyForm)
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

    @app.route("/listar/funcionario/<int:id>", endpoint="list_employee")
    def list_employee(id):
        employee = Employees.query.get(id)
        return render_template("employees/list_employee.html", employee=employee)

    @app.route("/atualizar/funcionario/<int:id>", methods=["GET", "POST"], endpoint="update_employee")
    def update_employee(id):
        form = EmployeeUpdateForm()
        employee = Employees.query.get(id)

        # Carregue os dados do telefone associado ao funcionário
        employee_phone = employee.phone

        if form.validate_on_submit():
            if form.firstname.data:
                employee.firstname = form.firstname.data.upper()
            if form.lastname.data:
                employee.lastname = form.lastname.data.upper()
            if form.email.data:
                employee.email = form.email.data

            # Atualize o número de telefone se um novo número for fornecido
            if form.phone.data:
                employee_phone.phone = form.phone.data

            db.session.commit()  # Salva as atualizações no banco de dados

            flash("Dados do funcionário atualizados com sucesso", "success")
            return redirect(url_for("list_employee", id=id))

        # Preenche os campos do formulário com os dados atuais do funcionário
        form.firstname.data = employee.firstname
        form.lastname.data = employee.lastname
        form.email.data = employee.email

        # Preenche o campo de telefone com o número de telefone atual
        if employee_phone:
            form.phone.data = employee_phone.phone

        return render_template("employees/update_employees.html", form=form, employee=employee)

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
