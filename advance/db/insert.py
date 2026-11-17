from contextlib import closing
from db import get_connection

def create_user(name, vazn, ghad):
    with closing(get_connection()) as conn:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO employee (name, vazn, ghad) VALUES (%s, %s, %s)",
                    (name, vazn, ghad)
                )