import sqlite3
from sqlite3 import Error

DATABASE = "database.db"
KEY=''
USERNAME=''

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        return conn


def firstRun():
    db = create_connection(DATABASE)
    try:
        table = '''CREATE TABLE userInfo (username text NOT NULL,password text NOT NULL,key text NOT NULL);'''
        db.execute(table)
        db.commit()
        db.close()
    except sqlite3.OperationalError:
        db.close()