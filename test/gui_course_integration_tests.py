import unittest
import tkinter as tk
from datetime import date, timedelta
import os
from src.course import Course, CourseList, COURSE_FILE
from src.task import Task, TASK_FILE
from src.gui.components.add_course_view import AddCourseView
from src.gui.components.edit_task_view import EditTaskView
from src.gui.gui import TaskManagerGUI


class IntegrationGUITests(unittest.TestCase):
    def setUp(self):
        # Clean up any existing test files
        if os.path.exists(COURSE_FILE):
            os.remove(COURSE_FILE)
        if os.path.exists(TASK_FILE):
            os.remove(TASK_FILE)

        # Create test root window
        self.root = tk.Tk()

        # Create TaskManagerGUI instance
        self.gui = TaskManagerGUI(self.root)

        # Create sample course
        self.course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            date.today(),
            date.today() + timedelta(days=30),
        )
        self.gui.course_list.add_course(self.course)

    def tearDown(self):
        # Clean up
        if os.path.exists(COURSE_FILE):
            os.remove(COURSE_FILE)
        if os.path.exists(TASK_FILE):
            os.remove(TASK_FILE)
        self.root.destroy()

    def test_add_task_updates_gui(self):
        """Test that adding a task updates the GUI"""
        # Get initial task count
        initial_tasks = len(self.gui.task_container.winfo_children())

        # Create and add new task
        task = Task(1, "Test Task", "Description", date.today(), self.course.id)
        self.gui.all_tasks.append(task)
        Task.save_tasks(self.gui.all_tasks)

        # Refresh GUI
        self.gui.setup_gui()

        # Verify task count increased
        final_tasks = len(self.gui.task_container.winfo_children())
        self.assertEqual(final_tasks, initial_tasks + 1)

    def test_delete_task_updates_gui(self):
        """Test that deleting a task updates the GUI"""
        # Add task first
        task = Task(1, "Test Task", "Description", date.today(), self.course.id)
        self.gui.all_tasks.append(task)
        Task.save_tasks(self.gui.all_tasks)
        self.gui.setup_gui()

        # Get initial task count
        initial_tasks = len(self.gui.task_container.winfo_children())

        # Delete task
        self.gui.delete_task("Test Task")

        # Verify task was removed from GUI
        final_tasks = len(self.gui.task_container.winfo_children())
        self.assertEqual(final_tasks, initial_tasks - 1)
