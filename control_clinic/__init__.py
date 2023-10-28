import os
from flask import Flask
from flask_migrate import Migrate
from . import views
from .models import db
Migrate()


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

    db.init_app(app)
    Migrate(app, db)

    return app
