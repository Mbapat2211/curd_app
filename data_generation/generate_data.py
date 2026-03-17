import pandas as pd
import random
import sqlite3 as sql

def create(name, age, email):
    con = sql.connect("Customer.db")
    c = con.cursor()
    c.execute(f"INSERT INTO CUSTOMER_DATA VALUES (?, ?, ?)", (name, age, email))
    con.commit()
    con.close()

df_f = pd.read_csv("data_generation/Forename_Autumn2014.csv")
df_s = pd.read_csv("data_generation/Surname_Autumn2014.csv")

first_name_list = df_f["Forename"]
last_name_list = df_s["Surname"]

for i in range(100):
    for j in range(100):
        first_name = first_name_list[i]
        last_name = last_name_list[j]
        name = f"{first_name} {last_name}"
        email = f"{first_name}.{last_name}@dummy.com"
        age = random.randint(18, 60)
        create(name, age, email)
