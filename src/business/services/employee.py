from src.model.entity.Models import Employee
from src.model.repository.employee import EmployeeRepository
from src.business.dto.employee import EmployeeRequest, EmployeeResponse
from .department import DepartmentService


class EmployeeService:
    """
    This class is responsible
    to service the
    employee
    """

    def __init__(self):
        """_summary_: Initialize the EmployeeService class
        """
        self.__repository = EmployeeRepository()

    def list_employees(self) -> list:
        """_summary_ : List all employees

        Returns:
            list: _description_: Return a list with all employees
        """
        try:
            employees = self.__repository.select_all_employees()
            if len(employees) == 0:
                return []
            
            return [
                EmployeeResponse(
                    name=employee.name,
                    have_dependents=self.validate_dependents(employee),
                )
                for employee in employees
            ]
        except Exception as e:
            raise 


    def create_employee(self, employee: EmployeeRequest) -> EmployeeResponse:
        """_summary_: Create employee

        Args:
            employee (EmployeeRequest): _description_: Employee object to be created

        Returns:
            bool: _description_: Return True if the employee is created, otherwise False
        """
        try:
            if self.validate_employee(employee):
                department_id = DepartmentService().find_ID_by_name(employee.department_name)
                employee_entity = Employee(employee.name, department_id, employee.dependents)
                self.__repository.insert_employee(employee_entity)
        except Exception as e:
            raise
    
    def validate_dependents(self, employee: Employee) -> bool:
        """_summary_: Validate dependents to make a convert have_dependents

        Args:
            employee (Employee): _description_: Employee object to be validated

        Returns:
            bool: _description_: Return True if the employee have dependents, otherwise False
        """
        if employee.dependents>0:
            return True
        return False
    
    def validate_employee(self, employee: EmployeeRequest) -> bool:
        """_summary_: Validate employee 

        Args:
            employee (EmployeeRequest): _description_: Employee object to be validated

        Returns:
            bool: _description_: Return True if the employee is valid, otherwise False
        """
        name:str = employee.name
        if (
            name == ""
            or name == None
            or (len(name) > 100 or len(name) < 3)
            or name.islower()
        ):
            return False
        department_name = employee.department_name
        if (department_name == ""
            or department_name == None
            ):
                return False 
        dependents =employee.dependents
        if (dependents == None
            or int(dependents) < 0
            ):
                return False
                
        return True
    