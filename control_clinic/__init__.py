import os

from flask import Flask, session
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from control_clinic.models import db
from control_clinic.models.doctors import Doctor
from control_clinic.models.employees import Employees

from . import views
from .admin_service import admin
from .controller import (clients, doctors, employees, medical_records_view,
                         signin)
from .controller.medical_records import initial_page

login_manager = LoginManager()

# from control_clinic.views import views


Migrate()
CSRFProtect()
Bootstrap()


@login_manager.user_loader
def load_user(user_id):
    parts = user_id.split('_')

    if len(parts) != 2:
        return None

    user_type, user_id = parts

    if user_type == 'colaborador':
        return Employees.query.get(int(user_id))
    elif user_type == 'medico':
        return Doctor.query.get(int(user_id))

    return None


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    if os.environ.get("FLASK_ENV") == "testing":
        app.config.from_object("database.TestConfigurations")
    elif os.environ.get("FLASK_ENV") == "development":
        app.config.from_object("database.DevelopmentConfig")
    elif os.environ.get("FLASK_ENV") == "production":
        app.config.from_object("database.ProductionConfig")
    else:
        raise ValueError("FLASK_ENV inválido")

    views.init_app(app)
    employees.init_app(app)
    doctors.init_app(app)
    clients.init_app(app)
    signin.init_app(app)
    initial_page.init_app(app)
    medical_records_view.init_app(app)

    db.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)
    Migrate(app, db)
    CSRFProtect(app)
    Bootstrap(app)

    return app
