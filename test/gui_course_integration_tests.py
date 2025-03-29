import unittest
import tkinter as tk
from datetime import date
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
        self.gui = TaskManagerGUI()

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
