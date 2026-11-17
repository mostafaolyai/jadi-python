from contextlib import closing
from db import get_connection


with closing(get_connection()) as conn:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                ALTER TABLE employee
                    ADD COLUMN IF NOT EXISTS username VARCHAR(255),
                    ADD COLUMN IF NOT EXISTS password VARCHAR(255),
                    DROP COLUMN IF EXISTS email,
                    DROP COLUMN IF EXISTS phone;
                """
            )