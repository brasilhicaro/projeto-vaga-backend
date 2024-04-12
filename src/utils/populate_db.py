from src.model.entity.Models import Department, Employee
from src.utils.connection_db import connection
import faker
import random

class FakeDataService:
    def __init__(self):
        self.__DEPARTMENTS: list = [
            "Tecnologia e Inovação",
            "Recursos Humanos",
            "Financeiro",
            "Marketing",
            "Vendas"
        ]
        self.session = connection()
        self.fake = faker.Faker()

    def create_fake_departments(self):
        DEPARTMENTS = [
            "Tecnologia e Inovação",
            "Recursos Humanos",
            "Financeiro",
            "Marketing",
            "Vendas"
        ]
        for department in DEPARTMENTS:
            department = Department(department)
            self.session.add(department)
        self.session.commit()
        self.session.close()
    def create_fake_employees(self, num_employees=10):
        for _ in range(num_employees):
            name = self.fake.name()
            department = random.choice(self.__DEPARTMENTS)
            department_id = self.get_department_id_by_name(department)
            dependents = random.randint(0, 5)
            employee = {
                "name": name,
                "department_id": department_id,
                "dependents": dependents
            }
            employee_entity = Employee(name, department_id, dependents)
            self.session.add(employee)
        self.session.commit()
        self.session.close()

    def get_department_id_by_name(self, name):
        department = self.session.query(Department).filter(Department.name == name).first()
        return department.id
    
    
# python populate_db.py
if __name__ == "__main__":
    data_service = FakeDataService()
    data_service.create_fake_departments()
    data_service.create_fake_employees()