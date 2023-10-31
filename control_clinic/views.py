from flask import flash, redirect, render_template, url_for
from werkzeug.security import generate_password_hash

from .forms import EmployeeForm, SpecialtyForm
from .models import Doctor_specialty, Employees, db


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
                    flash("Empleado registrado exitosamente!", "success")
                    return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                for error_message in e.args:
                    print(error_message)
                flash(
                    "Error al intentar dar de alta al empleado, inténtalo de nuevo.",
                    "error",
                )
        return render_template("forms/register-employee.html", form=form)

    @app.route("/cadastro/medico", endpoint="register_doctor")
    def register_doctor():
        return render_template("forms/register-doctor.html")

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
                    print("linha 65")
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
                    "Error al intentar registrar la especialidad, o una existente, Inténtalo de nuevo.",
                    "error",
                )

        return render_template("forms/register-specialty.html", form=form)

    @app.route("/cadastro/paciente", endpoint="register_patient")
    def register_patient():
        return render_template("forms/register-patient.html")
