from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    department_id: str
    dependents: int


class EmployeeResponse(BaseModel):
    name: str
    have_dependents: bool

    class Config:
        from_attributes = True
