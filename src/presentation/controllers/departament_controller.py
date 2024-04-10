from flask import Blueprint, request
from src.business.services.departament_service import DepartamentService
from src.business.dto.departament_request_DTO import DepartamentRequestDTO

departament_controller = Blueprint('departament_controller', __name__)

@departament_controller.route('/departament/list', methods=['GET'])
def list():
    try:
        departament_service = DepartamentService()
        departaments = departament_service.list_departaments()
        return {"departaments": [departament.__dict__ for departament in departaments]}, 200
    except Exception as e:
        return {"message": str(e)}, 400

@departament_controller.route('/departament/create', methods=['POST'])
def create():
    try:
        departament_service = DepartamentService()
        departament_request = DepartamentRequestDTO(name=request.json['name'])
        departament = departament_service.create_departament(departament_request)
        return departament.__dict__, 200
    except Exception as e:
        return {"message": str(e)}, 400