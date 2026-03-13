import sqlite3 as sql
import constants

def delete(name, age, email):
    con = sql.connect(constants.DATABASE_NAME)
    c = con.cursor()
    c.execute(f"DELETE FROM {constants.TABLE_NAME} WHERE Name=?, Age=?, Email=?", (name, age, email))
    con.close()