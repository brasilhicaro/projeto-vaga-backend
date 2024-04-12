from src.model.entity.Models import Department
from src.model.repository.department import DepartmentRepository
from src.business.dto.department import DepartmentRequest, DepartmentResponse

"""
Class responsible
to service the
department
"""


class DepartmentService:
    """
    Method responsible for
    creating a department
    """

    __repository: DepartmentRepository

    def __init__(self):
        self.__repository = DepartmentRepository()

    def list_departments(self) -> dict:
        try:
            departments = self.__repository.select_all_department()
            if len(departments) == 0:
                return {}
            return {
                DepartmentResponse(name=department.name)
                for department in departments
            }
        except Exception as e:
            raise

    def validate_department(self, department: Department) -> bool:
        if (
            department.name == ""
            and department.name == None
            and (department.name.isnumeric() or department.name.isalnum())
            and department.name.isspace()
            and (len(department.name) > 100 or len(department.name) < 3)
        ):
            return False
        return True
    
    def find_ID_by_name(self, department_name: str) -> str :
        try:
            department = self.__repository.find_ID_by_name(department_name)
            return department.id
        except Exception as e:
            raise