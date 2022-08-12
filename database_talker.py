import sqlite3 as db

connection = db.connect('SurfDatabase.db')
cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM SurfTable"
)

print(cursor.fetchall())
connection.close()
