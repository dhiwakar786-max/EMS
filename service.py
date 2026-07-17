from model import Employee 
import re

class Employee_Controller:
    lis=[]
    addres_lis=[]
    def add_employee(self,emp):
        self.lis.append(emp)
        return self.lis
    def validate_employee_name(self,name):
        pattern=r"[a-zA-Z\s'-]+$"
        if re.match(pattern,name):
            return True
        else:
            return False
   
    def display_employee_details(self):
        if  len(Service.lis)==0:
            return True
        else:
            return False   
    def emp_details(self,choice_id):
        for emp in Service.lis:
                if choice_id==emp.get_emp_id():
                    return emp
                
    def update_employee_details(self,update_id):
        for emp in Service.lis:
                if update_id==emp.get_emp_id():
                     return emp
    def update_employee_name(self,emp,valname):
        if self.checkname(valname):
            emp.set_emp_name(valname)
        return emp                      
    def update_employee_age(self,emp,valage):
        emp.set_emp_age(valage)
        return emp
    def update_employee_salary(self,emp,valsal):
        emp.set_emp_salary(valsal)
        return emp  

    def update_employee_email(self,emp,valemail):
         emp.set_emp_email(valemail) 
         return emp  
    def update_employee_address(self,emp,valadd):
         emp.set_emp_address(valadd)
         return emp
    def delete_employee_detail(self,del_id):
        for emp in Service.lis:
                if del_id==emp.get_emp_id():
                    Service.lis.remove(emp)
                    print( Service.lis)

    def validate_employee_email(self,email):
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern,email):
             return True
        else:
             return False
        
    def validate_employee_age(self,age):
         if age>18 and age<100:
              return True
         else:
              return False
