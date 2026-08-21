"""Employee ORM model — DB mapping for trainee employee fields."""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database.base import Base


class EmployeeModel(Base):
    __tablename__ = "employees"

    emp_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    emp_name: Mapped[str] = mapped_column(String(255), nullable=False)
    emp_age: Mapped[int] = mapped_column(Integer, nullable=False)
    emp_salary: Mapped[int] = mapped_column(Integer, nullable=False)
    emp_email: Mapped[str] = mapped_column(String(255), nullable=False)

    # address (trainee field names)
    emp_doorno: Mapped[int] = mapped_column(Integer, nullable=False)
    emp_street: Mapped[str] = mapped_column(String(255), nullable=False)
    emp_city: Mapped[str] = mapped_column(String(255), nullable=False)
    emp_pincode: Mapped[int] = mapped_column(Integer, nullable=False)

    def get_emp_name(self):
        return self.emp_name

    def set_emp_name(self, value):
        self.emp_name = value

    def get_emp_id(self):
        return self.emp_id

    def set_emp_id(self, value):
        self.emp_id = value

    def get_emp_age(self):
        return self.emp_age

    def set_emp_age(self, value):
        self.emp_age = value

    def get_emp_salary(self):
        return self.emp_salary

    def set_emp_salary(self, value):
        self.emp_salary = value

    def get_emp_email(self):
        return self.emp_email

    def set_emp_email(self, value):
        self.emp_email = value

    def get_emp_address(self):
        return {
            "emp_doorno": self.emp_doorno,
            "emp_street": self.emp_street,
            "emp_city": self.emp_city,
            "emp_pincode": self.emp_pincode,
        }

    def set_emp_address(self, value):
        self.emp_doorno = value.emp_doorno if hasattr(value, "emp_doorno") else value.get("emp_doorno")
        self.emp_street = value.emp_street if hasattr(value, "emp_street") else value.get("emp_street")
        self.emp_city = value.emp_city if hasattr(value, "emp_city") else value.get("emp_city")
        self.emp_pincode = value.emp_pincode if hasattr(value, "emp_pincode") else value.get("emp_pincode")
