import sqlite3

conn = sqlite3.connect("data/usuarios.db")
cursor = conn.cursor()

with open("database.sql", "r") as f:
    sql_script = f.read()

cursor.executescript(sql_script)
conn.commit()
conn.close()

print("Base de datos creada correctamente.")

