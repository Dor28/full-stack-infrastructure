import psycopg2
import settings
import os

conn = None


def connect():
    global conn
    try:
        conn = psycopg2.connect(dbname=settings.DB_NAME,
                                user=settings.DB_USER,
                                password=settings.DB_PASSWORD,
                                host=settings.DB_HOST,
                                port=settings.DB_PORT)
    except psycopg2.DatabaseError as e:
        print(e)


def get_db():
    if not conn:
        connect()
    return conn


