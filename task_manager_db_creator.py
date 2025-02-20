import sqlite3

# Connect to the database and create a cursor
connection = sqlite3.connect('task_manager.db')
cursor = connection.cursor()

# Create a table for users

create_table_users = """CREATE TABLE IF NOT EXISTS users (
User_ID INTEGER PRIMARY KEY,
FirstName TEXT NOT NULL,
LastName TEXT NOT NULL,
Email TEXT NOT NULL
)"""

cursor.execute(create_table_users)

# Create a table for categories

create_table_categories = """CREATE TABLE IF NOT EXISTS categories (
Category_ID INTEGER PRIMARY KEY,
Name TEXT NOT NULL
)"""

cursor.execute(create_table_categories)

# Create a table for tasks

create_table_tasks = """CREATE TABLE IF NOT EXISTS tasks (
Task_ID INTEGER PRIMARY KEY,
Title TEXT NOT NULL,
Description TEXT NOT NULL,
Status TEXT NOT NULL,
User_ID INTEGER NOT NULL,
Category_ID INTEGER,
FOREIGN KEY (User_ID) REFERENCES users(User_ID),
FOREIGN KEY (Category_ID) REFERENCES categories(Category_ID) ON DELETE SET NULL
)"""

cursor.execute(create_table_tasks)

# Commit changes and close the connection
connection.commit()
connection.close()