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
            Length(min=8, message="Mínimo 8 caracteres"),
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


class SpecialtyForm(FlaskForm):
    name = StringField(
        "Especialidad",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )


class PatientForm(FlaskForm):
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
    birtday = StringField(
        "fecha de nacimiento",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )
    sex = StringField("Sexo", validators=[
        DataRequired("Este campo é obrigatório."),
    ])
    name_father = StringField(
        "Apellido paterno",
        validators=[
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres")
        ],
    )
    name_mather = StringField(
        "Apellido materno",
        validators=[
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres")
        ],
    )
    document = StringField(
        "Documento",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=4, message="Mínimo 4 caracteres"),
        ],
    )
    email = StringField(
        "email",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Email("Endereço de e-mail inválido."),
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
