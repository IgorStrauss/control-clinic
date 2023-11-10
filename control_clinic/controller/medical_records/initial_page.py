def init_app(app):
    @app.route("/initial-page", methods=["GET"], endpoint="initial_page")
    def initial_page():
        return "Initial Page Medical"
