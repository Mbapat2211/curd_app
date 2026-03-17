import sqlite3 as sql
import constants

def read_from_name(name):
    con = sql.connect(constants.DATABASE_NAME)
    c = con.cursor()
    c.execute(f'SELECT * FROM {constants.TABLE_NAME} WHERE Name LIKE "%{name}%"')
    data = c.fetchall()
    con.close()
    return data

def read_from_email(email):
    con = sql.connect(constants.DATABASE_NAME)
    c = con.cursor()
    c.execute(f"SELECT * FROM {constants.TABLE_NAME} WHERE Email=?", (email, ))
    data = c.fetchall()
    con.close()
    return data