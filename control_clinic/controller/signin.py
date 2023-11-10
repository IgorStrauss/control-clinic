from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash

from control_clinic.models.doctors import Doctor
from control_clinic.models.employees import Employees


def init_app(app):
    @app.route("/login", methods=["GET", "POST"], endpoint="login")
    def login():
        if request.method != "POST":
            return render_template("auth/login.html")

        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        if role == "medico":
            user = Doctor.query.filter_by(email=email).first()
        elif role == "colaborador":
            user = Employees.query.filter_by(email=email).first()
        else:
            flash("Papel de usuário inválido!", "error")
            return redirect(url_for("login"))

        if not user or not check_password_hash(user.password, password):
            flash("Credenciais incorretas!", "error")
            app.logger.warning(
                f"Tentativa de login com credenciais inválidas: {email}, {role}"
            )
            return redirect(url_for("login"))

        # Atribua a ID do usuário com o prefixo do tipo de usuário
        user.id = f"{role}_{user.id}"
        login_user(user)

        if role == "medico":
            return redirect(url_for("initial_page"))
        flash("Login efetuado com sucesso!", "success")
        return redirect(url_for("index"))

    @app.route("/logout", methods=["GET"], endpoint="logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("login"))
