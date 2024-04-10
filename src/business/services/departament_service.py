from src.model.entity.departament import Departament
from src.model.repository.departament_repository import DepartamentRepository
from src.model.repository.impl.departament_repository_impl import DepartamentRepositoryImpl
from src.infra.db.settings.connection import Connection
from src.business.dto.departament_request_DTO import DepartamentRequestDTO
from src.business.dto.departament_response_DTO import DepartamentResponseDTO

"""
Class responsible
to service the
departament
"""
class DepartamentService:
    """
    Method responsible for
    creating a departament
    """
    
    __repository: DepartamentRepository

    def __init__(self):
        self.__repository = DepartamentRepositoryImpl()
    
    def create_departament(self, departament_request: DepartamentRequestDTO) -> DepartamentResponseDTO:
        with Connection() as conn:
            try:
                departament = Departament(name=departament_request.name)
                if not self.validate_departament(departament_request):
                    raise Exception("Invalid departament name")
                departament = self.__repository.create(departament)

                return DepartamentResponseDTO(id=departament.id, name=departament.name)
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()
    def list_departaments(self) -> list:
        with Connection() as conn:
            try:
                departaments = self.__repository.list_departaments()
                return [DepartamentResponseDTO(id=departament.id, name=departament.name) for departament in departaments]
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def get_departament(self, id: str) -> DepartamentResponseDTO:
        with Connection() as conn:
            try:
                departament = self.__repository.get_departament(id)
                return DepartamentResponseDTO(id=departament.id, name=departament.name)
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def update_departament(self, id: str, departament_request: DepartamentRequestDTO) -> DepartamentResponseDTO:
        with Connection() as conn:
            try:
                departament = self.get_departament(id, departament_request)
                departament.name = departament_request.name
                if not self.validate_departament(departament_request):
                    raise Exception("Invalid departament name")
                departament = self.__repository.update_departament(departament)
                return DepartamentResponseDTO(id=departament.id, name=departament.name)
            except:
                raise Exception("Departament not found")

    def delete_departament(self, id: str) -> None:
        with Connection() as conn:
            try:
                self.__repository.delete_departament(id)
            except:
                raise Exception("Departament not found")


    def validate_departament(self, departament:DepartamentRequestDTO) -> bool:
        if departament.name == "" and departament.name == None and \
        (departament.name.isnum or departament.name.isalphanum()) \
        and departament.name.isspace() and (len(departament.name) > 100 or len(departament.name) < 3):
            return False
        return True
        