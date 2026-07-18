"""Employee domain entity (stub)."""
from uuid import UUID
from dataclasses import dataclass


@dataclass
class Employee:

    employee_id : UUID
    employee_name : str
    employee_age : int
    employee_salary : int
    employee_email : str
    employee_address : str

