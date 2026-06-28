class Employee:

    def __init__(self,name,id,age,salary,address):
        self.emp_name   = name
        self.emp_id     = id
        self.emp_age    = age
        self.emp_salary = salary
        self.emp_address = address

    def get_emp_name(self):
        return self.emp_name

    def set_emp_name(self, value):
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

    def get_emp_address(self):
        return self.emp_address
    
    def set_emp_address(self,value):
        self.emp_address = value
       
    def display(self):
        print("Employee name:",self.emp_name)
        print("Emplouee id:",self.emp_id)
        print("Employee age:",self.emp_age)
        print("Employee salary :",self.emp_salary)
        print("Employee address : ",self.emp_address)

class Address:

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