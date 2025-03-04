import tkinter as tk
from components.custom_button import CustomButton
from components.task_visual import TaskItem
from components.filter_menu import MenuWindow
from components.edit_task_view import EditTaskView
from components.add_task_view import AddTaskView
from components.add_course_view import AddCourseView
import os

# Create the main window
root = tk.Tk()
root.title("Course Task Manager")
root.geometry("1500x900")

# Change the window background color
root.configure(background="#FFFFFF")

nav_bar = tk.Frame(root, bg="#B6EEFB", height=75)
nav_bar.pack(fill=tk.X)


def resize_image(image_path, width, height):
    """Resize an image while maintaining aspect ratio"""
    img = Image.open(image_path)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)


filter_menu = MenuWindow(
    root, lambda c, d: print(f"Filtering by course: {c} and date: {d}")
)


def toggle_filter_menu():
    if filter_menu.winfo_ismapped():
        filter_menu.pack_forget()
    else:
        filter_menu.pack(after=nav_bar, fill="x")


def edit_task(task_id):
    def save_changes(task_data):
        print(f"Saving changes for task {task_id}: {task_data}")
        # Implement other saving logic here

    edit_window = EditTaskView(root, task_id=task_id, save_callback=save_changes)
    edit_window.grab_set()  # Make window modal


def add_new_task():
    def save_new_task(task_data):
        print(f"Adding new task: {task_data}")
        # Implement task creation logic here

    add_window = AddTaskView(root, save_callback=save_new_task)
    add_window.grab_set()  # Make window modal


def add_new_course():
    def save_new_course(course_data):
        print(f"Adding new course: {course_data}")
        # Implement course creation logic here

    add_window = AddCourseView(root, save_callback=save_new_course)
    add_window.grab_set()  # Make window modal


# Menu Button with icon
try:
    menu_icon = resize_image(os.path.join(assets_dir, "menu.png"), 20, 20)
    menu_button = tk.Button(
        nav_bar,
        image=menu_icon,
        command=toggle_filter_menu,
        bg="#B6EEFB",
        relief="flat",
        bd=0,
    )
    menu_button.image = menu_icon  # Keep a reference
    menu_button.pack(side=tk.LEFT, padx=10, pady=10)
except Exception as e:
    # Fallback to text button if image fails to load
    menu_button = CustomButton(nav_bar, text="Filter", command=toggle_filter_menu)
    menu_button.pack(side=tk.LEFT, padx=10, pady=10)

# Add Task Button
add_task_button = CustomButton(nav_bar, text="+ Add Task", command=add_new_task)
add_task_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Add Course Button - place it next to Add Task
add_course_button = CustomButton(nav_bar, text="+ Add Course", command=add_new_course)
add_course_button.pack(side=tk.RIGHT, padx=10, pady=10)

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


# Create task items
for task in sample_tasks:
    task_item = TaskItem(
        task_container, *task, delete_callback=delete_task, edit_callback=edit_task
    )
    task_item.pack(fill="x", padx=5, pady=5)

# Run the application
root.mainloop()
