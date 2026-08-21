"""Employee domain entity (stub)."""

from dataclasses import dataclass

from app.domain.entities.employeeaddress import EmployeeAddress


@dataclass
class Employee:
    employee_id: int
    employee_name: str
    employee_age: int
    employee_salary: int
    employee_email: str
    employee_address: EmployeeAddress
