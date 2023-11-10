from flask import redirect, render_template, url_for
from flask_login import current_user, login_required


def init_app(app):
    @app.route("/", endpoint="index")
    def index():
        if login_required and current_user.is_anonymous:
            return redirect(url_for("login"))

        return render_template("base.html")

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("error_404.html"), 404
