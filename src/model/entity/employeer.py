from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from uuid import uuid4

"""
Class responsible for mapping the employeer entity
"""
class Employeer(declarative_base()):
    __tablename__ = 'tb_employeer'

    id = Column(String, primary_key=True, default=str(uuid4()))
    name = Column(String, nullable=False)
    departament_id = Column(String, nullable=False)
    dependents = Column(Integer, nullable=False)

    """
    Method responsible for returning a string representation of the object
    """
    def __repr__(self) -> str:
        return f'Employeer id: {self.id}, name: {self.name}, departament_id: {self.departament_id}, dependents: {self.dependents}'