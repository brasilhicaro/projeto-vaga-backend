import pytest
from .connection import  Connection


"""
This test is skipped because it is necessary to have a database to run it.
"""
@pytest.mark.skip(reason="Sensitive test, it's necessary a database to run this test")
def test_connection():
      """
      Test if the connection is not None,
      if the connection is None, the test will fail.
      """
      connection = Connection()
      assert connection.get_connection() is not None