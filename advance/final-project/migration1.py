from contextlib import closing
from db import get_connection


with closing(get_connection()) as conn:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS bama (
                    name VARCHAR(255),
                    model VARCHAR(255),
                    year INTEGER,
                    kilometer INTEGER,
                    price BIGINT
                )
                """
            )