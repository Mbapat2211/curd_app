import sqlite3 as sql
import constants

def create(name, age, email):
    con = sql.connect(constants.DATABASE_NAME)
    c = con.cursor()
    c.execute(f"INSERT INTO {constants.TABLE_NAME} VALUES (?, ?, ?)", (name, age, email))
    con.close()