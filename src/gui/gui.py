import tkinter as tk
from tkinter import messagebox
from components.custom_button import CustomButton
from components.task_visual import TaskItem
from components.filter_menu import MenuWindow
from components.edit_task_view import EditTaskView
from components.add_task_view import AddTaskView
from components.add_course_view import AddCourseView
import os
from datetime import datetime, timedelta

# Create the main window
root = tk.Tk()
root.title("Course Task Manager")
root.geometry("1500x900")

# Change the window background color
root.configure(background="#E6E6E6")

nav_bar = tk.Frame(root, bg="#B6EEFB", height=75)
nav_bar.pack(fill=tk.X)


def resize_image(image_path, width, height):
    """Resize an image while maintaining aspect ratio"""
    img = Image.open(image_path)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)


class TaskManagerGUI:
    def __init__(self):
        self.all_tasks = []  # Store all tasks
        self.task_container = None
        self.setup_gui()

    def delete_task(self, task_name):
        """Delete a task after confirmation"""
        if messagebox.askyesno(
            "Confirm Delete", f"Are you sure you want to delete '{task_name}'?"
        ):
            print(f"Deleting task: {task_name}")
            # Remove from all_tasks list
            self.all_tasks = [task for task in self.all_tasks if task[0] != task_name]
            # Here you would add the database deletion logic
            # Example: database_manager.delete_task(task_name)
            return True
        return False

    def setup_gui(self):
        filter_menu = MenuWindow(root, self.apply_filters)

        def toggle_filter_menu():
            if filter_menu.winfo_ismapped():
                filter_menu.pack_forget()
            else:
                filter_menu.pack(after=nav_bar, fill="x")

        def edit_task(task_id):
            def save_changes(task_data):
                print(f"Saving changes for task {task_id}: {task_data}")
                # Implement other saving logic here

            edit_window = EditTaskView(
                root, task_id=task_id, save_callback=save_changes
            )
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
            menu_button = CustomButton(
                nav_bar, text="Filter", command=toggle_filter_menu
            )
            menu_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Add Task Button
        add_task_button = CustomButton(nav_bar, text="+ Add Task", command=add_new_task)
        add_task_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Add Course Button - place it next to Add Task
        add_course_button = CustomButton(
            nav_bar, text="+ Add Course", command=add_new_course
        )
        add_course_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Create a container for tasks below the nav bar
        self.task_container = tk.Frame(root, bg="#E6E6E6")  # Changed to light gray
        self.task_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Sample tasks for testing
        self.all_tasks = [
            ("Assignment 1", "Complete chapter 1-3", "CS 2450", "2025-03-01"),
            ("Project Milestone", "Submit phase 1", "CS 3060", "2025-03-15"),
            ("Quiz Prep", "Study for quiz 2", "CS 2420", "2025-03-10"),
        ]

        # Create task items
        for task in self.all_tasks:
            task_item = TaskItem(
                self.task_container,
                *task,
                delete_callback=self.delete_task,
                edit_callback=edit_task,
            )
            task_item.pack(fill="x", padx=5, pady=5)

    def apply_filters(self, course, date_filter):
        """Filter tasks based on course and date criteria"""
        # Clear current tasks
        for widget in self.task_container.winfo_children():
            widget.destroy()

        # Filter tasks
        filtered_tasks = self.filter_tasks(course, date_filter)

        # Display filtered tasks
        for task in filtered_tasks:
            task_item = TaskItem(
                self.task_container,
                task[0],
                task[1],
                task[2],
                task[3],
                delete_callback=self.delete_task,
                edit_callback=self.edit_task,
            )
            task_item.pack(fill="x", padx=5, pady=5)

    def filter_tasks(self, course, date_filter):
        """Filter tasks based on criteria"""
        filtered = self.all_tasks.copy()

        # Filter by course
        if course != "All Courses":
            filtered = [task for task in filtered if task[2] == course]

        # Filter by date
        if date_filter != "All":
            today = datetime.now()
            if date_filter == "Week":
                end_date = today + timedelta(days=7)
            elif date_filter == "Month":
                end_date = today + timedelta(days=30)

            filtered = [
                task
                for task in filtered
                if self.is_date_in_range(task[3], today, end_date)
            ]

        return filtered

    def is_date_in_range(self, date_str, start_date, end_date):
        """Check if a date string falls within the given range"""
        try:
            task_date = datetime.strptime(date_str, "%Y-%m-%d")
            return start_date <= task_date <= end_date
        except ValueError:
            return False


# Run the application
TaskManagerGUI()
root.mainloop()
