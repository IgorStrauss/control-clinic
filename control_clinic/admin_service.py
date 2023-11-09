from flask_admin import Admin

from control_clinic.models import db
# from control_clinic.models import (Doctor, Doctor_phone, Doctor_specialty, Employee_phone,
#                      Employees, Patient, Patient_phone, db)
from control_clinic.models.doctors import (Doctor, Doctor_phone,
                                           Doctor_specialty)
from control_clinic.models.employees import Employee_phone, Employees
from control_clinic.models.patients import Patient, Patient_phone

from .admin_views import (DoctorModelView, DoctorPhoneModelView,
                          DoctorSpecialtyModelView, EmployeeModelView,
                          EmployeesPhoneModelView, PatientModelView,
                          PatientPhoneModelView)

admin = Admin()

# Empleados
admin.add_view(EmployeeModelView(
    Employees, db.session, category="Empleados"))
admin.add_view(EmployeesPhoneModelView(
    Employee_phone, db.session, category="Empleados"))
# Especialidades
admin.add_view(DoctorSpecialtyModelView(
    Doctor_specialty, db.session, category="Medicos"))
# Medicos
admin.add_view(DoctorModelView(
    Doctor, db.session, category="Medicos"))
admin.add_view(DoctorPhoneModelView(
    Doctor_phone, db.session, category="Medicos"))
# Patients
admin.add_view(PatientModelView(
    Patient, db.session, category="Pacientes"))
admin.add_view(PatientPhoneModelView(
    Patient_phone, db.session, category="Pacientes"))
