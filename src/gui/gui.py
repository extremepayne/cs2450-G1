import tkinter as tk
from components.custom_button import CustomButton
from components.task_visual import TaskItem

# Create the main window
root = tk.Tk()
root.title("Course Task Manager")
root.geometry("1500x900")

# Change the window background color
root.configure(background="#FFFFFF")

nav_bar = tk.Frame(root, bg="#B6EEFB", height=75)
nav_bar.pack(fill=tk.X)

# Example use of a custom button component
example_button = CustomButton(
    nav_bar, text="Example Button", command=lambda: print("Button clicked!")
)

# Packing button into the navigation bar
example_button.pack(side=tk.LEFT, padx=10, pady=10)


# Create a container for tasks below the nav bar
task_container = tk.Frame(root, bg="#FFFFFF")
task_container.pack(fill="both", expand=True, padx=20, pady=20)

# Sample tasks for testing
sample_tasks = [
    ("Assignment 1", "Complete chapter 1-3", "CS 2450", "2025-03-01"),
    ("Project Milestone", "Submit phase 1", "CS 3060", "2025-03-15"),
    ("Quiz Prep", "Study for quiz 2", "CS 2420", "2025-03-10"),
]


def delete_task(task_name):
    print(f"Delete task: {task_name}")


def edit_task(task_name):
    print(f"Edit task: {task_name}")


# Create task items
for task in sample_tasks:
    task_item = TaskItem(
        task_container, *task, delete_callback=delete_task, edit_callback=edit_task
    )
    task_item.pack(fill="x", padx=5, pady=5)

# ...existing code...

# Run the application
root.mainloop()
