import sqlite3
from sqlite3 import Error

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

def firstRun(c,table):
    c.execute(table)

db=create_connection(r"database.db")
c=db.cursor()
table1=""" CREATE TABLE IF NOT EXISTS userInfo (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        password text NOT NULL,
                                    ); """


firstRun(c,table1)
db.close()



