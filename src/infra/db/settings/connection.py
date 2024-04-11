
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Connection:
    """
    Responsible Class for creating a connection with the database
    """

    Session: object
    __connection_string: str
    __engine: create_engine

    """
    Initializes the connection string and the engine
    """

    def __init__(self) -> None:
        self.__connection_string = (
            "mysql+pymysql://loren:loren@localhost:3306/projeto_vaga_backend"
        )
        self.__engine = self.__connect()
        self.Session = sessionmaker(bind=self.__engine)

    """
    Create a connection with the database
    """

    def __connect(self) -> create_engine:
        return create_engine(self.__connection_string)

    """
    To get the connection with the database
    """

    def get_session(self) -> object:
        return self.Session()

    def __enter__(self):
        self.session = self.get_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()
