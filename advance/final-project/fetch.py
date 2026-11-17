from contextlib import closing
from db import get_connection

def get_cars():
    with closing(get_connection()) as conn:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM bama"
                )
                return cursor.fetchall()    