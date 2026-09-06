"""Department request / response schemas (presentation DTOs — stub)."""

from pydantic import BaseModel


class DepartmentCreateRequest(BaseModel):
    # TODO: name, description, manager_id
    pass


class DepartmentUpdateRequest(BaseModel):
    pass


class DepartmentResponse(BaseModel):
    # TODO: id, created_at, updated_at, ...
    model_config = {"from_attributes": True}

'''project entities - project name ,id,list(employee 
project create ,update,delete,response
in create ,add employees by their id 
in update, employees update their project details
in delete , delete an  employee, and delete an project
create request - routers - service - created project - add employeesto the project-store in list of project - response as created
get request - routers - service - get project by their id in list - shows the employees in theproject and project status-response 
update request - routers - service - project id - employee id - update the details - response
delete request - routers - service - project id - delete proj - employee id - del employee - response
'''
