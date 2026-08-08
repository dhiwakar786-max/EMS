"""Employee application service / use cases (stub)."""

# from sqlalchemy.orm import Session

from app.domain.entities.employee import Employee


class EmployeeService:
    def __init__(self) -> None:
        self._db = []

    def list_employees(self, *, skip: int = 0, limit: int = 100) -> list[Employee]:
        if len(self._db) == 0:
            return "No Employee Added"
        else:
            return self._db

    def get_employee(self, employee_id: int) -> Employee:
        for  employee in self._db:
            if employee.id ==  employee_id:
                return employee


    def create_employee(self, employee: Employee) -> Employee:
        result = self._db.append(employee)
        if result == None:
            return True,"Employee Added "
        else:
            return False,"Employee Not Added"
        

    def update_employee(self, employee_id: int, employee: Employee) -> Employee:
        for employee in self._db:
            if employee.id == employee_id:
                pass


    def delete_employee(self, employee_id: int) -> None:
        for emp in self._db:
            if emp.id == employee_id:
                self._db.remove(emp)
                return True
        raise Exception("Employee not found")
        
