import pytest
from src.infra.db.settings.connection import Connection


"""
This test is skipped because it is necessary to have a database to run it.
"""
@pytest.mark.skip("This test is skipped because it is necessary to have a database to run it.")
def test_connection():
      """
      Test if the connection is not None,
      if the connection is None, the test will fail.
      """
      connection = Connection()
      assert connection.get_connection() is not None