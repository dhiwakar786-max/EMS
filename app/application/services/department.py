"""Department application service / use cases (stub)."""

# from sqlalchemy.orm import Session

from app.domain.entities.department import Department


class DepartmentService:
    def __init__(self) -> None:
        self._db = []

    def list_departments(self, *, skip: int = 0, limit: int = 100) -> list[Department]:
        raise NotImplementedError

    def get_department(self, department_id: int) -> Department:
        raise NotImplementedError

    def create_department(self, department: Department) -> Department:
        raise NotImplementedError

    def update_department(self, department_id: int, department: Department) -> Department:
        raise NotImplementedError

    def delete_department(self, department_id: int) -> None:
        raise NotImplementedError
