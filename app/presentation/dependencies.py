"""Presentation dependencies — wire DB session and application services."""

from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.services.department import DepartmentService
from app.application.services.employee import EmployeeService
from app.infrastructure.database.session import get_db


# def get_database() -> Generator[Session, None, None]:
#     yield from get_db()

employeeService =  EmployeeService()
def get_employee_service() -> EmployeeService:
    return employeeService


def get_department_service() -> DepartmentService:
    return DepartmentService()
