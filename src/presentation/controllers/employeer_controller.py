from flask import Blueprint, request
from src.business.services.employeer_service import EmployeerService
from src.business.dto.employeer_request_DTO import EmployeerRequestDTO

employeer_controller = Blueprint('employeer_controller', __name__)

@employeer_controller.route('/employeer/list', methods=['GET'])
def list():
    try:
        employeer_service = EmployeerService()
        employeers = employeer_service.list_employeers()
        return {"employeers": [employeer.__dict__ for employeer in employeers]}, 200
    except Exception as e:
        return {"message": str(e)}, 400
    
@employeer_controller.route('/employeer/create', methods=['POST'])
def create():
    try:
        employeer_service = EmployeerService()
        employeer_request = EmployeerRequestDTO(name=request.json['name'], departament_id=request.json['departament_id'], have_dependents=request.json['have_dependents'])
        employeer = employeer_service.create_employeer(employeer_request)
        return employeer.__dict__, 200
    except Exception as e:
        return {"message": str(e)}, 400




