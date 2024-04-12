import faker
import random
import faker.providers

from src.business.services.department import DepartmentService

DEPARTMENTS = [
    "Tecnologia e Inovação",
    "Recursos Humanos",
    "Financeiro",
    "Marketing",
    "Vendas"
]

faker = faker.Faker()


def create_fake_departments() -> dict:
    department_service = DepartmentService()
    for department in DEPARTMENTS:
        department_service.create_department(department)
def create_fake_employeer() -> dict:
    for _ in range(10):
        name = faker.name()
        department_id = get_department_id_by_name(random.choice(DEPARTMENTS))
        dependents = random.randint(0, 5)
        employee = {
            "name": name,
            "department_id": get_department_id_by_name(department_id),
            "dependents": dependents
        }
        populate_db(connection, "tb_employee", employee)
        
        
        

def get_department_id_by_name(name:str) -> str:
    departament_service=DepartmentService()
    departament=departament_service.find_ID_by_name(name)
    return departament.id


# python populate_db.py
if __name__ == "__main__":
    create_fake_departments()
    create_fake_employeer()
