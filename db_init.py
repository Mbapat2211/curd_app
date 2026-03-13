import sqlite3 as sql
import constants

def init_db():
    con = sql.connect(constants.DATABASE_NAME)
    c = con.cursor()
    c.execute(f"CREATE TABLE IF NOT EXISTS {constants.TABLE_NAME}(Name TEXT, Age INTEGER, Email TEXT)")