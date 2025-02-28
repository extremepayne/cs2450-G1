import tkinter as tk
from components.custom_button import CustomButton
from components.task_visual import TaskItem
from components.filter_menu import MenuWindow
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


# #function to open the task filterer
# def show_filter_menu():
#     def apply_filters(course, due_date):
#         print(f"Filtering by course: {course} and date: {due_date}")
#         # Add your filtering logic here

#     filter_window = MenuWindow(root, apply_filters)
#     filter_window.grab_set()  # Make window modal

# #clickable hamburger menu icon
# # Get the absolute path to the assets directory
# assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

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
