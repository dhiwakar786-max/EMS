"""Employee controller / presentation routes (stub)."""
#from app.infrastructure.database
from fastapi import APIRouter, Depends , HTTPException 
from app.application.services.employee import EmployeeService
from app.presentation.dependencies import get_employee_service
from app.presentation.schemas.employee import (
    EmployeeCreateRequest,
    EmployeeResponse,
    EmployeeUpdateRequest,
    EmployeedictResponse,EmployeelistResponse

)

router = APIRouter(prefix="/employees", tags=["employees"])


@router.get("/", response_model=EmployeelistResponse)
def list_employees(
    
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeelistResponse:

    is_done, result = service.list_employees()

    return EmployeelistResponse(is_done=is_done, result=result)

    


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
        

@router.get("/{employee_id}", response_model=EmployeedictResponse)
def get_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeedictResponse:
    is_Created,result = service.get_employee(employee_id)
    return EmployeedictResponse(is_Created=is_Created,message=result)
    #except Exception as e:
        #raise HTTPException(status_code = 404,detail = "Employee not found")
    
   


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    payload: EmployeeUpdateRequest,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    try:
        is_Created, message = service.update_employee(employee_id, payload)
        return EmployeeResponse(is_Created=is_Created, message=message)
    except Exception as e:
        raise HTTPException(status_code=404, detail="employee not found")

   

@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    service: EmployeeService = Depends(get_employee_service),
) -> EmployeeResponse:
    try:
        is_Created , message = service.delete_employee(employee_id)
        return EmployeeResponse(is_Created = is_Created,message = message)
        
    except Exception as e:
        raise HTTPException(status_code = 404,detail = "employee not found")
    
