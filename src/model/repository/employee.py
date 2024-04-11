from src.model.entity.employee import Employee
from src.infra.db.settings.connection import Connection

"""
Class responsible
for implementing the
employee repository
interface
"""


class EmployeeRepository:

    def insert_employee(self, employee: Employee) -> Employee:
        """
        Method responsible for inserting a employee in the database
        """
        with Connection() as conn:
            try:
                conn.session.add(employee)
                conn.session.commit()
                return employee
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def select_employee(self, employee_id: str) -> Employee:
        """
        Method responsible for returning a employee from the database
        """
        with Connection() as conn:
            try:
                return (
                    conn.session.query(Employee)
                    .filter(Employee.id == employee_id)
                    .first()
                )
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def select_all_employees(self) -> list:
        """
        Method responsible for returning all employees from the database
        """
        with Connection() as conn:
            try:
                return conn.session.query(Employee).all()
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def update_employee(self, employee: Employee) -> Employee:
        """
        Method responsible for updating a employee in the database
        """
        with Connection() as conn:
            try:
                conn.session.merge(employee)
                conn.session.commit()
                return employee
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def delete_employee(self, employee_id: str) -> None:
        """
        Method responsible for deleting a employee from the database
        """
        with Connection() as conn:
            try:
                conn.session.query(Employee).filter(Employee.id == employee_id).delete()
                conn.session.commit()
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()