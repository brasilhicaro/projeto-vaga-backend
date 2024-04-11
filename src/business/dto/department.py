from pydantic import BaseModel

"""
Department DTO
"""
class Department(BaseModel):
    name: str


class DepartmentResponse(Department):
    id: str

    class Config:
        orm_mode = True