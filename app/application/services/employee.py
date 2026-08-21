"""Employee application service — DB-backed create / list / get / delete."""

from sqlalchemy.orm import Session

from app.domain.entities.employee import Employee
from app.domain.entities.employeeaddress import EmployeeAddress
from app.infrastructure.models.employee import EmployeeModel
from app.presentation.schemas.employee import EmployeeCreateRequest


class EmployeeService:
    def __init__(self, db: Session) -> None:
        self._db = db

    def list_employees(self, *, skip: int = 0, limit: int = 100):
        rows = self._db.query(EmployeeModel).offset(skip).limit(limit).all()
        employees = [self._to_entity(row) for row in rows]
        if len(employees) == 0:
            return False, employees
        return True, employees

    def get_employee(self, employee_id: int):
        row = self._db.query(EmployeeModel).filter(EmployeeModel.emp_id == employee_id).first()
        if row is None:
            return False, None
        return True, self._to_entity(row)

    def generate_emp_id(self):
        # kept for trainee compatibility; DB uses autoincrement instead
        return None

    def create_employee(self, employee: EmployeeCreateRequest):
        address = employee.employee_address
        row = EmployeeModel(
            emp_name=employee.employee_name,
            emp_age=employee.employee_age,
            emp_salary=employee.employee_salary,
            emp_email=employee.employee_email,
            emp_doorno=address.employee_dooorno,
            emp_street=address.employee_streetname,
            emp_city=address.employee_city,
            emp_pincode=address.employee_pincode,
        )
        self._db.add(row)
        self._db.commit()
        self._db.refresh(row)
        return True, "Employee Added "

    def update_employee(self, employee_id: int, employee):
        row = self._db.query(EmployeeModel).filter(EmployeeModel.emp_id == employee_id).first()
        if row is None:
            raise ValueError("employee not found")

        row.emp_name = employee.employee_name
        row.emp_age = employee.employee_age
        row.emp_salary = employee.employee_salary
        row.emp_email = employee.employee_email

        addr = employee.employee_address
        # update schema uses employee_doorno (one 'o'); create uses employee_dooorno
        row.emp_doorno = getattr(addr, "employee_doorno", None) or getattr(addr, "employee_dooorno")
        row.emp_street = addr.employee_streetname
        row.emp_city = addr.employee_city
        row.emp_pincode = addr.employee_pincode

        self._db.commit()
        self._db.refresh(row)
        return True, "Employee Updated "

    def delete_employee(self, employee_id: int):
        row = self._db.query(EmployeeModel).filter(EmployeeModel.emp_id == employee_id).first()
        if row is None:
            return False, "not deleted"
        self._db.delete(row)
        self._db.commit()
        return True, "deleted"

    def _to_entity(self, row: EmployeeModel) -> Employee:
        address = EmployeeAddress(
            row.emp_doorno,
            row.emp_street,
            row.emp_city,
            row.emp_pincode,
        )
        return Employee(
            row.emp_id,
            row.emp_name,
            row.emp_age,
            row.emp_salary,
            row.emp_email,
            address,
        )
