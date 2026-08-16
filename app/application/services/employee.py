"""Employee application service / use cases (stub)."""

# from sqlalchemy.orm import Session

from app.domain.entities.employee import Employee
from app.domain.entities.employeeaddress import EmployeeAddress
from app.presentation.schemas.employee import EmployeeCreateRequest
import random

class EmployeeService:
    def __init__(self) -> None:
        self._db = []

    def list_employees(self,*, skip: int = 0, limit: int = 100) -> list[Employee]:
        print(self._db)
        if len(self._db) == 0:
            return False, self._db
        else:
            return True, self._db

    def get_employee(self, employee_id: int) -> Employee:
        for  emp in self._db:
            print(emp.employee_id,employee_id)
            if emp.employee_id ==  employee_id:
                return True, emp
        return False, None
        

    def generate_emp_id(self):
        id = random.randint(1,20)
        return id

    def create_employee(self, employee: EmployeeCreateRequest) -> Employee:
        name = employee.employee_name
        age = employee.employee_age 
        address = employee.employee_address
        doorno = address.employee_dooorno
        street = address.employee_streetname
        city = address.employee_city
        pincode =address.employee_pincode
        address1 = EmployeeAddress(doorno,street,city,pincode)
        salary = employee.employee_salary 
        email = employee.employee_email
        id = int(self.generate_emp_id())
        employ = Employee(id,name,age,salary,email,address1)
        print(employ)
    
        
        result = self._db.append(employ)
        print(self._db)
        if result == None:
            return True,"Employee Added ",
        else:
            return False,"Employee Not Added"
        

    def update_employee(self, employee_id: int, employee: Employee) -> Employee:
        for emp in self._db:
            if emp.employee_id == employee_id:
                employee = emp
                return 
                


    def delete_employee(self, employee_id: int) -> None:
        print(self._db)
        for emp in self._db:
            print(emp.employee_id,employee_id)
            if emp.employee_id == employee_id:
                self._db.remove(emp)
                return True , "deleted"
        return False , "not deleted"
        
        
