import sqlite3

# Add a simple helper function to avoid code duplication
def fetch_tasks_by_user_id(user_id):
    cursor.execute("SELECT * FROM tasks WHERE User_ID = ?", (user_id,))
    tasks = cursor.fetchall()
    return tasks

# Connect to the database and create a cursor
connection = sqlite3.connect('task_manager.db')
cursor = connection.cursor()

# Fetch all data from the tasks table
fetch_data_command = """SELECT * FROM tasks"""
cursor.execute(fetch_data_command)
tasks = cursor.fetchall()

print("All tasks in tasks table:")
for task in tasks:
    print(task)

# Fetch the data from the tasks table for a specific user
user_id = 1
tasks = fetch_tasks_by_user_id(user_id)

print(f"Tasks for user with ID {user_id}:")
for task in tasks:
    print(task)

# Create a new task for the user for testing purposes
task_1_2 = ('Task 1_2', 'Description of Task 1_2', 'Not Started', 1, 2)
cursor.execute("INSERT INTO tasks (Title, Description, Status, User_ID, Category_ID) VALUES (?, ?, ?, ?, ?)", task_1_2)

# Fetch all data from the tasks table for user with id 1 once again
updated_tasks = fetch_tasks_by_user_id(user_id)

print(f"Tasks for user with ID {user_id} after update:")
for task in updated_tasks:
    print(task)

# Close the connection without commiting the changes (so our new task is not saved)
connection.close()