from sqlalchemy import create_engine
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

from os import getenv

load_dotenv()



def connection():
    try:
        engine = create_engine(URL.create(
                getenv('POSTGRES_ENGINE'),
                username=getenv('POSTGRES_USER'),
                password=getenv('POSTGRES_PASSWORD'),
                host=getenv('POSTGRES_HOST', 'localhost'),
                port=getenv('POSTGRES_PORT'),
                database=getenv('POSTGRES_DB',)
            ))
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except SQLAlchemyError as e:
        print(e)

def populate_db(connection, table_name:str, data:dict) -> None:
    try:
        session = connection()
        # Cria uma nova entrada no banco de dados
        table = session.query(table_name)
        table.insert().values(**data)
        session.commit()
    except SQLAlchemyError as e:
        print(e)

def read_raw_from_db(connection, table_name:str, data:tuple, target:tuple) -> dict:
    try:
        session = connection()
        # Realiza a consulta
        result = session.query(*data).filter(getattr(table_name, target[0]) == target[1]).first()
        return result
    except SQLAlchemyError as e:
        print(e)