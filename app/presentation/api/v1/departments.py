"""Department controller / presentation routes (stub)."""

from fastapi import APIRouter, Depends

from app.application.services.department import DepartmentService
from app.presentation.dependencies import get_department_service
from app.presentation.schemas.department import (
    DepartmentCreateRequest,
    DepartmentResponse,
    DepartmentUpdateRequest,
)

router = APIRouter(prefix="/departments", tags=["departments"])


@router.get("/", response_model=list[DepartmentResponse])
def list_departments(
    skip: int = 0,
    limit: int = 100,
    service: DepartmentService = Depends(get_department_service),
) -> list[DepartmentResponse]:
    raise NotImplementedError


@router.post("/", response_model=DepartmentResponse, status_code=201)
def create_department(
    payload: DepartmentCreateRequest,
    service: DepartmentService = Depends(get_department_service),
) -> DepartmentResponse:
    raise NotImplementedError


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department(
    department_id: int,
    service: DepartmentService = Depends(get_department_service),
) -> DepartmentResponse:
    raise NotImplementedError


@router.put("/{department_id}", response_model=DepartmentResponse)
def update_department(
    department_id: int,
    payload: DepartmentUpdateRequest,
    service: DepartmentService = Depends(get_department_service),
) -> DepartmentResponse:
    raise NotImplementedError


@router.delete("/{department_id}", status_code=204)
def delete_department(
    department_id: int,
    service: DepartmentService = Depends(get_department_service),
) -> None:
    raise NotImplementedError
