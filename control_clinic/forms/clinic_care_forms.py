from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, Length


class ClinicCareForm(FlaskForm):
    medical_records_id = IntegerField(
        "medical_records_id",
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
    exams = IntegerField(
        "medical_exams",
    )
    bood_pressure = StringField(
        "bood_pressure",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 2 caractere, máximo 10 caracteres"),
        ]
    )
    heart_rate = StringField(
        "heart_rate",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=2, max=45, message="Mínimo 2 caractere, máximo 10 caracteres"),
        ]
    )
    respiratory_frequency = StringField(
        "respiratory_frequency",
    )
    temperature = StringField(
        "temperature",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=2, max=45, message="Mínimo 2 caractere, máximo 10 caracteres"),
        ]
    )
    weight = StringField(
        "weight",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=2, max=45, message="Mínimo 2 caractere, máximo 10 caracteres"),
        ]
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
