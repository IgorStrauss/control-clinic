from datetime import datetime

from flask_login import UserMixin

from . import db


class Employees(db.Model, UserMixin):
    __tablename__ = "employee"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime, default=datetime.now, server_default=db.func.now()
    )
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.now, server_default=db.func.now()
    )
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(64), nullable=False)
    phone = db.relationship(
        "Employee_phone", backref="employee", uselist=False)

    def __str__(self):
        return self.firstname


class Employee_phone(db.Model):
    __tablename__ = "employee_phone"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(14), default=000)
    employee_id = db.Column(db.ForeignKey("employee.id"), nullable=False)

    def __str__(self):
        return self.phone

    @property
    def format_employee_phone(self):
        return f"({self.phone[:3]}) {self.phone[3:7]}-{self.phone[7:]}"
