import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog  # Add this import at the top of the file
import sys
import os
from datetime import datetime, timedelta, date
import json


# Add src directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
sys.path.append(src_dir)

# Define assets directory
assets_dir = os.path.join(current_dir, "assets")

# Local imports
from .components.custom_button import CustomButton
from .components.task_visual import TaskItem
from .components.filter_menu import MenuWindow
from .components.edit_task_view import EditTaskView
from .components.add_task_view import AddTaskView
from .components.add_course_view import AddCourseView

# Add src directory to path if not already there
src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if src_dir not in sys.path:
    sys.path.append(src_dir)

from course import Course, CourseList
from task import Task


def resize_image(image_path, width, height):
    """Resize an image while maintaining aspect ratio"""
    img = Image.open(image_path)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)


class TaskManagerGUI:
    def __init__(self, root=None):

        self.root = root
        self.course_list = CourseList()
        self.all_tasks = Task.load_tasks()
        self.task_container = None
        self.filter_menu = None
        self.next_task_id = len(self.all_tasks) + 1
        self.nav_bar = tk.Frame(root, bg="#B6EEFB", height=75)
        self.nav_bar.pack(fill=tk.X)

        # Only setup GUI if root is provided
        if root:
            self.setup_gui()

    def save_tasks(self):
        self.course_list.save_courses()

    """
    def save_new_course(self, course_data):
        try:
            # Generate a new course ID (simple increment for now)
            new_id = len(self.course_list.courses) + 1

            # Create new Course instance
            new_course = Course(
                id=new_id,
                name=course_data["name"],
                description=course_data["description"],
                code=course_data["code"],
                start_date=course_data["start_date"],
                end_date=course_data["end_date"],
            )

            # Check if course already exists
            for course in self.course_list.courses:
                if new_course.name == course.name:
                    raise ValueError(
                        f"Course name \"{course_data['name']}\" already exists"
                    )
                elif new_course.code == course.code:
                    raise ValueError(
                        f"Course code \"{course_data['code']}\" already exists"
                    )

            # Add to CourseList
            self.course_list.add_course(new_course)
            messagebox.showinfo(
                "Success", f"Course \"{course_data['name']}\" added successfully!"
            )

        except ValueError as e:
            messagebox.showerror("Error", str(e))
    """

    def add_new_course(self):
        """Add a new course and display it in the course list"""

        def save_new_course(course_data):
            try:

                # Generate a new course ID (simple increment for now)
                new_id = len(self.course_list.courses) + 1

                # Create new Course instance
                new_course = Course(
                    id=new_id,
                    name=course_data["name"],
                    description=course_data["description"],
                    code=course_data["code"],
                    start_date=course_data["start_date"],
                    end_date=course_data["end_date"],
                )

                # Check if course already exists
                for course in self.course_list.courses:
                    if new_course.name == course.name:
                        raise ValueError(
                            f"Course name \"{course_data['name']}\" already exists"
                        )
                    elif new_course.code == course.code:
                        raise ValueError(
                            f"Course code \"{course_data['code']}\" already exists"
                        )

                # Add to CourseList
                self.course_list.add_course(new_course)
                messagebox.showinfo(
                    "Success", f"Course \"{course_data['name']}\" added successfully!"
                )

            except ValueError as e:
                messagebox.showerror("Error", str(e))

        add_window = AddCourseView(self.root, save_callback=save_new_course)
        add_window.grab_set()

    def update_course_filters(self):
        """Update the course filter dropdown with current courses"""
        course_codes = [course.code for course in self.course_list.courses]
        # Update filter menu courses - assuming filter_menu is accessible
        self.filter_menu.update_courses(course_codes)

    def save_new_task(self, task_data):
        try:
            # Create new Task instance
            new_task = Task(
                task_id=self.next_task_id,
                title=task_data["name"],
                description=task_data["description"],
                due_date=date.fromisoformat(task_data["due_date"]),
                course_id=task_data["course"],
                status=task_data["status"],
            )

            # Check if task already exists
            for task in self.all_tasks:
                if (
                    new_task.title == task.title
                    and new_task.course_id == task.course_id
                ):
                    raise ValueError(
                        f"Task name \"{task_data['name']}\" in course \"{task_data['course']}\" already exists"
                    )

            # Add to tasks list and update next_task_id
            self.all_tasks.append(new_task)
            self.next_task_id += 1

            # Save tasks to JSON
            Task.save_tasks(self.all_tasks)

            self.display_new_task(new_task, task_data)

            messagebox.showinfo(
                "Success", f"Task '{task_data['name']}' added successfully!"
            )

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def display_new_task(self, new_task, task_data):
        # Create new task item
        task_item = TaskItem(
            self.task_container,
            new_task.title,
            new_task.description,
            task_data["course"],  # Use selected course
            new_task.due_date,
            delete_callback=self.delete_task,
            edit_callback=self.edit_task,
        )

        # Display new task item in UI
        task_item.pack(fill="x", padx=5, pady=5)

    def add_new_task(self):
        """Add a new task and display it in the task container"""

        def save_new_task(task_data):
            try:
                # Create new Task instance
                new_task = Task(
                    task_id=self.next_task_id,
                    title=task_data["name"],
                    description=task_data["description"],
                    due_date=date.fromisoformat(task_data["due_date"]),
                    course_id=task_data["course"],
                    status=task_data["status"],
                )

                # Check if task already exists
                for task in self.all_tasks:
                    if (
                        new_task.title == task.title
                        and new_task.course_id == task.course_id
                    ):
                        raise ValueError(
                            f"Task name \"{task_data['name']}\" in course \"{task_data['course']}\" already exists"
                        )

                # Add to tasks list and update next_task_id
                self.all_tasks.append(new_task)
                self.next_task_id += 1

                # Save tasks to JSON
                Task.save_tasks(self.all_tasks)

                # Create new task item
                task_item = TaskItem(
                    self.task_container,
                    new_task.title,
                    new_task.description,
                    task_data["course"],  # Use selected course
                    new_task.due_date,
                    delete_callback=self.delete_task,
                    edit_callback=self.edit_task,
                )

                # Display new task item in UI
                task_item.pack(fill="x", padx=5, pady=5)

                messagebox.showinfo(
                    "Success", f"Task '{task_data['name']}' added successfully!"
                )

            except ValueError as e:
                messagebox.showerror("Error", str(e))

        add_window = AddTaskView(self.root, save_callback=save_new_task)

        course_codes = [course.code for course in self.course_list.courses]
        add_window.update_courses(course_codes)

        add_window.grab_set()

    def apply_filters(self, course):
        """Apply filters to tasks and update display"""
        # Clear current tasks
        for widget in self.task_container.winfo_children():
            widget.destroy()

        # Filter tasks
        filtered_tasks = [
            task
            for task in self.all_tasks
            if course == "All Courses" or task.course_id == course
        ]

        # Display filtered tasks
        for task in filtered_tasks:
            task_item = TaskItem(
                self.task_container,
                task.title,
                task.description,
                task.course_id,
                task.due_date,
                delete_callback=self.delete_task,
                edit_callback=self.edit_task,
            )
            task_item.pack(fill="x", padx=5, pady=5)

    def display_filtered_tasks(self, filtered_tasks):
        # Display filtered tasks
        for task in filtered_tasks:
            task_item = TaskItem(
                self.task_container,
                task.title,
                task.description,
                task.course_id,
                task.due_date,
                delete_callback=self.delete_task,
                edit_callback=self.edit_task,
            )
            task_item.pack(fill="x", padx=5, pady=5)

    def toggle_filter_menu(self):
        if self.filter_menu.winfo_ismapped():
            self.filter_menu.pack_forget()
        else:
            self.filter_menu.pack(after=self.nav_bar, fill="x")

    def setup_gui(self):
        # Create filter menu with reference to self
        self.filter_menu = MenuWindow(self.root, self.apply_filters)

        # Update the filter menu course list
        self.update_course_filters()

        #### This function goes unused. Delete if unneeded
        # def edit_task(task_id):
        #     def save_changes(task_data):
        #         print(f"Saving changes for task {task_id}: {task_data}")
        #         # Implement other saving logic here

        def edit_task(task_id):
            def save_changes(task_data):
                print(f"Saving changes for task {task_id}: {task_data}")
                # Implement other saving logic here

            edit_window = EditTaskView(
                self.root, task_id=task_id, save_callback=save_changes
            )
            edit_window.grab_set()  # Make window modal

        # Menu Button with icon
        try:
            menu_icon = resize_image(os.path.join(assets_dir, "menu.png"), 20, 20)
            menu_button = tk.Button(
                nav_bar,
                image=menu_icon,
                command=self.toggle_filter_menu,
                bg="#B6EEFB",
                relief="flat",
                bd=0,
            )
            menu_button.image = menu_icon  # Keep a reference
            menu_button.pack(side=tk.LEFT, padx=10, pady=10)
        except Exception as e:
            # Fallback to text button if image fails to load
            menu_button = CustomButton(
                self.nav_bar, text="Filter", command=self.toggle_filter_menu
            )
            menu_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Add Task Button (now using the class method)
        add_task_button = CustomButton(
            self.nav_bar, text="+ Add Task", command=self.add_new_task
        )
        add_task_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Add Course Button - place it next to Add Task
        add_course_button = CustomButton(
            self.nav_bar, text="+ Add Course", command=self.add_new_course
        )
        add_course_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Add Export Tasks Button
        export_tasks_button = CustomButton(
            self.nav_bar, text="Export Tasks", command=self.export_tasks
        )
        export_tasks_button.pack(side=tk.RIGHT, padx=10, pady=10)

        import_tasks_button = CustomButton(
            self.nav_bar, text="Import Tasks", command=self.import_tasks
        )
        import_tasks_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Create a container for tasks below the nav bar
        self.task_container = tk.Frame(self.root, bg="#E6E6E6")
        self.task_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Display existing tasks if any
        for task in self.all_tasks:
            task_item = TaskItem(
                self.task_container,
                task.title,
                task.description,
                "CS 2450",  # TODO: Get actual course code
                task.due_date,
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

    def delete_task(self, task_name):
        """Delete a task after confirmation"""
        if messagebox.askyesno(
            "Confirm Delete", f"Are you sure you want to delete '{task_name}'?"
        ):
            # Find and remove the task from all_tasks list
            self.all_tasks = [
                task for task in self.all_tasks if task.title != task_name
            ]
            # Save updated task list to JSON
            Task.save_tasks(self.all_tasks)

            self.setup_gui()
            return True  # Return True to trigger widget destruction
        return False

    def save_changes(self, task_data, task_name):
        task_to_edit = next(
            (task for task in self.all_tasks if task.title == task_name), None
        )
        if not task_to_edit:
            return

        # Update task attributes
        task_to_edit.title = task_data["name"]
        task_to_edit.description = task_data["description"]
        task_to_edit.due_date = task_data["due_date"]
        task_to_edit.status = task_data["status"]

        # Save to JSON
        Task.save_tasks(self.all_tasks)

        # Refresh the task display
        for widget in self.task_container.winfo_children():
            widget.destroy()

        # Redisplay all tasks
        for task in self.all_tasks:
            task_item = TaskItem(
                self.task_container,
                task.title,
                task.description,
                task_data["course"],  # Use selected course
                task.due_date,
                delete_callback=self.delete_task,
                edit_callback=self.edit_task,
            )
            task_item.pack(fill="x", padx=5, pady=5)

        messagebox.showinfo("Success", "Task updated successfully!")

    def edit_task(self, task_name):
        """Edit an existing task"""
        # Find the task to edit
        task_to_edit = next(
            (task for task in self.all_tasks if task.title == task_name), None
        )
        if not task_to_edit:
            return

        # Open edit window with current task data
        edit_window = EditTaskView(
            self.root,
            task_id=task_to_edit.task_id,
            task_data={
                "name": task_to_edit.title,
                "description": task_to_edit.description,
                "due_date": task_to_edit.due_date,
                "status": task_to_edit.status,
                "course": "CS 2450",  # TODO: Get actual course
            },
            save_callback=self.save_changes,
        )
        edit_window.grab_set()

    def export_tasks(self):
        """Export tasks to a custom directory as a JSON file."""
        # Open a directory selection dialog
        directory = filedialog.askdirectory(title="Select Export Directory")
        if not directory:
            return  # User canceled the dialog

        try:
            # Call the export_tasks function from task.py
            Task.export_tasks(self.all_tasks, directory)
            messagebox.showinfo(
                "Success", f"Tasks exported successfully to {directory}"
            )
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def import_tasks(self):
        """Import tasks from a user-selected JSON file."""
        file = filedialog.askopenfile(title="Select file to import")
        if file is None:
            return  # user canceled the dialog
        if not file.name.endswith(".json"):
            messagebox.showerror("Error", "File is not a JSON file.")
            return
        try:
            Task.load_tasks_from_file(file)
            messagebox.showinfo("Success", "Tasks imported successfully")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


def main():
    root = tk.Tk()
    root.title("Course Task Manager")
    root.geometry("1500x900")
    root.configure(background="#E6E6E6")

    app = TaskManagerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
