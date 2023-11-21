from flask import flash, redirect, render_template, url_for
from flask_login import login_required
from werkzeug.security import generate_password_hash

from control_clinic.forms.employees_form import (EmployeeForm,
                                                 EmployeeUpdateForm)
from control_clinic.models import db
from control_clinic.models.employees import EmployeePhone, Employees


def init_app(app):
    @app.route(
        "/cadastro/funcionario", methods=["GET", "POST"], endpoint="register_employee"
    )
    # @login_required
    # TODO: definir login_required
    # TODO: Definir regra que se tiver logado, redirecionar para index
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
                    phone = EmployeePhone(
                        phone=form.phone.data,
                        employee=employee,
                    )
                    db.session.add(phone)
                    db.session.commit()

                    flash("Empleado registrado exitosamente!", "success")
                    return redirect(url_for("login"))
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
    @login_required
    def list_employees():
        employees = Employees.query.all()
        return render_template("employees/list_employees.html", employees=employees)

    @app.route("/listar/funcionario/<int:id>", endpoint="list_employee")
    @login_required
    def list_employee(id):
        employee = Employees.query.get_or_404(id)
        return render_template("employees/list_employee.html", employee=employee)

    @app.route(
        "/atualizar/funcionario/<int:id>",
        methods=["GET", "POST"],
        endpoint="update_employee",
    )
    @login_required
    def update_employee(id):
        form = EmployeeUpdateForm()
        employee = Employees.query.get_or_404(id)

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

        return render_template(
            "employees/update_employees.html", form=form, employee=employee
        )
