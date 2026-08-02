"""Employee ORM model (stub)."""

from app.infrastructure.database.base import Base
from app.infrastructure.models.employeeaddress import EmployeeAddressModel

class EmployeeModel(Base):
    __tablename__ = "employees"
    # TODO: colu
    def __init__(self,id,name,age,salary,email,address):
        
        self.emp_id     = id
        self.emp_name   = name
        self.emp_age    = age
        self.emp_salary = salary
        self.emp_email = email
        self.emp_address = address

    def get_emp_name(self):
        return self.emp_name

    def set_emp_name(self,value):
        self.emp_name = value

    def get_emp_id(self):
        return self.emp_id

    def set_emp_id(self, value):
        self.emp_id = value

    def get_emp_age(self):
        return self.emp_age

    def set_emp_age(self, value):
        self.emp_age = value

    def get_emp_salary(self):
        return self.emp_salary

    def set_emp_salary(self, value):
        self.emp_salary = value

    def get_emp_email(self):
        return self.emp_email
    
    def set_emp_email(self,value):
        self.emp_email = value

    def get_emp_address(self):
        return self.emp_address
    
    def set_emp_address(self,value):
        self.emp_address = value



