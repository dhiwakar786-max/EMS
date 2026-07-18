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
