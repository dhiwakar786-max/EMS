"""Employee controller / presentation routes (stub)."""
from app.infrastructure.database.
from fastapi import APIRouter, Depends

from app.application.services.employee import EmployeeService
from app.presentation.dependencies import get_employee_service
from app.presentation.schemas.employee import (
    EmployeeCreateRequest,
    EmployeeResponse,
    EmployeeUpdateRequest,
)

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/", response_model=list[EmployeeResponse])
def list_employees(
    skip: int = 0,
    limit: int = 100,
    service: EmployeeService = Depends(get_employee_service),
) -> list[EmployeeResponse]:
    return service.list_employees(skip = skip,limit = limit)


@router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(
    payload: EmployeeCreateRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    try:
        employee = service.create_employee(payload)
        return employee
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e0))
      
        

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    try:
        employee = service.get_employee(employee_id)
        return employee
    except Exception as e:
        raise HTTPException(status_code = 404,detail = "Employee not found)
    
   


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    payload: EmployeeUpdateRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    try:
        employee = service.update_employee(employee_id,payload)
        return employee
    except Exception as e:
        raise HTTPException(status_code = 404,detail ="employee not found")

   

@router.delete("/{employee_id}", status_code=204)
def delete_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service),
) -> None:
    try:
        success = service.delete_employee(employee_id)
        return None
    except Exception as e:
        raise HTTPException(status_code = 404,detail = "employee not found")
    
