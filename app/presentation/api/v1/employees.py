"""Employee controller / presentation routes (stub)."""

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
    raise NotImplementedError


@router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(
    payload: EmployeeCreateRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    raise NotImplementedError
        

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    raise NotImplementedError


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    payload: EmployeeUpdateRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    raise NotImplementedError


@router.delete("/{employee_id}", status_code=204)
def delete_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service),
) -> None:
    raise NotImplementedError
