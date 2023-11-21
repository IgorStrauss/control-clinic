from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired


class MedicalRecordsForm(FlaskForm):
    patient_id = IntegerField(
        "patient_id",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ]
    )
