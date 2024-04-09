from sqlalchemy import create_engine

class Connection: 
    """
    Responsible Class for creating a connection with the database 
    """
    __connection_string: str
    __engine: create_engine

    def __init__(self) -> None:
        self.__connection_string = "mysql+pymysql://loren:loren@localhost:3306/projeto_vaga_backend"
        self.__engine= self.__connect()
    def __connect(self):
        return create_engine(self.__connection_string)

    def get_connection(self):
        return self.__engine