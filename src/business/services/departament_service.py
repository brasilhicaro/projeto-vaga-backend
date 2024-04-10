from src.model.entity.departament import Departament
from src.model.repository.departament_repository_impl import DepartamentRepository
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
        self.__repository = DepartamentRepository()
    
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

    def list_departaments(self) -> dict:
        try:
            print("List departaments service")
            departaments = self.__repository.select_all_departament()
            print("retornando departaments")
            return {DepartamentResponseDTO(id= departament.id, name=departament.name ) for departament in departaments}
        except Exception as e:
            raise 

    def get_departament(self, id: str) -> DepartamentResponseDTO:
        try:
            departament = self.__repository.get_departament(id)
            return DepartamentResponseDTO(id=departament.id, name=departament.name)
        except:
            raise Exception("Departament not found")
        
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
        