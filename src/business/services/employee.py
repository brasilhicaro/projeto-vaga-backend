from src.model.entity.Models import Employee
from src.model.repository.employee import EmployeeRepository
from src.business.dto.employee import EmployeeRequest, EmployeeResponse

"""
This class is responsible
to service the
employee
"""


class EmployeeService:
    """
    Method responsible for
    creating an employee
    """

    def __init__(self):
        self.__repository = EmployeeRepository()

    def list_employees(self) -> list:
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

    def validate_employee(self, employee: EmployeeRequest) -> bool:
        name_split = employee.name.split(" ")
        for name in name_split:
            if (
                len(name) < 3
                or len(name) > 20
                or not name.isalpha()
                or name[0].islower()
            ):
                return False
        return True

    def validate_dependents(self, employee: Employee) -> bool:
        if employee.dependents>0:
            return True
        return False