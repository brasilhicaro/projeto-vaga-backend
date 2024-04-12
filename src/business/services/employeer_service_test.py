from src.business.services.employeer_service import EmployeerService
from src.business.services.departament_service import DepartamentService
from src.model.entity.employeer import Employeer
from src.model.entity.departament import Departament
import pytest


def register_employeer():
    
    departament = Departament(
        id="1",
        name="Test"
    )
    DepartamentService().create_departament(departament)
    
    employeer = Employeer(id= "1",
                         name="Test",
                            departament_id="1",
                            have_dependents=0)   
    
    employeer_service = EmployeerService()
    assert employeer_service.create_employeer(employeer) == employeer
    assert employeer_service.list_employeers() == [employeer]
    assert employeer_service.get_employeer("1") == employeer
    assert employeer_service.delete_employeer("1") == True