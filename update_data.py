import sqlite3

# Add a simple helper function to avoid code duplication
def fetch_by_task_id(task_id):
    cursor.execute("SELECT * FROM tasks WHERE Task_ID = ?", (task_id,))
    tasks = cursor.fetchone()
    return tasks

# Connect to the database and create a cursor
connection = sqlite3.connect('task_manager.db')
cursor = connection.cursor()

# Fetch the task with id 1
task_id = 1
print(f"Task with ID {task_id} before update:")
print(fetch_by_task_id(task_id))

# Update the status of the task
new_status = 'Done'
cursor.execute("UPDATE tasks SET Status = ? WHERE Task_ID = ?", (new_status, task_id))
print(f"Task with ID {task_id} after update:")
print(fetch_by_task_id(task_id))

# Close the connection without commiting the changes
connection.close()