"""Employee ORM model (stub)."""

from app.infrastructure.database.base import Base


class EmployeeModel(Base):
    __tablename__ = "employees"
    # TODO: colu
    def __init__(self,id : int,emp_name : str):
        self.id = id
        self.emp_name = emp_name

    def get_name(self,emp_name):
        return self.emp_name

    def set_name(self,value:str):
        self.emp_name = value
