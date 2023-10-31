from flask import flash, redirect, render_template, url_for
from werkzeug.security import generate_password_hash

from .forms import EmployeeForm
from .models import Employees, db


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
                    flash("Este email já está em uso.", "error")
                else:
                    employee = Employees(
                        firstname=form.firstname.data,
                        lastname=form.lastname.data,
                        email=form.email.data,
                        password=generate_password_hash(form.password.data),
                    )
                    db.session.add(employee)
                    db.session.commit()
                    flash("Funcionário cadastrado com sucesso!", "success")
                    return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                for error_message in e.args:
                    print(error_message)
                flash(
                    "Erro ao tentar cadastrar o funcionário, tente novamente.", "error"
                )
        return render_template("forms/register-employee.html", form=form)

    @app.route("/cadastro/medico", endpoint="register_doctor")
    def register_doctor():
        return render_template("forms/register-doctor.html")

    @app.route("/cadastro/especialidade", endpoint="register_specialty")
    def register_specialty():
        return render_template("forms/register-specialty.html")

    @app.route("/cadastro/paciente", endpoint="register_patient")
    def register_patient():
        return render_template("forms/register-patient.html")
