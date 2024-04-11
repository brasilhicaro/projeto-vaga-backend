from src.model.entity.employee import Employee
from src.infra.db.settings.connection import Connection
from src.model.repository.employee import EmployeeRepository
from src.business.dto.employee import Employee, EmployeeResponse

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

    @classmethod
    def create_employee(self, employee_request: Employee) -> EmployeeResponse:
        try:
            employee = Employee(
                name=employee_request.name,
                department_id=employee_request.department_id,
                have_dependents=employee_request.dependents,
            )
            if not self.validate_employee(employee_request):
                raise Exception("Invalid employee name")
            employee = self.__repository.create(employee)

            return EmployeeResponse(
                id=employee.id,
                name=employee.name,
                department_id=employee.department_id,
                have_dependents=self.validate_dependents(employee),
            )
        except Exception as e:
            raise Exception(e.message)

    def list_employees(self) -> list:
        try:
            employees = self.__repository.list_employees()
            return [
                EmployeeResponse(
                    id=employee.id,
                    name=employee.name,
                    department_id=employee.department_id,
                    have_dependents=self.validate_dependents(employee),
                )
                for employee in employees
            ]
        except Exception as e:
            raise Exception(e.message)

    def validate_employee(self, employee: Employee) -> bool:
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

    def get_employee(self, id: str) -> EmployeeResponse:
        try:
            employee = self.__repository.get_employee(id)
            return EmployeeResponse(
                id=employee.id,
                name=employee.name,
                department_id=employee.department_id,
                have_dependents=self.validate_dependents(employee),
            )
        except Exception as e:
            raise Exception("e.message")

    def delete_employee(self, id: str) -> bool:
        try:
            return self.__repository.delete_employee(id)
        except Exception as e:
            raise Exception(e.message)

    def update_employee(self, id: str, employee_request: Employee) -> EmployeeResponse:
        try:
            employee = Employee(
                name=employee_request.name,
                department_id=employee_request.department_id,
                have_dependents=employee_request.dependents,
            )
            if not self.validate_employee(employee_request):
                raise Exception("Invalid employee name")
            employee = self.__repository.update_employee(id, employee)
            return EmployeeResponse(
                id=employee.id,
                name=employee.name,
                department_id=employee.department_id,
                have_dependents=self.validate_dependents(employee),
            )
        except Exception as e:
            raise Exception(e.message)

    def validate_dependents(self, employee: Employee) -> bool:
        if employee.dependents>0:
            return True
        return False