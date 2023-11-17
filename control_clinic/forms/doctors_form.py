from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, Length


class SpecialtyForm(FlaskForm):
    name = StringField(
        "Especialidad",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )


class DoctorForm(FlaskForm):
    firstname = StringField(
        "firstname",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    lastname = StringField(
        "lastname",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    email = StringField(
        "email",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Email("Endereço de e-mail inválido."),
        ],
    )
    register = StringField(
        "register",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    password = PasswordField(
        "password",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=8, message="Mínimo 8 caracteres"),
        ],
    )
    phone = StringField(
        "phone",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=10, max=15,
                   message="Mínimo 10 caracteres, máximo 15 caracteres"),
        ],
    )
    specialty = StringField(
        "specialty", validators=[DataRequired("Este campo é obrigatório.")]
    )


class DoctorUpdateForm(FlaskForm):
    firstname = StringField(
        "firstname",
        validators=[
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    lastname = StringField(
        "lastname",
        validators=[
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    email = StringField(
        "email",
        validators=[
            Email("Endereço de e-mail inválido."),
        ],
    )
    register = StringField(
        "register",
        validators=[
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    phone = StringField(
        "phone",
        validators=[
            Length(min=10, max=15,
                   message="Mínimo 10 caracteres, máximo 15 caracteres"),
        ],
    )
    specialty = StringField()
