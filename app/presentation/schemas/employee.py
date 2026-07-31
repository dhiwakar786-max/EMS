"""Employee request / response schemas (presentation DTOs — stub)."""
from uuid import UUID
from employeeaddress import EmployeeAddress
from pydantic import BaseModel , Field



class EmployeeCreateRequest(BaseModel):
    
   
    employee_name : str = Field(..., min_length = 1)
    employee_age : int = Field(..., ge = 0)
    employee_salary : int = Field(..., ge = 0)  
    employee_email : str = Field(..., min_length =1)
    employee_address : EmployeeAddress


class EmployeeUpdateRequest(BaseModel):
    employee_name : str
    employee_age : int
    employee_salary : int
    employee_email : str
    employee_address : EmployeeAddress


class EmployeeResponse(BaseModel):
     
    model_config = {"from_attributes": True}

    employee_id : UUID
    employee_name : str
    employee_age : int
    employee_salary : int
    employee_email : str
    employee_address : EmployeeAddress

    
