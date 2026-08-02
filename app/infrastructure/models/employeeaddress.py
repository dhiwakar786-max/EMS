from app.infrastructure.database.base import Base


class EmployeeAddressModel(Base):
    __tablename__ = "employees"

    def __init__(self,doorno,street,city,pincode):
        self.emp_doorno = doorno
        self.emp_street = street
        self.emp_city = city
        self.emp_pincode = pincode

    def get_emp_doorno(self):
        return self.emp_doorno
    
    def set_emp_doorno(self,value):
        self.emp_doorno = value

    def get_emp_street(self):
        return self.emp_street
    
    def set_emp_street(self,value):
        self.emp_street = value

    def get_emp_city(self):
        return self.emp_city
    
    def set_emp_city(self,value):
        self.emp_city = value

    def get_emp_pincode(self):
        return self.emp_pincode
    
    def set_emp_pincode(self,value):
        self.emp_pincode = value