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
        """_summary_: List all departments

        Returns:
            dict: _description_: Return a dictionary with all departments
        """
        try:
            departments = self.__repository.select_all_department()
            if len(departments) == 0:
                return {}
            return {
                department.name: DepartmentResponse(name=department.name)
                for department in departments
            }
        except Exception as e:
            raise
    
    def create_department(self, department: DepartmentRequest) -> bool:
        """_summary_: Create department

        Args:
            department (DepartmentRequest): _description_: Department object to be created

        Returns:
            bool: _description_: Return True if the department is created, otherwise False
        """
        try:
            if self.validate_department(department):
                self.__repository.insert_department(department.name)
                return True
            return False
        except Exception as e:
            raise   
            

    def validate_department(self, department: DepartmentRequest) -> bool:
        """_summary_: Validate department

        Args:
            department (DepartmentRequest): _description_: Department object to be validated

        Returns:
            bool: _description_: Return True if the department is valid, otherwise False
        """
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
        """_summary_: Find department ID by name 

        Args:
            department_name (str): _description_: Department name to be searched

        Returns:
            str: _description_: Return the department ID found
        """
        try:
            department = self.__repository.select_department_id_by_name(department_name)
            return department
        except Exception as e:
            raise
    def get_department(self, department_id: int) -> Department:
        """_summary_: Get department by ID

        Args:
            department_id (str): _description_: Department ID to be searched

        Returns:
            Department: _description_: Return the department found
        """
        try:
            department = self.__repository.select_department(department_id)
            return department
        except Exception as e:
            raise