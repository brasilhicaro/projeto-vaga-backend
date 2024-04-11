import faker
import random
from uuid import uuid4

import faker.providers
from src.utils.connection_db import get_connection, populate_db


DEPARTMENTS = [
    "Tecnologia e Inovação",
    "Recursos Humanos",
    "Financeiro",
    "Marketing",
    "Vendas"
]

faker = faker.Faker()
connection = get_connection()


def create_fake_department() -> dict:
    """Cria um Departamento Fake

    Returns:
        dict: Com ID e Nome do Departamento
    """
    
    id = uuid4()
    department = random.choice(DEPARTMENTS)
    return {"id":id, "department":department}


def populate_db_with_fake_department(num_departments:int) -> None:
    
    for _ in range(num_departments):
        try:
            dummy_department = create_fake_department()
            populate_db(dummy_department)
        except e as e:
            print(e)



# def create_fake_employee() -> dict:
#     """Cria um Funcionário Fake

#     Returns:
#         dict: Com ID, Nome do Funcionário, ID do Departamento, Dependentes
#     """
    
#     employee_id = uuid4()
#     name = faker.name()
#     department_id = 
    

# python populate_db.py
if __name__ == "__main__":
    ...
    

# Argparse https://realpython.com/command-line-interfaces-python-argparse/#fine-tuning-your-command-line-arguments-and-options
# python app.py ......