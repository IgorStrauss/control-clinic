from flask import render_template


def init_app(app):
    @app.route("/", endpoint="index")
    def index():
        return render_template("base.html")

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("error_404.html"), 404
