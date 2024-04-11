from typing import List

from fastapi import APIRouter, HTTPException

from src.business.services.employee import EmployeeService
from src.business.dto.employee import Employee, EmployeeResponse

router = APIRouter()


@router.get("/", response_model=List[EmployeeResponse], status_code=200)
async def get_employees():
    try:
        employee_service = EmployeeService()
        employees_list = employee_service.list_employees()
        return {"employees": [employee.dict() for employee in employees_list]}
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)


@router.post("/", response_model=EmployeeResponse, status_code=201)
async def create_employee(payload: Employee) -> EmployeeResponse:
    try:
        employee_service = EmployeeService()
        employee = employee_service.create_employee(payload)
        return EmployeeResponse.model_validate(employee)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)