import unittest
from unittest.mock import patch, mock_open
import json
from datetime import date
from src.task import Task


class TestTaskMethods(unittest.TestCase):

    def test_create_task(self):
        # Test creating a task
        print("Running test to create a task")
        task = Task.create_task(
            1, "Test Task", "This is a test task", date.fromisoformat("2023-06-01"), 1
        )
        print("Task created:", end=" ")
        print(task)
        self.assertEqual(
            task.title, "Test Task", "ERROR: task.title was created unsuccessfully"
        )
        self.assertEqual(
            task.description,
            "This is a test task",
            "ERROR: task.description was created unsuccessfully",
        )
        self.assertEqual(
            task.due_date,
            date.fromisoformat("2023-06-01"),
            "ERROR: task.due_date was created unsuccessfully",
        )
        self.assertEqual(
            task.course_id, 1, "ERROR: task.course_id was created unsuccessfully"
        )
        self.assertEqual(
            task.status, "pending", "ERROR: task.status flag was created unsuccessfully"
        )
        print("Task successfully created")
        print()

    def test_get_task_details(self):
        # Test getting task details
        print("Running test to get task details")
        task = Task(
            1, "Test Task", "This is a test task", date.fromisoformat("2023-06-01"), 1
        )
        print("Task created:", end=" ")
        print(task)
        details = task.to_dict()
        self.assertEqual(
            details["title"],
            "Test Task",
            "ERROR: unable to get task.title, or field is incorrect",
        )
        self.assertEqual(
            details["description"],
            "This is a test task",
            "ERROR: unable to get task.description, or field is incorrect",
        )
        # date should be a string here, and nowhere else, because the method we are testing
        # is for preparing the task for JSON saving. JSON cannot save date objects, so we
        # make it into an ISO format string.
        self.assertEqual(
            details["due_date"],
            "2023-06-01",
            "ERROR: unable to get task.due_date, or field is incorrect",
        )
        self.assertEqual(
            details["course_id"],
            1,
            "ERROR: unable to get task.course_id, or field is incorrect",
        )
        self.assertEqual(
            details["status"],
            "pending",
            "ERROR: unable to get task.status flag, or field is incorrect",
        )
        print("Details succefully got")
        print()

    def test_update_task(self):
        # Test updating a task
        print("Running test to update a task")
        task = Task(
            1, "Test Task", "This is a test task", date.fromisoformat("2023-06-01"), 1
        )
        print("Task created:", end=" ")
        print(task)
        task.update_task(
            title="Updated Task",
            description="This is an updated task",
            due_date=date.fromisoformat("2023-07-01"),
        )
        print("Updated Task:", end=" ")
        print(task)
        self.assertEqual(
            task.title, "Updated Task", "ERROR: unable to change task.title"
        )
        self.assertEqual(
            task.description,
            "This is an updated task",
            "ERROR: unable to change task.description",
        )
        self.assertEqual(
            task.due_date,
            date.fromisoformat("2023-07-01"),
            "ERROR: unable to change task.due_date",
        )
        print("Task successfully updated")
        print()

    def test_mark_complete(self):
        # Test marking a task as complete
        print('Running test to mark a task asa "complete"')
        task = Task(
            1, "Test Task", "This is a test task", date.fromisoformat("2023-06-01"), 1
        )
        print("Task created:", end=" ")
        print(task)
        task.mark_complete()
        print("Updated Task:", end=" ")
        print(task)
        self.assertEqual(
            task.status, "completed", 'ERROR: Unable to mark task as "completed"'
        )
        print("Task successfully updated")
        print()

    def test_mark_pending(self):
        # Test marking a task as pending
        print('Running test to mark a task as "pending"')
        task = Task(
            1, "Test Task", "This is a test task", date.fromisoformat("2023-06-01"), 1
        )
        task.mark_complete()
        print('Task created and pre-marked as "complete":', end=" ")
        print(task)
        task.mark_pending()
        print("Updated Task:", end=" ")
        print(task)
        self.assertEqual(
            task.status, "pending", 'ERROR: Unable to mark task as "pending"'
        )
        print("Task successfully updated")
        print()

    def test_delete_task(self):
        # Test deleting a task from a list
        print("Running test to delete a task from a list")
        task1 = Task(
            1,
            "Test Task 1",
            "This is a test task 1",
            date.fromisoformat("2023-06-01"),
            1,
        )
        task2 = Task(
            2,
            "Test Task 2",
            "This is a test task 2",
            date.fromisoformat("2023-06-02"),
            1,
        )
        print("Task1 created:", end=" ")
        print(task1)
        print("Task2 created:", end=" ")
        print(task2)
        tasks_list = [task1, task2]
        tasks_list = Task.delete_task(tasks_list, 1)
        self.assertNotIn(task1, tasks_list, "ERROR: task1 should not be in the list")
        self.assertIn(task2, tasks_list, "ERROR: task2 should not be missing")
        self.assertEqual(
            len(tasks_list),
            1,
            "ERROR: tasks_list should only have 1 object, but "
            + str(len(tasks_list))
            + "was found",
        )
        print("Task successfully deleted")
        print()

    def test_update_task_with_invalid_field(self):
        # Test updating a task with an invalid field
        print(
            "Running test to update a task with an invalid field, which should not be possible"
        )
        task = Task(
            1, "Test Task", "This is a test task", date.fromisoformat("2023-06-01"), 1
        )
        print("Task created:", end=" ")
        print(task)
        task.update_task(invalid_field="Invalid")
        self.assertFalse(
            hasattr(task, "invalid_field"), "ERROR: task should not have invalid fields"
        )
        print("Success! invalid field was not updated, nor does it exist")
        print()

    def test_create_task_with_empty_title(self):
        # Test creating a task with an empty title
        print("Running test to create task with an empty title")
        task = Task.create_task(
            1, "", "This is a test task", date.fromisoformat("2023-06-01"), 1
        )
        print("Task created:", end=" ")
        print(task)
        self.assertEqual(
            task.title, "", "ERROR: Unable to create task with empty title"
        )
        print("Task successfully created")
        print()

    def test_create_task_with_empty_description(self):
        # Test creating a task with an empty description
        print("Running test to create a task with an empty description")
        task = Task.create_task(1, "Test Task", "", date.fromisoformat("2023-06-01"), 1)
        print("Task created:", end=" ")
        print(task)
        self.assertEqual(
            task.description, "", "ERROR: Unable to create task with empty description"
        )
        print("Task successfully created")
        print()

    def make_task_with_str_dates(self):
        task = Task(1, "Test Task", "This is a test task", "", 1)

    def test_create_task_with_empty_due_date(self):
        # Test creating a task with a strinh due date
        print("Running test to add a task with string date")
        self.assertRaises(TypeError, self.make_task_with_str_dates)
        print("Task caused a TypeError correctly")
        print()

    def test_create_task_with_invalid_course_id(self):
        # Test creating a task with an invalid course ID
        print("Running test to create a task with an invalid course_id")
        task = Task.create_task(
            1, "Test Task", "This is a test task", date.fromisoformat("2023-06-01"), -1
        )
        print("Task created:", end=" ")
        print(task)
        self.assertEqual(
            task.course_id, -1, "ERROR: Unable to create task with invalid course_id"
        )
        print("Task successfully created")
        print()

    def test_mark_complete_on_already_completed_task(self):
        # Test marking a task as complete when it is already completed
        print('Running test to mark "complete" on a completed task')
        task = Task(
            1,
            "Test Task",
            "This is a test task",
            date.fromisoformat("2023-06-01"),
            1,
            status="completed",
        )
        print("Task created:", end=" ")
        print(task)
        task.mark_complete()
        print("Updated Task:", end=" ")
        print(task)
        self.assertEqual(
            task.status,
            "completed",
            'ERROR: status should be "completed", but marked as "pending"',
        )
        print("Task successfully updated")
        print()

    def test_mark_pending_on_already_pending_task(self):
        # Test marking a task as pending when it is already pending
        print('Running test to mark "pending" on a pending task')
        task = Task(
            1,
            "Test Task",
            "This is a test task",
            date.fromisoformat("2023-06-01"),
            1,
            status="pending",
        )
        print("Task created:", end=" ")
        print(task)
        task.mark_pending()
        print("Updated Task:", end=" ")
        print(task)
        self.assertEqual(
            task.status,
            "pending",
            'ERROR: status should be "pending", but marked as "completed"',
        )
        print("Task successfully updated")
        print()

    def test_delete_non_existent_task(self):
        # Test deleting a non-existent task from a list
        print("Running test to delete a non-existent task from a list")
        task1 = Task(
            1,
            "Test Task 1",
            "This is a test task 1",
            date.fromisoformat("2023-06-01"),
            1,
        )
        print("Task created:", end=" ")
        print(task1)
        tasks_list = [task1]
        tasks_list = Task.delete_task(tasks_list, 2)
        self.assertIn(task1, tasks_list, "ERROR: task1 should still be in the list")
        self.assertEqual(
            len(tasks_list),
            1,
            "ERROR: tasks_list should only have 1 object, but "
            + str(len(tasks_list))
            + "was found",
        )
        print("Success! existing Task task1 was not deleted")
        print()


if __name__ == "__main__":
    unittest.main()
