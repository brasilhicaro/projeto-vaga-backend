from src.model.entity.department import Department
from src.model.repository.department import DepartmentRepository
from src.infra.db.settings.connection import Connection
from src.business.dto.department import Department, DepartmentResponse

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

    def create_department(self, department_request: Department) -> DepartmentResponse:
        with Connection() as conn:
            try:
                department = Department(name=department_request.name)
                if not self.validate_department(department_request):
                    raise Exception("Invalid department name")
                department = self.__repository.create(department)

                return DepartmentResponse(id=department.id, name=department.name)
            except:
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    def list_departments(self) -> dict:
        try:
            print("List departments service")
            departments = self.__repository.select_all_department()
            print("retornando departments")
            return {
                DepartmentResponse(id=department.id, name=department.name)
                for department in departments
            }
        except Exception as e:
            raise

    def get_department(self, id: str) -> DepartmentResponse:
        try:
            department = self.__repository.get_department(id)
            return DepartmentResponse(id=department.id, name=department.name)
        except:
            raise Exception("Department not found")

    def update_department(
        self, id: str, department_request: Department
    ) -> DepartmentResponse:
        with Connection() as conn:
            try:
                department = self.get_department(id, department_request)
                department.name = department_request.name
                if not self.validate_department(department_request):
                    raise Exception("Invalid department name")
                department = self.__repository.update_department(department)
                return DepartmentResponse(id=department.id, name=department.name)
            except:
                raise Exception("Department not found")

    def delete_department(self, id: str) -> None:
        with Connection() as conn:
            try:
                self.__repository.delete_department(id)
            except:
                raise Exception("Department not found")

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