# Execute SQL from file
from connection import get_cursor, connection

with open("schema.sql", "r") as f:
    get_cursor().execute(f.read())

get_cursor().execute(
    "INSERT INTO posts (title, content) VALUES (%s, %s)",
    ("First Post 3", "Content for the first post 3"),
)

get_cursor().execute(
    "INSERT INTO posts (title, content) VALUES (%s, %s)",
    ("Second Post 3 ", "Content for the second post 3"),
)

connection.commit()
get_cursor().close()
connection.close()
