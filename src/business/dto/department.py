from pydantic import BaseModel

"""
Department DTO
"""


class DepartmentRequest(BaseModel):
    name: str


class DepartmentResponse(DepartmentRequest):

    class Config:
        from_attributes = True