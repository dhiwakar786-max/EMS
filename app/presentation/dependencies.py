"""Presentation dependencies — wire DB session and application services."""

from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.services.department import DepartmentService
from app.application.services.employee import EmployeeService
from app.infrastructure.database.session import get_db


def get_database() -> Generator[Session, None, None]:
    yield from get_db()


def get_employee_service(db: Session = Depends(get_database)) -> EmployeeService:
    return EmployeeService(db)


def get_department_service(db: Session = Depends(get_database)) -> DepartmentService:
    return DepartmentService(db)
