
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from uuid import uuid4

"""
Class responsible for mapping the department entity
"""

class Department(declarative_base()):
    __tablename__ = "tb_department"

    id = Column(String, primary_key=True, default=str(uuid4()))
    name = Column(String, nullable=False)

    """
        Method responsible for returning a string representation of the object
        """

    def __repr__(self) -> str:
        return f"Departament id: {self.id}, name: {self.name}"
