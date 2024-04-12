from pydantic import BaseModel

"""
Department DTO
"""


class DepartmentRequest(BaseModel):
    name: str


class DepartmentResponse(BaseModel):
    name: str
    class Config:
        from_attributes = True