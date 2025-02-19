from typing import List, Dict


class Task:
    """A class representing a task associated with a course."""

    def __init__(
        self,
        task_id: int,
        title: str,
        description: str,
        due_date: str,
        course_id: int,
        status: str = "pending",
    ):
        """
        Initialize a new Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task
            description (str): Description of the task
            due_date (str): Due date for the task
            course_id (int): ID of the associated course
            status (str, optional): Current status of the task. Defaults to "pending"
        """
        self.task_id: int = task_id
        self.title: str = title
        self.description: str = description
        self.due_date: str = due_date
        self.course_id: int = course_id
        self.status: str = status

    @staticmethod
    def create_task(
        task_id: int, title: str, description: str, due_date: str, course_id: int
    ) -> "Task":
        """
        Create a new Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Title of the task
            description (str): Description of the task
            due_date (str): Due date for the task
            course_id (int): ID of the associated course

        Returns:
            Task: New Task instance
        """
        return Task(task_id, title, description, due_date, course_id)

    def get_task_details(self) -> Dict[str, str]:
        """
        Get task details as a dictionary.

        Returns:
            Dict[str, str]: Dictionary containing task details
        """
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "course_id": self.course_id,
            "status": self.status,
        }

    def update_task(self, **kwargs) -> "Task":
        """
        Update task attributes using keyword arguments.

        Args:
            **kwargs: Keyword arguments containing attributes to update

        Returns:
            Task: Updated Task instance
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self

    def mark_complete(self) -> "Task":
        """
        Mark the task as completed.

        Returns:
            Task: Updated Task instance
        """
        self.status = "completed"
        return self

    def mark_pending(self) -> "Task":
        """
        Mark the task as pending.

        Returns:
            Task: Updated Task instance
        """
        self.status = "pending"
        return self

    @staticmethod
    def delete_task(tasks_list: List["Task"], task_id: int) -> List["Task"]:
        """
        Delete a task from a list of tasks.

        Args:
            tasks_list (List[Task]): List of tasks
            task_id (int): ID of the task to delete

        Returns:
            List[Task]: Updated list of tasks with specified task removed
        """
        return [task for task in tasks_list if task.task_id != task_id]
