from flask_wtf import FlaskForm
from wtforms import (FieldList, FloatField, FormField, IntegerField,
                     SelectMultipleField, StringField)
from wtforms.validators import DataRequired, Length


class ClinicCareForm(FlaskForm):
    medical_rec_id = IntegerField(
        "medical_records_id",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ]
    )
    patient_id = IntegerField(
        "patient_id",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ]
    )
    doctor_id = IntegerField(
        "doctor_id",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ]
    )
    selected_exams = SelectMultipleField(
        "exams",
        choices=[],
        coerce=int
    )
    blood_pressure = StringField(
        "blood_pressure",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ]
    )
    heart_rate = FloatField(
        "heart_rate",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ]
    )
    respiratory_frequency = StringField(
        "respiratory_frequency",
    )
    temperature = FloatField(
        "temperature",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ]
    )
    weight = FloatField(
        "weight",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ]
    )
    length = FloatField(
        "length",
    )
    diagnosis = StringField(
        "diagnosis",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=10, max=255,
                   message="Mínimo 25 caracteres, máximo 255 caracteres"),
        ]
    )
    treatment = StringField(
        "treatment",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=10, max=255,
                   message="Mínimo 25 caracteres, máximo 255 caracteres"),
        ]
    )
    doctors_prescription = StringField(
        "doctors_prescription",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=10, max=255,
                   message="Mínimo 10 caracteres, máximo 255 caracteres"),
        ]
    )
    laboratory_results = StringField(
        "laboratory_results",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=10, max=255,
                   message="Mínimo 10 caracteres, máximo 255 caracteres"),
        ]
    )
    initial_report = StringField(
        "initial_report",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=10, max=255,
                   message="Mínimo 10 caracteres, máximo 255 caracteres"),
        ]
    )
