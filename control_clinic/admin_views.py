from flask_admin.contrib.sqla import ModelView


class EmployeeModelView(ModelView):
    column_list = [
        "id",
        "firstname",
        "lastname",
        "email",
        "created_at",
        "updated_at",
        "is_active",
        "is_admin",
    ]
    column_searchable_list = ["id", "firstname", "lastname", "email"]
    column_labels = {
        "id": "ID",
        "firstname": "Primer nombre",
        "lastname": "Apellido",
        "email": "E-mail",
        "created_at": "Fecha de creación",
        "updated_at": "Fecha de actualización",
        "is_active": "Activo",
        "is_admin": "Administrador",
    }
    form_excluded_columns = ["password"]


class EmployeesPhoneModelView(ModelView):
    column_list = ["phone", "employee_id"]
    column_searchable_list = ["phone"]
    column_labels = {
        "phone": "Teléfono",
        "employee_id": "Empleado",
    }


class DoctorModelView(ModelView):
    column_list = [
        "id",
        "firstname",
        "lastname",
        "register",
        "email",
        "specialty",
        "created_at",
        "updated_at",
        "is_active",
        "is_admin",
    ]
    column_searchable_list = ["id", "firstname", "register", "email"]
    column_labels = {
        "id": "ID",
        "firstname": "Primer nombre",
        "lastname": "Apellido",
        "email": "E-mail",
        "created_at": "Fecha de creación",
        "updated_at": "Fecha de actualización",
        "register": "Registro",
        "specialty": "Especialidad",
        "is_active": "Activo",
        "is_admin": "Administrador",
    }
    form_excluded_columns = ["password"]


class DoctorPhoneModelView(ModelView):
    column_list = ["phone", "doctor_id"]
    column_searchable_list = ["phone"]
    column_labels = {
        "phone": "Teléfono",
        "doctor_id": "Doctor",
    }


class DoctorSpecialtyModelView(ModelView):
    column_list = ["name"]
    column_searchable_list = ["name"]
    column_labels = {
        "name": "Especialidad",
    }


class PatientModelView(ModelView):
    column_list = [
        "id",
        "firstname",
        "lastname",
        "birtday",
        "sex",
        "name_father",
        "name_mather",
        "document",
        "email",
        "created_at",
        "updated_at",
    ]
    column_searchable_list = ["id", "document", "email"]
    column_labels = {
        "id": "ID",
        "firstname": "Primer nombre",
        "lastname": "Apellido",
        "birtday": "Fecha de nacimiento",
        "sex": "Sexo",
        "name_father": "Apellido paterno",
        "name_mather": "Apellido materno",
        "document": "Documento",
        "email": "E-mail",
        "created_at": "Fecha de creación",
        "updated_at": "Fecha de actualización",
    }


class PatientPhoneModelView(ModelView):
    column_list = ["phone", "patient_id"]
    column_searchable_list = ["phone"]
    column_labels = {
        "phone": "Teléfono",
        "patient_id": "Paciente",
    }
