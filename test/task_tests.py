import unittest
from unittest.mock import patch, mock_open
import json
from src.task import Task
from src.main import (
    load_tasks,
    save_tasks,
    filter_tasks_by_due_date,
    filter_tasks_by_course,
    sort_tasks_by_due_date,
    sort_tasks_by_course_id,
)


class TestTaskMethods(unittest.TestCase):

    def test_create_task(self):
        # Test creating a task
        task = Task.create_task(1, "Test Task", "This is a test task", "2023-06-01", 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "This is a test task")
        self.assertEqual(task.due_date, "2023-06-01")
        self.assertEqual(task.course_id, 1)
        self.assertEqual(task.status, "pending")

    def test_get_task_details(self):
        # Test getting task details
        task = Task(1, "Test Task", "This is a test task", "2023-06-01", 1)
        details = task.get_task_details()
        self.assertEqual(details["title"], "Test Task")
        self.assertEqual(details["description"], "This is a test task")
        self.assertEqual(details["due_date"], "2023-06-01")
        self.assertEqual(details["course_id"], 1)
        self.assertEqual(details["status"], "pending")

    def test_update_task(self):
        # Test updating a task
        task = Task(1, "Test Task", "This is a test task", "2023-06-01", 1)
        task.update_task(
            title="Updated Task",
            description="This is an updated task",
            due_date="2023-07-01",
        )
        self.assertEqual(task.title, "Updated Task")
        self.assertEqual(task.description, "This is an updated task")
        self.assertEqual(task.due_date, "2023-07-01")

    def test_mark_complete(self):
        # Test marking a task as complete
        task = Task(1, "Test Task", "This is a test task", "2023-06-01", 1)
        task.mark_complete()
        self.assertEqual(task.status, "completed")

    def test_mark_pending(self):
        # Test marking a task as pending
        task = Task(1, "Test Task", "This is a test task", "2023-06-01", 1)
        task.mark_complete()
        task.mark_pending()
        self.assertEqual(task.status, "pending")

    def test_delete_task(self):
        # Test deleting a task from a list
        task1 = Task(1, "Test Task 1", "This is a test task 1", "2023-06-01", 1)
        task2 = Task(2, "Test Task 2", "This is a test task 2", "2023-06-02", 1)
        tasks_list = [task1, task2]
        tasks_list = Task.delete_task(tasks_list, 1)
        self.assertNotIn(task1, tasks_list)
        self.assertIn(task2, tasks_list)
        self.assertEqual(len(tasks_list), 1)

    def test_update_task_with_invalid_field(self):
        # Test updating a task with an invalid field
        task = Task(1, "Test Task", "This is a test task", "2023-06-01", 1)
        task.update_task(invalid_field="Invalid")
        self.assertFalse(hasattr(task, "invalid_field"))

    def test_create_task_with_empty_title(self):
        # Test creating a task with an empty title
        task = Task.create_task(1, "", "This is a test task", "2023-06-01", 1)
        self.assertEqual(task.title, "")

    def test_create_task_with_empty_description(self):
        # Test creating a task with an empty description
        task = Task.create_task(1, "Test Task", "", "2023-06-01", 1)
        self.assertEqual(task.description, "")

    def test_create_task_with_empty_due_date(self):
        # Test creating a task with an empty due date
        task = Task.create_task(1, "Test Task", "This is a test task", "", 1)
        self.assertEqual(task.due_date, "")

    def test_create_task_with_invalid_course_id(self):
        # Test creating a task with an invalid course ID
        task = Task.create_task(1, "Test Task", "This is a test task", "2023-06-01", -1)
        self.assertEqual(task.course_id, -1)

    def test_mark_complete_on_already_completed_task(self):
        # Test marking a task as complete when it is already completed
        task = Task(
            1, "Test Task", "This is a test task", "2023-06-01", 1, status="completed"
        )
        task.mark_complete()
        self.assertEqual(task.status, "completed")

    def test_mark_pending_on_already_pending_task(self):
        # Test marking a task as pending when it is already pending
        task = Task(
            1, "Test Task", "This is a test task", "2023-06-01", 1, status="pending"
        )
        task.mark_pending()
        self.assertEqual(task.status, "pending")

    def test_delete_non_existent_task(self):
        # Test deleting a non-existent task from a list
        task1 = Task(1, "Test Task 1", "This is a test task 1", "2023-06-01", 1)
        tasks_list = [task1]
        tasks_list = Task.delete_task(tasks_list, 2)
        self.assertIn(task1, tasks_list)
        self.assertEqual(len(tasks_list), 1)


