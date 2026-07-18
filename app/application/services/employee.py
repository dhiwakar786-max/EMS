"""Employee application service / use cases (stub)."""

from sqlalchemy.orm import Session

from app.domain.entities.employee import Employee


class EmployeeService:
    def __init__(self, db: Session) -> None:
        self._db = db

    def list_employees(self, *, skip: int = 0, limit: int = 100) -> list[Employee]:
        raise NotImplementedError

    def get_employee(self, employee_id: int) -> Employee:
        raise NotImplementedError

    def create_employee(self, employee: Employee) -> Employee:
        raise NotImplementedError

    def update_employee(self, employee_id: int, employee: Employee) -> Employee:
        raise NotImplementedError

    def delete_employee(self, employee_id: int) -> None:
        raise NotImplementedError
