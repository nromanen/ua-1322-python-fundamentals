from contextlib import contextmanager

import psycopg2

connection = psycopg2.connect(
    dbname="schedule", user="postgres", password="root", host="localhost", port="5432"
)


def get_cursor():
    return get_connection().cursor()


def get_connection():
    global connection
    if connection is None or connection.closed:
        connection = psycopg2.connect(...)
    return connection


@contextmanager
def get_db():
    cursor = get_connection().cursor()
    try:
        yield cursor
    finally:
        cursor.close()
