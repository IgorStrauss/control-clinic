from flask import render_template


def init_app(app):
    @app.route("/login", methods=["GET", "POST"], endpoint="login")
    def login():
        return render_template("auth/login.html")
