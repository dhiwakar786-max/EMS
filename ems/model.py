class Employee:

    def __init__(self,name,id,age,salary):
        self.emp_name   = name
        self.emp_id     = id
        self.emp_age    = age
        self.emp_salary = salary

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

       
    def display(self):
        print("Employee name:",self.emp_name)
        print("Emplouee id:",self.emp_id)
        print("Employee age:",self.emp_age)
        print("Employee salary :",self.emp_salary)