import faker
import random
from uuid import uuid4
import faker.providers
from src.utils.connection_db import get_connection, populate_db, read_raw_from_db


DEPARTMENTS = [
    "Tecnologia e Inovação",
    "Recursos Humanos",
    "Financeiro",
    "Marketing",
    "Vendas"
]

faker = faker.Faker()
connection = get_connection()


def create_fake_departments() -> dict:
    for department in DEPARTMENTS:
        sql: str = f"INSERT INTO tb_departament (id, name) VALUES ('{str(uuid4())}','{department}')"
        populate_db(connection, sql)

def create_fake_employeer() -> dict:
    for _ in range(10):
        sql:str = f"INSERT INTO tb_employee (id, name, department_id, dependents) VALUES ('{str(uuid4())}', '{faker.name()}',\
            '{get_department_id_by_name(random.choice(DEPARTMENTS))}', {random.randint(0, 5)})"
        populate_db(connection,sql)
    
def get_department_id_by_name(name:str) -> str:
    result = read_raw_from_db(connection, f"SELECT id FROM tb_departament WHERE name = '{name}'")
    return result.get('id')

# python populate_db.py
if __name__ == "__main__":
    create_fake_departments()
    create_fake_employeer()


# Argparse https://realpython.com/command-line-interfaces-python-argparse/#fine-tuning-your-command-line-arguments-and-options
# python app.py ......