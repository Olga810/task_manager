from db import get_connection


def list_statutes() -> list[dict]:
    with get_connection() as connection:
        return connection.execute("SELECT id, code, name FROM statutes ORDER BY id").fetchall()