from sqlalchemy import create_engine

class Connection: 
    """
    Responsible Class for creating a connection with the database 
    """
    __connection_string: str
    __engine: create_engine

    """
    Initializes the connection string and the engine
    """
    def __init__(self) -> None:
        self.__connection_string = "mysql+pymysql://loren:loren@localhost:3306/projeto_vaga_backend"
        self.__engine= self.__connect()
    """
    Create a connection with the database
    """
    def __connect(self) -> create_engine:
        return create_engine(self.__connection_string)
    """
    To get the connection with the database
    """
    def get_connection(self) -> create_engine:
        return self.__engine