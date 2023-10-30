from flask import render_template


def init_app(app):
    @app.route("/", endpoint="index")
    def index():
        return render_template("base.html")

    @app.route("/cadastro/funcionario", endpoint="register_employee")
    def register_employee():
        return render_template("forms/register-employee.html")

    @app.route("/cadastro/medico", endpoint="register_doctor")
    def register_doctor():
        return render_template("forms/register-doctor.html")

    @app.route("/cadastro/especialidade", endpoint="register_specialty")
    def register_specialty():
        return render_template("forms/register-specialty.html")
