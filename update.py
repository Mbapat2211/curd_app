import sqlite3 as sql
import constants

def update(initial_name, initial_age, initial_email, updated_name, updated_age, updated_email):
    con = sql.connect(constants.DATABASE_NAME)
    c = con.cursor()
    c.execute(f"UPDATE {constants.TABLE_NAME} SET Name=?, Age=?, Email=? WHERE Name=?, Age=?, Email=?", 
              (updated_name, updated_age, updated_email, initial_name, initial_age, initial_email))
    con.close()