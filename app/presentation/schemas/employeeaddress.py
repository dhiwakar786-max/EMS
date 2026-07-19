
from pydantic import BaseModel , Field


class EmployeeAddress(BaseModel):

    employee_dooorno : int = Field(...,ge = 0)
    employee_streetname : str = Field(...,min_length = 1)
    employee_city : str = Field(...,min_length = 1)
    employee_pincode : int = Field(...,ge = 0)