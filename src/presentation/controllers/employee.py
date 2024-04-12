from typing import List

from fastapi import APIRouter, HTTPException

from src.business.services.employee import EmployeeService
from src.business.dto.employee import EmployeeRequest, EmployeeResponse

router = APIRouter()


@router.get("/", response_model=List[EmployeeResponse], status_code=200)
async def get_employees():
    try:
        employee_service = EmployeeService()
        employees_list = employee_service.list_employees()
        
        if not employees_list:
            return []
        
        return {"employees": [employee.dict() for employee in employees_list]}
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)


@router.post("/", response_model=EmployeeResponse, status_code=201)
async def create_employee(employee: EmployeeRequest):
    try:
        employee_service = EmployeeService()
        employer_response = employee_service.create_employee(employee)
        if employer_response == None:
            raise HTTPException(status_code=400, detail="Invalid employee")
        return employer_response.dict()
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)