from abc import ABC, abstractmethod
from src.model.entity.departament import Departament

class DepartamentRepository(ABC):
    """
    Abstract class responsible
    for defining the departament
    repository interface
    """
    @abstractmethod
    def insert_departament(self, departament: Departament) -> Departament:
        pass

    @abstractmethod
    def select_departament(self, departament_id: str) -> Departament:
        pass

    @abstractmethod
    def select_all_departaments(self) -> list:
        pass

    @abstractmethod
    def update_departament(self, departament: Departament) -> Departament:
        pass

    @abstractmethod
    def delete_departament(self, departament_id: str) -> None:
        pass