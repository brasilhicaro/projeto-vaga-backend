import pymysql.cursors
from os import getenv

def get_connection():
    """Retorna a conexão com o DB
    """

    return pymysql.connect(
        host= getenv('HOST'),
        user= getenv('USER'),
        password= getenv('PASSWORD'),
        database=getenv('DATABASE'),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        )
    
    
def populate_db(connection, sql_function:str) -> None:
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            cursor.execute(sql_function)
        connection.commit()

def read_raw_from_db(connection:object, sql_function:str) -> dict:
    """_summary_

    Args:
        connection (_type_): conexão com db
        table_name (str): nome da tabela
        data (tuple): Campos buscados da tabela 
        target (tuple): (label, target)

    Returns:
        dict: _description_
    """
    with connection.cursor() as cursor:
        sql = sql_function
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    