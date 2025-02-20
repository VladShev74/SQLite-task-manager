import sqlite3

# Connect to the database and create a cursor
connection = sqlite3.connect('task_manager.db')
cursor = connection.cursor()

# Add a users to the users table

user_1 = ('John', 'Doe', 'john123@example.com')
user_2 = ('Jane', 'Smith', 'jane456@example.com')
user_3 = ('Alice', 'Brown', 'alice789@example.com')

for user in [user_1, user_2, user_3]:
    cursor.execute("INSERT INTO users (FirstName, LastName, Email) VALUES (?, ?, ?)", user)

# Add a categories to the categories table

category_1 = ('Work',)
category_2 = ('Personal',)

for category in [category_1, category_2]:
    cursor.execute("INSERT INTO categories (Name) VALUES (?)", category)

# Add tasks to the tasks table

task_1 = ('Task 1', 'Description of Task 1', 'In Progress', 1, 1)
task_2 = ('Task 2', 'Description of Task 2', 'Completed', 2, 2)
task_3 = ('Task 3', 'Description of Task 3', 'Not Started', 3, None)

for task in [task_1, task_2, task_3]:
    cursor.execute("INSERT INTO tasks (Title, Description, Status, User_ID, Category_ID) VALUES (?, ?, ?, ?, ?)", task)

# Print to console to confirm the data was added
print("Data added successfully.")

# Commit changes and close the connection
connection.commit()
connection.close()