from src.model.entity.departament import Departament
from sqlalchemy.exc import SQLAlchemyError
from src.infra.db.settings.connection import Connection

class DepartamentRepository():
    """
    Class responsible
    for implementing the
    departament repository
    interface
    """

    def insert_departament(self, departament: Departament) -> Departament:
        """
        Method responsible for inserting a departament in the database
        """
        with Connection() as conn:
            try:
                conn.session.add(departament)
                conn.session.commit()
                return departament
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def select_departament(self, departament_id: str) -> Departament:
        """
        Method responsible for returning a departament from the database
        """
        with Connection() as conn:
            try:
                return conn.session.query(Departament).filter(Departament.id == departament_id).first()
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def select_all_departament(self) -> list:
        """
        Method responsible for returning all departament from the database
        """
        with Connection() as conn:
            try:
                return conn.session.query(Departament).all()
            except SQLAlchemyError as e:
                conn.session.rollback()
                print("An error occurred while querying departments:", e)
                raise
            finally:
                conn.session.close()

    def update_departament(self, departament: Departament) -> Departament:
        """
        Method responsible for updating a departament in the database
        """
        with Connection() as conn:
            try:
                conn.session.merge(departament)
                conn.session.commit()
                return departament
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def delete_departament(self, departament_id: str) -> None:
        """
        Method responsible for deleting a departament from the database
        """
        with Connection() as conn:
            try:
                conn.session.query(Departament).filter(Departament.id == departament_id).delete()
                conn.session.commit()
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()