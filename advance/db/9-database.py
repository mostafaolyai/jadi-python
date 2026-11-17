# import psycopg

# with psycopg.connect(
#     host="localhost",
#     port=3031,
#     dbname="ss_server_dev1",
#     user="user",
#     password="password"
# ) as conn:

#     with conn.cursor() as cursor:
#         cursor.execute("CREATE TABLE employee (id SERIAL PRIMARY KEY,name VARCHAR(100),ghad INTEGER,vazn INTEGER);")



from insert import create_user
from fetch import get_users

# employees =[["Amin", 80, 175], ["Mahdi", 90, 190 ], ["Mohammad", 75, 175], ["Ahmad", 60, 175]]

# for item in employees:
#     create_user(item[0], item[1], item[2])


for item in get_users():
    print(item)

