"""Employee application service / use cases (stub)."""

# from sqlalchemy.orm import Session

from app.domain.entities.employee import Employee


class EmployeeService:
    def __init__(self) -> None:
        self._db = []

    def list_employees(self,*, skip: int = 0, limit: int = 100) -> list[Employee]:
        if len(self._db) == 0:
            return False, self._db
        else:
            return True, self._db

    def get_employee(self, employee_id: int) -> Employee:
        for  employee in self._db:
            if employee.id ==  employee_id:
                return employee


    def create_employee(self, employee: Employee) -> Employee:
        employee.employee_name = name
        employee.employee_age = age
        employee.employee_address = address
        employee.employee_salary = salary
        employee.employee_email = email
        employ = (name,age,address,salary,email)
        print(employ)
        result = self._db.append(employ)
        print(self._db)
        if result == None:
            return True,"Employee Added ",
        else:
            return False,"Employee Not Added"
        

    def update_employee(self, employee_id: int, employee: Employee) -> Employee:
        for emp in self._db:
            if emp.id == employee_id:
                return employee
                


    def delete_employee(self, employee_id: int) -> None:
        for emp in self._db:
            if emp.id == employee_id:
                self._db.remove(emp)
                return True
        raise Exception("Employee not found")
        
