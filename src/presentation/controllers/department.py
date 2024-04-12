
from typing import List

from fastapi import APIRouter, HTTPException

from src.business.services.department import DepartmentService
from src.business.dto.department import DepartmentRequest, DepartmentResponse


router = APIRouter()

@router.get("/", response_model=List[DepartmentResponse], status_code=200)
async def get_departments():
    try:
        department_service = DepartmentService()
        departments_dict = department_service.list_departments()
        
        if not departments_dict:
            return []
        
        departments_list = [department.dict() for department in departments_dict.values()]
        
        return departments_list
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)



@router.post("/", response_model=DepartmentResponse, status_code=201)
async def create_department(payload: DepartmentRequest) -> DepartmentResponse:
    try:
        department_service = DepartmentService()
        department = department_service.create_department(payload)
        return DepartmentResponse.model_validate(department)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)
