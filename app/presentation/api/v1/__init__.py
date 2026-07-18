"""API v1 controllers."""

from fastapi import APIRouter

from app.presentation.api.v1 import departments, employees

api_router = APIRouter()
api_router.include_router(employees.router)
api_router.include_router(departments.router)
