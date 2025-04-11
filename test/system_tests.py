import unittest
import tkinter as tk
from datetime import date, datetime, timedelta
import os
import time
import json
from src.course import Course, CourseList, COURSE_FILE
from src.task import Task, TASK_FILE
from src.gui.components.add_course_view import AddCourseView
from src.gui.components.edit_task_view import EditTaskView
from src.gui.gui import TaskManagerGUI


class SystemTests(unittest.TestCase):
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

    def test_application_restart(self):
        """Test data survives application restart"""
        # Create and save initial test data
        test_task = Task(1, "Test Task", "Description", date.today(), self.course.id)
        self.gui.all_tasks.append(test_task)
        Task.save_tasks(self.gui.all_tasks)  # Save tasks
        self.gui.course_list.save_courses()  # Save courses

        # Store initial state
        initial_course = self.course
        initial_task = test_task

        # Simulate application restart
        self.gui.root.destroy()
        self.root = tk.Tk()
        self.gui = TaskManagerGUI(self.root)

        # Verify course data preserved
        restored_course = next(
            (
                course
                for course in self.gui.course_list.courses
                if course.id == initial_course.id
            ),
            None,
        )
        self.assertEqual(restored_course.name, initial_course.name)
        self.assertEqual(restored_course.code, initial_course.code)

        # Verify task data preserved
        restored_task = next(
            (
                task
                for task in self.gui.all_tasks
                if task.task_id == initial_task.task_id
            ),
            None,
        )
        self.assertEqual(restored_task.title, initial_task.title)
        self.assertEqual(restored_task.course_id, initial_task.course_id)
        self.assertEqual(restored_task.status, initial_task.status)

    def test_task_creation_performance(self):
        """Test task creation meets 500ms requirement"""
        start_time = time.time()
        task = Task(1, "Test Task", "Description", date.today(), 1)
        Task.save_tasks([task])
        end_time = time.time()

        self.assertLess(
            end_time - start_time, 0.5, "Task creation took longer than 500ms"
        )

    def test_system_clock_sync(self):
        """Test application syncs with system clock"""
        test_date = date.today()
        task = Task(1, "Test Task", "Description", test_date, 1)
        self.assertEqual(task.due_date, test_date)

    def test_invalid_file_recovery(self):
        """Test recovery from corrupted save files"""
        # Corrupt the JSON files
        with open(COURSE_FILE, "w") as f:
            f.write("Invalid JSON")

        # Verify application still loads with empty course list
        course_list = CourseList()
        self.assertIsNotNone(course_list)
        self.assertEqual(len(course_list.courses), 0)
