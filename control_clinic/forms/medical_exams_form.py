from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class MedicalExamForm(FlaskForm):
    exam = StringField(
        "exam",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=5, max=120,
                   message="Mínimo 3 caracteres, máximo 45 caracteres"),
        ],
    )
    description = StringField(
        "description",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=10, max=255,
                   message="Mínimo 3 caractere, máximo 255 caracteres"),
        ],
    )
