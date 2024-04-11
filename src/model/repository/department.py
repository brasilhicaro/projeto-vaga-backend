from src.model.entity.department import Department
from sqlalchemy.exc import SQLAlchemyError
from src.infra.db.settings.connection import Connection


class DepartmentRepository:
    """
    Class responsible
    for implementing the
    department repository
    interface
    """

    def insert_department(self, department: Department) -> Department:
        """
        Method responsible for inserting a department in the database
        """
        with Connection() as conn:
            try:
                conn.session.add(department)
                conn.session.commit()
                return department
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def select_department(self, department_id: str) -> Department:
        """
        Method responsible for returning a department from the database
        """
        with Connection() as conn:
            try:
                return (
                    conn.session.query(Department)
                    .filter(Department.id == department_id)
                    .first()
                )
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def select_all_department(self) -> list:
        """
        Method responsible for returning all department from the database
        """
        with Connection() as conn:
            try:
                return conn.session.query(Department).all()
            except SQLAlchemyError as e:
                conn.session.rollback()
                print("An error occurred while querying departments:", e)
                raise
            finally:
                conn.session.close()

    def update_department(self, department: Department) -> Department:
        """
        Method responsible for updating a department in the database
        """
        with Connection() as conn:
            try:
                conn.session.merge(department)
                conn.session.commit()
                return department
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def delete_department(self, department_id: str) -> None:
        """
        Method responsible for deleting a department from the database
        """
        with Connection() as conn:
            try:
                conn.session.query(Department).filter(
                    Department.id == department_id
                ).delete()
                conn.session.commit()
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()