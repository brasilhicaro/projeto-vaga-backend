from src.model.entity.Models import Department
from sqlalchemy.exc import SQLAlchemyError
from src.infra.db.settings.connection import Connection

class DepartmentRepository:
    """
    Class responsible
    for implementing the
    department repository
    interface
    """
    __postgres_connection: Connection
    
    def __init__(self) -> None:
        """
        _summary_: Method responsible for initializing the class
        """
        self.__postgres_connection = Connection()
        
    def insert_department(self, department: str) -> Department:
        """
        _summary_: Method responsible for inserting a department into the database

        Args:
            department (Department): _description_: Department object

        Returns:
            Department: _description_: Department object
        """
        if department is "":
            raise ValueError("Department object cannot be None")

        session = self.__postgres_connection.get_session()
        
        try:
            with session.begin():
                session.add(department)
                session.flush()
                session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error inserting department: {e}")
            raise
        finally:
            session.close()

        return department
    def select_department(self, department_id: str) -> Department:
        """_summary_: Method responsible for returning a department from the database

        Args:
            department_id (str): _description_: Department id

        Returns:
            Department: _description_: Department object
        """
        if department_id is None:
            raise ValueError("Department id cannot be None")

        session = self.__postgres_connection.get_session()

        try:
            department = session.query(Department).filter(Department.id == department_id).first()
        except SQLAlchemyError as e:
            print(f"Error selecting department: {e}")
            raise
        finally:
            session.close()

        return department

    def select_department_by_name(self, department_name: str) -> str:
        """
        _summary_: 
            Method responsible for returning a department from the database
        args:
            department_name (str): _description_: Department name
        Returns:
            str: _description_: Department id
        """       
        if department_name is None:
            raise ValueError("Department name cannot be None")
        session = self.__postgres_connection.get_session()
        try:
            department = session.query(Department).filter(Department.name == department_name).first()
        except SQLAlchemyError as e:
            print(f"Error selecting department: {e}")
            raise
        finally:
            session.close()
        
    def select_all_department(self) -> list:
        """_summary_: Method responsible for returning all departments from the database

        Returns:
            list: List of department objects
        """
        session = self.__postgres_connection.get_session()

        try:
            departments = session.query(Department).all()
        except SQLAlchemyError as e:
            print(f"Error selecting all departments: {e}")
            raise
        finally:
            session.close()

        return departments