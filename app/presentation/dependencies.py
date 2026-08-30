"""Presentation dependencies — wire DB session and application services."""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.application.services.department import DepartmentService
from app.application.services.employee import EmployeeService
from app.infrastructure.database.session import get_db


def get_employee_service(db: Session = Depends(get_db)) -> EmployeeService:
    return EmployeeService(db)


def get_department_service() -> DepartmentService:
    return DepartmentService()
    
