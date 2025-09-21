import pytest
from .db_connection_handler import DBConnectionHandler


@pytest.mark.skip(reason="Integration with DB")
def test_db_connection_handler():
    db_conn_handler = DBConnectionHandler()

    assert db_conn_handler.session is None             #teste de integridade

    with db_conn_handler:
        assert db_conn_handler.session is not None      #teste de integridade
