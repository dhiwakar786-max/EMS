from model import Employee 

class Service:
    lis=[]
    addres_lis=[]
    def create(self,emp):
        self.lis.append(emp)
        return self.lis
   
    def display(self):
        if  len(Service.lis)==0:
            return True
        else:
            return False   
    def emp_details(self,choice_id):
        for emp in Service.lis:
                if choice_id==emp.get_emp_id():
                    return emp
                
    def update_details(self,update_id):
        for emp in Service.lis:
                if update_id==emp.get_emp_id():
                     return emp
    def update_name(self,emp,valname):
        emp.set_emp_name(valname)
        return emp                      
    def update_age(self,emp,valage):
        emp.set_emp_age(valage)
        return emp
    def update_salary(self,emp,valsal):
        emp.set_emp_salary(valsal)
        return emp      
    def update_address(self,emp,valadd):
         emp.set_emp_address(valadd)
         return emp
    def delete(self,del_id):
        for emp in Service.lis:
                if del_id==emp.get_emp_id():
                    Service.lis.remove(emp)
                    print( Service.lis)
 