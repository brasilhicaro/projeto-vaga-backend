from src.model.entity.Models import Employee
from sqlalchemy.exc import SQLAlchemyError
from src.infra.db.settings.connection import Connection


class EmployeeRepository:

    """
    Class responsible
    for implementing the
    employee repository
    interface
    """

    __postgres_connection: Connection
    def __init__(self) -> None:
        """
        _summary_: Method responsible for initializing the class
        """
        self.__postgres_connection = Connection()
        

    def insert_employee(self, employee: Employee) -> Employee:
        """_summary_:
            Method responsible for inserting a employee into the database

        Args:
            employee (Employee): _description_: Employee object

        Returns:
            Employee: _description_: Employee object
        """
        if employee is None:
            raise ValueError("Employee object cannot be None")

        session = self.__postgres_connection.get_session()

        try:
            with session.begin():
                session.add(employee)
                session.flush()
                session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error inserting employee: {e}")
            raise
        finally:
            session.close()

        return employee
    def select_employee(self, employee_id: str) -> Employee:
        """_summary_: Method responsible for returning a employee from the database

        Args:
            employee_id (str): _description_: Employee id

        Returns:
            Employee: _description_: Employee object
        """
        if employee_id is None:
            raise ValueError("Employee id cannot be None")

        session = self.__postgres_connection.get_session()
        try:
            employee = session.query(Employee).filter(Employee.id == employee_id).first()
            session.close()
            return employee
        except SQLAlchemyError as e:
            session.close()
            print(f"Error selecting employee: {e}")
            raise
        
    def select_all_employees(self) -> list:
        """_summary_:
            Method responsible for returning all employees from the database

        Returns:
            list: List of employee objects
        """
        session = self.__postgres_connection.get_session()
        try:
            employees = session.query(Employee).all()
            session.close()
            return employees
        except SQLAlchemyError as e:
            session.close()
            print(f"Error selecting all employees: {e}")
            raise
        
