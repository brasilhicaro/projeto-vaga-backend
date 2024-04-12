from uuid import uuid4

from sqlalchemy import String, Column, ForeignKey, Integer 
from sqlalchemy.ext.declarative import declarative_base



def generate_uuid()->str:
    return str(uuid4())

Base = declarative_base()

class Department(Base):
    """
    Class responsible for representing the department entity
    """
    __tablename__ = "tb_department"
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)

    def __init__(self, name: str) -> None:
        """
        _summary_:
            Method responsible for returning a string representation of the object
        
        args:
            name (str): Department name 
        
        Returns:
            None
        """
        self.name = name
    
    def __repr__(self) -> str:
        """_summary_: Method responsible for returning a string representation of the object

        Returns:
            str: _description_ : Department id: {self.id}, name: {self.name}
        """
        return f"Departament id: {self.id}, name: {self.name}"

class Employee(Base):
    """class responsible for representing the employee entity"""

    __tablename__ = "tb_employee"
    
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String, nullable=False)
    department_id = Column(String, ForeignKey("tb_department.id"), nullable=False)
    dependents = Column(Integer, nullable=False, default=0)


    def __init__(self, name: str, department_id: str, dependents: int) -> None:
        """
        _summary_

        Args:
            name (str): name of the employee
            department_id (str): Foreign key of the department
            dependents (int): Quantity of dependents
        """
        self.name = name
        self.department_id = department_id
        self.dependents = dependents

    def __repr__(self) -> str:
        """_summary_: Method responsible for returning a string representation of the object

        Returns:
            str: _description_ : Employeer id: {self.id}, name: {self.name}, department_id: {self.department_id}, dependents: {self.dependents}
        """
        return f"Employeer id: {self.id}, name: {self.name}, department_id: {self.department_id}, dependents: {self.dependents}"