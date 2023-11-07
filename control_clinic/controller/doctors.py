from flask import flash, redirect, render_template, url_for
from werkzeug.security import generate_password_hash

from control_clinic.forms import DoctorForm, DoctorUpdateForm, SpecialtyForm
from control_clinic.models import Doctor, Doctor_phone, Doctor_specialty, db


def init_app(app):
    @app.route("/cadastro/medico", methods=["GET", "POST"], endpoint="register_doctor")
    def register_doctor():
        specialidads = Doctor_specialty.query.all()
        form = DoctorForm()

        if form.validate_on_submit():
            try:
                # Verifique se o email já existe
                existing_doctor = Doctor.query.filter_by(
                    email=form.email.data).first()
                if existing_doctor:
                    flash("Este correo ya estaba registrado.", "error")
                else:
                    doctor = Doctor(
                        firstname=form.firstname.data.upper(),
                        lastname=form.lastname.data.upper(),
                        email=form.email.data,
                        register=form.register.data,
                        password=generate_password_hash(form.password.data),
                        specialty=form.specialty.data,
                    )
                    db.session.add(doctor)
                    db.session.commit()

                    phone = Doctor_phone(
                        phone=form.phone.data,
                        doctor=doctor,
                    )
                    db.session.add(phone)
                    db.session.commit()
                    flash("Médico registrado exitosamente!", "success")
                    return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                for error_message in e.args:
                    print(error_message)
                flash(
                    "Error al intentar registrarme.",
                    "error",
                )
        return render_template(
            "forms/register-doctor.html", specialidads=specialidads, form=form
        )

    @app.route("/listar/medico/<int:id>", endpoint="list_doctor")
    def list_doctor(id):
        doctor = Doctor.query.get_or_404(id)
        return render_template("doctors/list_doctor.html", doctor=doctor)

    @app.route(
        "/atualizar/medico/<int:id>", methods=["GET", "POST"], endpoint="update_doctor"
    )
    def update_doctor(id):
        form = DoctorUpdateForm()
        doctor = Doctor.query.get_or_404(id)
        doctor_phone = doctor.phone
        doctor_specialty = doctor.specialty
        specialidads = Doctor_specialty.query.all()

        if form.validate_on_submit():
            if form.firstname.data:
                doctor.firstname = form.firstname.data.upper()
            if form.lastname.data:
                doctor.lastname = form.lastname.data.upper()
            if form.email.data:
                doctor.email = form.email.data
            if form.register.data:
                doctor.register = form.register.data

            # Atualize a especialidade do médico se um novo valor for selecionado no formulário
            if form.specialty.data:
                doctor.specialty = form.specialty.data

            # Atualize o número de telefone se um novo número for fornecido no formulário
            if form.phone.data:
                doctor_phone.phone = form.phone.data

            db.session.commit()
            flash("Dados do médico atualizados com sucesso", "success")
            return redirect(url_for("list_doctor", id=id))

        form.firstname.data = doctor.firstname
        form.lastname.data = doctor.lastname
        form.email.data = doctor.email
        form.register.data = doctor.register

        # Preenche o campo de especialidade com o valor atual
        form.specialty.data = doctor_specialty

        # Preenche o campo de telefone com o número de telefone atual
        if doctor_phone:
            form.phone.data = doctor_phone.phone

        return render_template(
            "doctors/update_doctor.html",
            form=form,
            doctor=doctor,
            doctor_phone=doctor_phone,
            doctor_specialty=doctor_specialty,
            specialidads=specialidads,
        )

    @app.route("/listar/medicos", endpoint="list_doctors")
    def list_medicos():
        doctors = Doctor.query.all()
        return render_template("doctors/list_doctors.html", doctors=doctors)

    @app.route(
        "/cadastro/especialidade",
        methods=["GET", "POST"],
        endpoint="register_specialty",
    )
    def register_specialty():
        form = SpecialtyForm()
        if form.validate_on_submit():
            try:
                existing_specialty = Doctor_specialty.query.filter_by(
                    name=form.name.data
                ).first()
                if existing_specialty:
                    flash("La especialidad ya existe.", "error")
                else:
                    specialty = Doctor_specialty(
                        name=form.name.data.upper(),
                    )
                    print(form.name.data)
                    db.session.add(specialty)
                    db.session.commit()
                    flash("Especialidad registrada con éxito!", "success")
                    return redirect(url_for("index"))
            except Exception as e:
                db.session.rollback()
                for error_message in e.args:
                    print(error_message)
                flash(
                    "Error al intentar registrarme.",
                    "error",
                )

        return render_template("forms/register-specialty.html", form=form)
