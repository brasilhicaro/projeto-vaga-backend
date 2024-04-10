from src.model.repository.employeer_repository import EmployeerRepository
from src.model.entity.employeer import Employeer
from src.infra.db.settings.connection import Connection

class DepartamentRepositoryImpl(EmployeerRepository):
    """
    Class responsible
    for implementing the
    departament repository
    interface
    """

    def insert_employeer(self, employeer: Employeer) -> Employeer:
        """
        Method responsible for inserting a employeer in the database
        """
        with Connection() as conn:
            try:
                conn.session.add(employeer)
                conn.session.commit()
                return employeer
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def select_employeer(self, employeer_id: str) -> Employeer:
        """
        Method responsible for returning a employeer from the database
        """
        with Connection() as conn:
            try:
                return conn.session.query(Employeer).filter(Employeer.id == employeer_id).first()
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def select_all_employeers(self) -> list:
        """
        Method responsible for returning all employeers from the database
        """
        with Connection() as conn:
            try:
                return conn.session.query(Employeer).all()
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def update_employeer(self, employeer: Employeer) -> Employeer:
        """
        Method responsible for updating a employeer in the database
        """
        with Connection() as conn:
            try:
                conn.session.merge(employeer)
                conn.session.commit()
                return employeer
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def delete_employeer(self, employeer_id: str) -> None:
        """
        Method responsible for deleting a employeer from the database
        """
        with Connection() as conn:
            try:
                conn.session.query(Employeer).filter(Employeer.id == employeer_id).delete()
                conn.session.commit()
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()