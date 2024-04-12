from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from src.model.entity.Models import Base
from dotenv import load_dotenv

from os import getenv

load_dotenv()
class Connection:
    """
    Class responsible for creating the connection with the postgres database
    """
    __session: sessionmaker
    __engine: create_engine
    __cursor: create_engine
    
    def __init__(self) -> None:
        """
        _summary_:
            Method responsible for initializing the connection object
        """
        
        try:
            self.__engine = create_engine(URL.create(
                getenv('POSTGRES_ENGINE'),
                username=getenv('POSTGRES_USER'),
                password=getenv('POSTGRES_PASSWORD'),
                host=getenv('POSTGRES_HOST', 'localhost'),
                port=getenv('POSTGRES_PORT'),
                database=getenv('POSTGRES_DB',)
            ))
            self.__cursor = self.__engine.connect()
            Base.metadata.create_all(bind=self.__engine)
            self.__session = sessionmaker(bind=self.__engine)
        except SQLAlchemyError as err:
            print(e)
            
    def get_session(self) -> sessionmaker:
        """
        _summary_:
            Method responsible for returning the session object
        
        returns: _description_: Session object
        """
        return self.__session()
