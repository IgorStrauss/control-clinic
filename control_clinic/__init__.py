import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from control_clinic.models import db

from . import views
from .admin_service import admin
from .controller import clients, doctors, employees

# from control_clinic.views import views


Migrate()
CSRFProtect()
Bootstrap()


def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    if os.environ.get('FLASK_ENV') == 'testing':
        app.config.from_object('database.TestConfigurations')
    elif os .environ.get('FLASK_ENV') == 'development':
        app.config.from_object('database.DevelopmentConfig')
    elif os .environ.get('FLASK_ENV') == 'production':
        app.config.from_object('database.ProductionConfig')
    else:
        raise ValueError('FLASK_ENV inválido')

    views.init_app(app)
    employees.init_app(app)
    doctors.init_app(app)
    clients.init_app(app)

    db.init_app(app)
    admin.init_app(app)
    Migrate(app, db)
    CSRFProtect(app)
    Bootstrap(app)

    return app
