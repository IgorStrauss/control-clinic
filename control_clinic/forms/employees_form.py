from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, Length


class EmployeeForm(FlaskForm):
    firstname = StringField(
        "Primer nombre",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    lastname = StringField(
        "Apellido",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    email = StringField(
        "E-mail",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Email("Endereço de e-mail inválido."),
            Length(min=8, message="Mínimo 8 caracteres"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=8, max=64, message="Mínimo 8 caracteres"),
        ],
    )
    phone = StringField(
        "Teléfono móvil",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=10, max=15,
                   message="Mínimo 10 caracteres, máximo 15 caracteres"),
        ],
    )


class EmployeeUpdateForm(FlaskForm):
    firstname = StringField(
        "Primer nombre",
        validators=[
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    lastname = StringField(
        "Apellido",
        validators=[
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    email = StringField(
        "E-mail",
        validators=[
            Email("Endereço de e-mail inválido."),
        ],
    )
    phone = StringField(
        "Teléfono móvil",
        validators=[
            Length(min=10, max=15,
                   message="Mínimo 10 caracteres, máximo 15 caracteres"),
        ],
    )
