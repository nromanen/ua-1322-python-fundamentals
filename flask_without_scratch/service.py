from database.connection import get_cursor, get_db
from database.model import Post


def get_posts(id=None):
    cursor = get_cursor()
    base_query = "SELECT * FROM posts"
    where_clause = " WHERE id = %s" if id else ""
    query = base_query + where_clause
    cursor.execute(query, (id,) if id else None)

    columns = [desc[0] for desc in cursor.description]
    posts = [Post(**dict(zip(columns, post))) for post in cursor.fetchall()]

    cursor.close()
    return posts


def create(post):
    with get_db() as cursor:
        cursor.execute(
            "INSERT INTO posts (title, content) VALUES (%s, %s)",
            (post.title, post.content),
        )
        cursor.connection.commit()
    return post


def update(post):
    with get_db() as cursor:
        cursor.execute(
            "update posts set title = %s, content = %s where id = %s",
            (post.title, post.content, post.id),
        )
        cursor.connection.commit()
    return post


def delete(id):
    with get_db() as cursor:
        cursor.execute("delete from posts where id = %s", (id,))
        cursor.connection.commit()
    return True
