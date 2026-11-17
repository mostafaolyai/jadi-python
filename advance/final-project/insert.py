from contextlib import closing
from db import get_connection

def create_car(name, model, year, kilometer, price):
    with closing(get_connection()) as conn:
        with conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO bama (name, model, year, kilometer, price) VALUES (%s, %s, %s, %s, %s)",
                    (name, model, year, kilometer, price)
                )