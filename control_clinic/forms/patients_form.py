from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField
from wtforms.fields import DateField, SelectField
from wtforms.validators import DataRequired, Email, Length


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
    birtday = DateField(
        "Fecha de nacimiento",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )
    sex_choices = [
        ("masculino", "Masculino"),
        ("feminino", "Feminino"),
        ("outro", "Outro"),
    ]
    sex = SelectField(
        "Sexo",
        choices=sex_choices,
        validators=[DataRequired("Este campo é obrigatório.")],
    )
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
    reference_telephone = StringField(
        "Telefone de referencia",
        validators=[
            Length(
                min=10, max=15, message="Mínimo 10 caracteres, máximo 14 caracteres"
            ),
            DataRequired("Este campo é obrigatório."),
        ],
    )
    reference_contact = StringField(
        "Contacto de referencia",
        validators=[
            Length(min=3, max=45,
                   message="Mínimo 10 caracteres, máximo 45 caracteres"),
            DataRequired("Este campo é obrigatório."),
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
    marital_status = StringField(
        "Estado civil",
        validators=[
            Length(
                min=3, max=45, message="Mínimo 3 caractere,.Disclaimer 45 caracteres"
            ),
        ],
    )
    profession = StringField(
        "Profesión",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    blood_type_choices = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("AB", "AB"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("nao_sabe", "Nao sabe"),
    ]
    blood_type = SelectField(
        "Tipo sanguíneo",
        choices=blood_type_choices,
        validators=[DataRequired("Este campo é obrigatório.")],
    )
    smoker = BooleanField(
        "Fumante",
    )
    controlled_medicine = StringField(
        "Remedio controlado",
        default="Sem remedio controlado",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )
    consumes_alcohol = BooleanField(
        "Consume Alcohol",
    )
    drug_user = BooleanField(
        "Consume drogas",
    )
    chronic_disease = StringField(
        "Doenças crônicas",
        default="Sem doenças crônicas",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )
    allergies = StringField(
        "Alergias",
        default="Sem alergias",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )

    phone = StringField(
        "phone",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(
                min=10, max=15, message="Mínimo 10 caracteres, máximo 15 caracteres"
            ),
        ],
    )
    address = StringField(
        "Endereço",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    number = StringField(
        "Número",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=10),
        ],
    )
    complement = StringField(
        "Complemento",
        default="Sem complemento",
        validators=[
            Length(min=1, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    neighborhood = StringField(
        "Barrio",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    city = StringField(
        "Ciudad",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    state = StringField(
        "Estado",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )


class PatientUpdateForm(FlaskForm):
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
    birtday = DateField(
        "Fecha de nacimiento",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )
    sex_choices = [
        ("masculino", "Masculino"),
        ("feminino", "Feminino"),
        ("outro", "Outro"),
    ]
    sex = SelectField(
        "Sexo",
        choices=sex_choices,
        validators=[DataRequired("Este campo é obrigatório.")],
    )
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
    reference_telephone = StringField(
        "Telefone de referencia",
        validators=[
            Length(
                min=10, max=15, message="Mínimo 10 caracteres, máximo 14 caracteres"
            ),
            DataRequired("Este campo é obrigatório."),
        ],
    )
    reference_contact = StringField(
        "Contacto de referencia",
        validators=[
            Length(min=3, max=45,
                   message="Mínimo 10 caracteres, máximo 45 caracteres"),
            DataRequired("Este campo é obrigatório."),
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
    marital_status = StringField(
        "Estado civil",
        validators=[
            Length(
                min=3, max=45, message="Mínimo 3 caractere,.Disclaimer 45 caracteres"
            ),
        ],
    )
    profession = StringField(
        "Profesión",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    blood_type_choices = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("AB", "AB"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("nao_sabe", "Nao sabe"),
    ]
    blood_type = SelectField(
        "Tipo sanguíneo",
        choices=blood_type_choices,
        validators=[DataRequired("Este campo é obrigatório.")],
    )
    smoker = BooleanField(
        "Fumante",
    )
    controlled_medicine = StringField(
        "Remedio controlado",
        default="Sem remedio controlado",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )
    consumes_alcohol = BooleanField(
        "Consume Alcohol",
    )
    drug_user = BooleanField(
        "Consume drogas",
    )
    chronic_disease = StringField(
        "Doenças crônicas",
        default="Sem doenças crônicas",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )
    allergies = StringField(
        "Alergias",
        default="Sem alergias",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )

    phone = StringField(
        "phone",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(
                min=10, max=15, message="Mínimo 10 caracteres, máximo 15 caracteres"
            ),
        ],
    )
    address = StringField(
        "Endereço",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    number = StringField(
        "Número",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=10),
        ],
    )
    complement = StringField(
        "Complemento",
        default="Sem complemento",
        validators=[
            Length(min=1, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    neighborhood = StringField(
        "Barrio",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    city = StringField(
        "Ciudad",
        validators=[
            DataRequired("Este campo é obrigatório."),
            Length(min=3, max=45, message="Mínimo 3 caractere, máximo 45 caracteres"),
        ],
    )
    state = StringField(
        "Estado",
        validators=[
            DataRequired("Este campo é obrigatório."),
        ],
    )
