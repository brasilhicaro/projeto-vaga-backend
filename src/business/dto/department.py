from pydantic import BaseModel

"""
Department DTO
"""


class Department(BaseModel):
    name: str


class DepartmentResponse(Department):

    class Config:
        from_attributes = True