class TestSortingMethods(unittest.TestCase):

    @patch("src.main.save_tasks")
    @patch("src.main.open", new_callable=mock_open)
    def test_sort_tasks_by_due_date(self, mock_file, mock_save_tasks):
        # Test sorting tasks by due date
        task1 = Task(1, "Task A", "This is Task A", "2023-06-01", 1)
        task2 = Task(2, "Task B", "This is Task B", "2023-06-11", 1)
        task3 = Task(3, "Task C", "This is Task C", "2023-06-05", 1)
        mock_tasks = [task1.__dict__, task2.__dict__, task3.__dict__]

        # Mock file reading with JSON data
        mock_file.return_value.read.return_value = json.dumps(mock_tasks)
        sort_tasks_by_due_date()
        mock_save_tasks.assert_called_once()
        sorted_tasks = mock_save_tasks.call_args[0][0]

        self.assertEqual(sorted_tasks[0]["task_id"], 1)
        self.assertEqual(sorted_tasks[1]["task_id"], 3)
        self.assertEqual(sorted_tasks[2]["task_id"], 2)

    @patch("src.main.save_tasks")
    @patch("src.main.open", new_callable=mock_open)
    def test_sort_tasks_by_course_id(self, mock_file, mock_save_tasks):
        # Test sorting tasks by course id
        task1 = Task(1, "Task A", "This is Task A", "2023-06-01", 4)
        task2 = Task(2, "Task B", "This is Task B", "2023-06-11", 8)
        task3 = Task(3, "Task C", "This is Task C", "2023-06-05", 2)
        mock_tasks = [task1.__dict__, task2.__dict__, task3.__dict__]

        # Mock file reading with JSON data
        mock_file.return_value.read.return_value = json.dumps(mock_tasks)
        sort_tasks_by_course_id()
        mock_save_tasks.assert_called_once()
        sorted_tasks = mock_save_tasks.call_args[0][0]

        self.assertEqual(sorted_tasks[0]["course_id"], 2)
        self.assertEqual(sorted_tasks[1]["course_id"], 4)
        self.assertEqual(sorted_tasks[2]["course_id"], 8)

    @patch("src.main.save_tasks")
    @patch("src.main.open", new_callable=mock_open)
    def test_sort_tasks_by_due_date_all_same(self, mock_file, mock_save_tasks):
        task1 = Task(1, "Task A", "This is Task A", "2023-06-01", 1)
        task2 = Task(1, "Task A", "This is Task A", "2023-06-01", 2)
        task3 = Task(1, "Task A", "This is Task A", "2023-06-01", 3)
        mock_tasks = [task1.__dict__, task2.__dict__, task3.__dict__]

        # Mock file reading with JSON data
        mock_file.return_value.read.return_value = json.dumps(mock_tasks)
        sort_tasks_by_due_date()
        mock_save_tasks.assert_called_once()
        sorted_tasks = mock_save_tasks.call_args[0][0]

        self.assertEqual(sorted_tasks[0]["task_id"], 1)
        self.assertEqual(sorted_tasks[1]["task_id"], 1)
        self.assertEqual(sorted_tasks[2]["task_id"], 1)

    @patch("src.main.save_tasks")
    @patch("src.main.open", new_callable=mock_open)
    def test_sort_tasks_by_course_id_all_same(self, mock_file, mock_save_tasks):
        task1 = Task(1, "Task A", "This is Task A", "2023-06-01", 1)
        task2 = Task(2, "Task A", "This is Task A", "2023-06-01", 1)
        task3 = Task(3, "Task A", "This is Task A", "2023-06-01", 1)
        mock_tasks = [task1.__dict__, task2.__dict__, task3.__dict__]

        # Mock file reading with JSON data
        mock_file.return_value.read.return_value = json.dumps(mock_tasks)
        sort_tasks_by_due_date()
        mock_save_tasks.assert_called_once()
        sorted_tasks = mock_save_tasks.call_args[0][0]

        self.assertEqual(sorted_tasks[0]["course_id"], 1)
        self.assertEqual(sorted_tasks[1]["course_id"], 1)
        self.assertEqual(sorted_tasks[2]["course_id"], 1)


if __name__ == "__main__":
    unittest.main()
