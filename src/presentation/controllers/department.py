
from typing import List

from fastapi import APIRouter, HTTPException

from src.business.services.department import DepartmentService
from src.business.dto.department import Department, DepartmentResponse


router = APIRouter()


@router.get("/", response_model=List[DepartmentResponse], status_code=200)
async def get_departments():
    try:
        department_service = DepartmentService()
        departments_list = department_service.list_departments()
        return {"departments": [department.dict() for department in departments_list]}
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)


@router.post("/", response_model=DepartmentResponse, status_code=201)
async def create_department(payload: Department) -> DepartmentResponse:
    try:
        department_service = DepartmentService()
        department = department_service.create_department(payload)
        return DepartmentResponse.model_validate(department)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
