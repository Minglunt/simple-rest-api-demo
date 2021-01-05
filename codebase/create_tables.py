import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(users_table)

students_table = "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name text, age int)"
cursor.execute(students_table)

cursor.execute("INSERT INTO students VALUES (1, 'Yanice', 22)")

connection.commit()
connection.close()