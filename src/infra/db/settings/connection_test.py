from connection import Connection

def test_connection():
    connection = Connection()
    assert connection.get_connection() is not None