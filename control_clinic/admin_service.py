from flask_admin import Admin

from .admin_views import (DoctorModelView, DoctorPhoneModelView,
                          DoctorSpecialtyModelView, EmployeeModelView,
                          EmployeesPhoneModelView, PatientModelView,
                          PatientPhoneModelView)
from .models import (Doctor, Doctor_phone, Doctor_specialty, Employee_phone,
                     Employees, Patient, Patient_phone, db)

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
