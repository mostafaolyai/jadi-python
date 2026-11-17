import psycopg

def get_connection():
    return psycopg.connect(
    host="localhost",
    port=3031,
    dbname="ss_server_dev1",
    user="user",
    password="password"
)