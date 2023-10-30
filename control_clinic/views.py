from flask import render_template


def init_app(app):
    @app.route("/")
    def index():
        return render_template("base.html")

    @app.route("/cadastro/funcionario", endpoint="register_employee")
    def register_employee():
        return render_template("forms/register-employee.html")