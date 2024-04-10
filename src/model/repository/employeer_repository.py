from abc import ABC, abstractmethod
from src.model.entity.employeer import Employeer

class EmployeerRepository(ABC):
    """
    Abstract class responsible for defining the employeer repository interface
    """
    @abstractmethod
    def insert_employeer(self, employeer: Employeer) -> Employeer:
        pass

    @abstractmethod
    def select_employeer(self, employeer_id: str) -> Employeer:
        pass

    @abstractmethod
    def select_all_employeers(self) -> list:
        pass

    @abstractmethod
    def update_employeer(self, employeer: Employeer) -> Employeer:
        pass

    @abstractmethod
    def delete_employeer(self, employeer_id: str) -> None:
        pass