"""Employee request / response schemas (presentation DTOs — stub)."""
from uuid import UUID
from  app.presentation.schemas.employeeaddress import EmployeeAddress , EmployeeAddressUpdateRequest
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
    employee_address : EmployeeAddressUpdateRequest


class EmployeeResponse(BaseModel):
    is_Created : bool
    message : str

    # def __init__(self,is_Created : bool,message : int):

    #     self.is_Created = is_Created 
    #     self.message = message

    # def get_is_Created(self):
    #     return self.is_Created

    # def set_is_Created(self,value):
    #     self.is_created = value

    # def get_message(self):
    #     return self.message    
    
    # def set_message(self, value):
    #     self.message = value