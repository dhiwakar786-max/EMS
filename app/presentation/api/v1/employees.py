"""Employee controller / presentation routes (stub)."""
#from app.infrastructure.database
from fastapi import APIRouter, Depends , HTTPException 
from app.application.services.employee import EmployeeService
from app.presentation.dependencies import get_employee_service
from app.presentation.schemas.employee import (
    EmployeeCreateRequest,
    EmployeeResponse,
    EmployeeUpdateRequest,EmployeelistResponse

)

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/", response_model=EmployeelistResponse)
def list_employees(
    skip: int = 0,
    limit: int = 100,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeelistResponse:

    is_done,result =service.list_employees(skip = skip,limit = limit)

    return EmployeelistResponse(is_done=is_done, message="sample" ,result= result)

    


@router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(
    payload: EmployeeCreateRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    try:
        is_Created, message  = service.create_employee(payload)
        print(EmployeeService)
        return  EmployeeResponse(is_Created=is_Created, message=message)
        
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))
      

    return EmployeelistRes
        

@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    try:
        employee = service.get_employee(employee_id)
        return employee
    except Exception as e:
        raise HTTPException(status_code = 404,detail = "Employee not found")
    
   


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
        is_Created,message = service.delete_employee(employee_id)
        return EmployeeResponse(is_Created = is_Created,message = message)
        
    except Exception as e:
        raise HTTPException(status_code = 404,detail = "employee not found")
    
