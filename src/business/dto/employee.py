from pydantic import BaseModel
from typing import List



class Employee(BaseModel):
    name: str
    department_id: str
    dependents: int


class EmployeeResponse(Employee):
    id: str
    have_dependents: bool

    class Config:
        orm_mode = True