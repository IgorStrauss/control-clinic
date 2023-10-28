#bin/sh

up:
	python main.py

up-gunicorn:
	gunicorn -c control_clinic/gunicorn_config.py app:app
#export FLASK_ENV=production && gunicorn -c project/gunicorn_config.py app:app
