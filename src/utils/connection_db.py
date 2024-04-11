import pymysql.cursors


def get_connection():
    """Retorna a conexão com o DB
    """

    return pymysql.connect(
        host='db_test',
        user='loren',
        password='loren',
        database='projeto_vaga_backend',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        )
    
def populate_db(connection, table_name:str, data:dict) -> None:
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO `{table_name}` (`{"`,`".join(data.keys())}`) VALUES ({"%s,"*len(data)})"
            cursor.execute(sql, (data.values()))
        connection.commit()

def read_raw_from_db(connection, table_name:str, data:tuple, target:tuple) -> dict:
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
        sql = f"SELECT `{'`,`'.join(data)}` FROM `{table_name}` WHERE `{target[0]}`=%s"
        cursor.execute(sql, (f'{target[1]}',))
        result = cursor.fetchone()
        return result
    