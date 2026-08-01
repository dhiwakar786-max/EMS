"""Employee application service / use cases (stub)."""

# from sqlalchemy.orm import Session

from app.domain.entities.employee import Employee


class EmployeeService:
    def __init__(self) -> None:
        self._db = []

    def list_employees(self, *, skip: int = 0, limit: int = 100) -> list[Employee]:
        pass

    def get_employee(self, employee_id: int) -> Employee:
        for  employee in self._db:
            if employee ==  employee_id:
                return employee  

    def create_employee(self, employee: Employee) -> Employee:
        if self._db.append(employee):
            return True
        else:
            return False

    def update_employee(self, employee_id: int, employee: Employee) -> Employee:
        raise NotImplementedError

    def delete_employee(self, employee_id: int) -> None:
        raise NotImplementedError
