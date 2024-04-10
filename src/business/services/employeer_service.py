from src.model.entity.employeer import Employeer
from src.infra.db.settings.connection import Connection
from src.model.repository.employeer_repository_impl import EmployeerRepository
from src.business.dto.employeer_request_DTO import EmployeerRequestDTO
from src.business.dto.employeer_response_DTO import EmployeerResponseDTO

"""
This class is responsible
to service the
employeer
"""
class EmployeerService:
    """
    Method responsible for
    creating a employeer
    """
    

    def __init__(self):
        self.__repository = EmployeerRepository()
    @classmethod
    def create_employeer(self, employeer_request: EmployeerRequestDTO) -> EmployeerResponseDTO:
        try:
            employeer = Employeer(name=employeer_request.name,
                                   departament_id=employeer_request.departament_id,
                                     have_dependents=employeer_request.dependents)
            if not self.validate_employeer(employeer_request):
                raise Exception("Invalid employeer name")
            employeer = self.__repository.create(employeer)

            return EmployeerResponseDTO(id=employeer.id,
                                         name=employeer.name,
                                           departament_id=employeer.departament_id,
                                              have_dependents=self.validate_dependents(employeer))
        except Exception as e:
            raise Exception(e.message)
               

    def list_employeers(self) -> list:
        try:
            employeers = self.__repository.list_employeers()
            return [EmployeerResponseDTO(id=employeer.id, name=employeer.name,
                                          departament_id=employeer.departament_id,
                                             have_dependents=self.validate_dependents(employeer)) for employeer in employeers]
        except Exception as e:
            raise Exception(e.message)
        
    def validate_employeer(self, employeer: EmployeerRequestDTO) -> bool:
        name_split = employeer.name.split(" ")
        for name in name_split:
            if len(name) < 3 or len(name) > 20 or not name.isalpha() or name[0].islower():
                return False
        return True
    
    def get_employeer(self, id: str) -> EmployeerResponseDTO:
        try:
            employeer = self.__repository.get_employeer(id)
            return EmployeerResponseDTO(id=employeer.id, name=employeer.name,
                                         departament_id=employeer.departament_id,
                                           have_dependents=self.validate_dependents(employeer))
        except Exception as e:
            raise Exception("e.message")
    
    def delete_employeer(self, id: str) -> bool:
        try:
            return self.__repository.delete_employeer(id)
        except Exception as e:
            raise Exception(e.message)

    def update_employeer(self, id: str, employeer_request: EmployeerRequestDTO) -> EmployeerResponseDTO:
        try:
            employeer = Employeer(name=employeer_request.name,
                                   departament_id=employeer_request.departament_id,
                                     have_dependents=employeer_request.dependents)
            if not self.validate_employeer(employeer_request):
                raise Exception("Invalid employeer name")
            employeer = self.__repository.update_employeer(id, employeer)
            return EmployeerResponseDTO(id=employeer.id,
                                         name=employeer.name,
                                           departament_id=employeer.departament_id,
                                              have_dependents=self.validate_dependents(employeer))
        except Exception as e:
            raise Exception(e.message)
    

    def validate_dependents(self, employeer: EmployeerRequestDTO) -> bool:
        if employeer.dependents < 0:
            return False
        return True
