import unittest
from src.course import Course, CourseList, COURSE_FILE
from src.task import Task, TASK_FILE
import os
import datetime as date


class TestCourseTaskIntegration(unittest.TestCase):
    def setUp(self):
        # cleaning up the data files before each test
        if os.path.exists(COURSE_FILE):
            os.remove(COURSE_FILE)
        if os.path.exists(TASK_FILE):
            os.remove(TASK_FILE)
        self.course_list = CourseList()
        # starting with a course because almost all tests require a course
        self.course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            date.date.today(),
            date.date.today() + date.timedelta(days=30),
        )
        self.course_list.add_course(self.course)

    def tearDown(self):
        # Clean up test data files after each test
        if os.path.exists(COURSE_FILE):
            os.remove(COURSE_FILE)
        if os.path.exists(TASK_FILE):
            os.remove(TASK_FILE)

    def test_add_task_to_course(self):
        # Test adding a task to a course
        task = Task(1, "Test Task", "This is a test task", date.date.today(), 1)
        # saving it to the task file
        Task.save_tasks([task])

        loaded_tasks = Task.load_tasks()
        self.assertEqual(len(loaded_tasks), 1)
        # checking if the task is "in" the course
        self.assertEqual(loaded_tasks[0].course_id, self.course.id)

    def test_delete_course_with_tasks(self):
        task = Task(1, "Test Task", "This is a test task", date.date.today(), 1)
        # saving it to the task file
        Task.save_tasks([task])

        # delete the course
        self.course_list.delete_course(self.course.id)

        # Verify the course was deleted
        loaded_courses = self.course_list.load_courses()
        self.assertEqual(len(loaded_courses), 0)

        # Verify the task was deleted
        loaded_tasks = Task.load_tasks()
        self.assertEqual(len(loaded_tasks), 0)

    def test_edit_course_with_tasks(self):
        """Test that tasks remain associated when editing a course"""
        # Create and save a task
        task = Task(1, "Test Task", "This is a test task", date.date.today(), 1)
        Task.save_tasks([task])

        # Edit the course
        course = self.course_list.courses[0]
        course.name = "Updated Course"
        course.code = "UC101"
        self.course_list.save_courses()

        # Verify task still references correct course
        loaded_tasks = Task.load_tasks()
        self.assertEqual(len(loaded_tasks), 1)
        self.assertEqual(loaded_tasks[0].course_id, 1)

    def test_task_with_invalid_course_id(self):
        """Test handling tasks with non-existent course IDs"""
        # Create task with non-existent course ID
        task = Task(1, "Test Task", "Test Description", date.date.today(), 999)
        Task.save_tasks([task])

        # Load and verify task saved but orphaned
        loaded_tasks = Task.load_tasks()
        self.assertEqual(len(loaded_tasks), 1)
        self.assertEqual(loaded_tasks[0].course_id, 999)

        # Verify course list doesn't contain invalid ID
        course_ids = [c.id for c in self.course_list.courses]
        self.assertNotIn(999, course_ids)

    def test_persistence_across_operations(self):
        """Test data integrity across multiple operations"""
        # Add initial task
        task1 = Task(1, "Task 1", "First task", date.date.today(), 1)
        Task.save_tasks([task1])

        # Delete course and verify task deleted
        self.course_list.delete_course(1)
        self.assertEqual(len(Task.load_tasks()), 0)

        # Create new course and task
        new_course = Course(
            2,
            "New Course",
            "New Description",
            "NC101",
            date.date.today(),
            date.date.today() + date.timedelta(days=30),
        )
        self.course_list.add_course(new_course)

        task2 = Task(2, "Task 2", "Second task", date.date.today(), 2)
        Task.save_tasks([task2])

        # Verify final state
        self.assertEqual(len(self.course_list.courses), 1)
        self.assertEqual(len(Task.load_tasks()), 1)
        self.assertEqual(Task.load_tasks()[0].course_id, 2)

    def test_task_date_validation(self):
        """Test task dates relative to course dates"""
        # Create task due after course end date
        future_date = date.date.today() + date.timedelta(days=60)
        task = Task(1, "Late Task", "Task due after course ends", future_date, 1)
        Task.save_tasks([task])

        # Load and verify task saved despite being due after course ends
        loaded_tasks = Task.load_tasks()
        self.assertEqual(len(loaded_tasks), 1)
        course = self.course_list.courses[0]
        self.assertTrue(loaded_tasks[0].due_date > course.end_date)

    def test_multiple_tasks_per_course(self):
        """Test handling multiple tasks associated with one course"""
        # Create multiple tasks for same course
        task1 = Task(1, "Task 1", "First task", date.date.today(), self.course.id)
        task2 = Task(2, "Task 2", "Second task", date.date.today(), self.course.id)
        Task.save_tasks([task1, task2])

        # Verify both tasks saved correctly
        loaded_tasks = Task.load_tasks()
        self.assertEqual(len(loaded_tasks), 2)
        self.assertTrue(all(t.course_id == self.course.id for t in loaded_tasks))

    def test_task_before_course_start(self):
        """Test creating task with due date before course starts"""
        past_date = date.date.today() - date.timedelta(days=10)
        task = Task(
            1, "Early Task", "Due before course starts", past_date, self.course.id
        )
        Task.save_tasks([task])

        loaded_tasks = Task.load_tasks()
        self.assertEqual(len(loaded_tasks), 1)
        self.assertTrue(loaded_tasks[0].due_date < self.course.start_date)

    def test_update_course_dates_with_tasks(self):
        """Test updating course dates affects existing tasks"""
        task = Task(1, "Test Task", "Description", date.date.today(), self.course.id)
        Task.save_tasks([task])

        # Update course dates
        new_start = date.date.today() + date.timedelta(days=60)
        new_end = new_start + date.timedelta(days=30)
        self.course.start_date = new_start
        self.course.end_date = new_end
        self.course_list.save_courses()

        # Verify task still exists and dates unchanged
        loaded_tasks = Task.load_tasks()
        self.assertEqual(len(loaded_tasks), 1)
        self.assertEqual(loaded_tasks[0].due_date, date.date.today())

    def test_concurrent_course_task_updates(self):
        """Test handling concurrent updates to courses and tasks"""
        # Create initial task
        task = Task(1, "Test Task", "Description", date.date.today(), self.course.id)
        Task.save_tasks([task])

        # Modify course and task "concurrently"
        self.course.name = "Updated Course"
        self.course_list.save_courses()
        task.title = "Updated Task"
        Task.save_tasks([task])

        # Verify both updates persisted
        loaded_courses = self.course_list.load_courses()
        loaded_tasks = Task.load_tasks()
        self.assertEqual(loaded_courses[0].name, "Updated Course")
        self.assertEqual(loaded_tasks[0].title, "Updated Task")
        self.assertEqual(loaded_tasks[0].course_id, self.course.id)
