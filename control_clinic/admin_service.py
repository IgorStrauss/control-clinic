from flask_admin import Admin

from control_clinic.models import db
# from control_clinic.models import (Doctor, DoctorPhone, DoctorSpecialty, EmployeePhone,
#                      Employees, Patient, PatientPhone, db)
from control_clinic.models.doctors import Doctor, DoctorPhone, DoctorSpecialty
from control_clinic.models.employees import EmployeePhone, Employees
from control_clinic.models.patients import Patient, PatientPhone

from .admin_views import (DoctorModelView, DoctorPhoneModelView,
                          DoctorSpecialtyModelView, EmployeeModelView,
                          EmployeesPhoneModelView, PatientModelView,
                          PatientPhoneModelView)

admin = Admin()

# Empleados
admin.add_view(EmployeeModelView(
    Employees, db.session, category="Empleados"))
admin.add_view(EmployeesPhoneModelView(
    EmployeePhone, db.session, category="Empleados"))
# Especialidades
admin.add_view(DoctorSpecialtyModelView(
    DoctorSpecialty, db.session, category="Medicos"))
# Medicos
admin.add_view(DoctorModelView(
    Doctor, db.session, category="Medicos"))
admin.add_view(DoctorPhoneModelView(
    DoctorPhone, db.session, category="Medicos"))
# Patients
admin.add_view(PatientModelView(
    Patient, db.session, category="Pacientes"))
admin.add_view(PatientPhoneModelView(
    PatientPhone, db.session, category="Pacientes"))
