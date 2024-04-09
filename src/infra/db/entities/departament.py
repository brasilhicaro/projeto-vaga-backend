from sqlalchemy import Column, Integer, String
from uuid import uuid4
from src.infra.db.settings import Base

"""
Class responsible for mapping the departament entity
"""
class Departament(Base):
    __tablename__ = 'tb_departament'

    id = Column(String, primary_key=True, default=str(uuid4()))
    name = Column(String, nullable=False)

    """
    Method responsible for returning a string representation of the object
    """
    def __repr__(self) -> str:
        return f'Departament id: {self.id}, name: {self.name}'
    