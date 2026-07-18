"""Employee request / response schemas (presentation DTOs — stub)."""

from pydantic import BaseModel 



class EmployeeCreateRequest(BaseModel):
    
    employee_name : str

class EmployeeUpdateRequest(BaseModel):
    pass


class EmployeeResponse(BaseModel):
     # TODO: id, created_at, updated_at, ...
    model_config = {"from_attributes": True}
