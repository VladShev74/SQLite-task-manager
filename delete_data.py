import sqlite3

# Fetch and print all tasks
def print_all_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    print("All tasks:")
    for task in tasks:
        print(task)

# Connect to the database and create a cursor
connection = sqlite3.connect('task_manager.db')
cursor = connection.cursor()

# Enable foreign key constraints (for setting the category_id to NULL when deleting a category)
cursor.execute("PRAGMA foreign_keys = ON;")

# Print all tasks before deletion
print_all_tasks()

# Delete the task with id 3
task_id = 3
cursor.execute("DELETE FROM tasks WHERE Task_ID = ?", (task_id,))
print(f"Task with ID {task_id} deleted.")

# Print all tasks after deletion
print_all_tasks()

# Delete category with id 2
category_id = 2
cursor.execute("DELETE FROM categories WHERE Category_ID = ?", (category_id,))
print(f"Category with ID {category_id} deleted.")

# Print all tasks after deletion of category with id 2
print_all_tasks()

# Print all categories
cursor.execute("SELECT * FROM categories")
categories = cursor.fetchall()
print("All categories after deletion:")
for category in categories:
    print(category)

# Close the connection without commiting the changes
connection.close()
