
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_users():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM userdetails;')
        userdetails = cursor.fetchall()
        if result > 0:
            got_users = jsonify(userdetails)
        else:
            got_users = 'No users in DB'
    conn.close()
    return got_users

def add_users(user):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO userdetails (firstname, lastname) VALUES(%s, %s)', (user["firstname"], user["lastname"]))
    conn.commit()
    conn.close()
