import sqlite3

# Establish a connection
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15")
rows = cursor.fetchall()
print(rows)

# Insert new rows
