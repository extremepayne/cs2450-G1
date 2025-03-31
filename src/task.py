import json
from typing import List, Dict, Any
from datetime import date

TASK_FILE = "tasks.json"


class Task:
    """A class representing a task associated with a course."""

    def __init__(
        self,
        task_id: int,
        title: str,
        description: str,
        due_date: date,
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
        if not isinstance(due_date, date):
            raise TypeError("Due Date must be a date object")
        self.due_date: date = due_date
        self.course_id: int = course_id
        self.status: str = status

    def __str__(self):
        """Returns human-readable string for print() functions"""
        return (
            f"{{task_id: {self.task_id}, title: {self.title}, "
            f"description: {self.description}, due_date: {self.due_date.strftime('%Y/%m/%d')}, "
            f"course_id: {self.course_id}, status: {self.status}}}"
        )

    @staticmethod
    def create_task(
        task_id: int, title: str, description: str, due_date: date, course_id: int
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

    @classmethod
    def load_tasks(cls) -> List["Task"]:
        """Load tasks from JSON file"""
        try:
            with open(TASK_FILE, "r") as file:
                tasks_data = json.load(file)
                return [cls.from_dict(task) for task in tasks_data]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_tasks(tasks: List["Task"]) -> None:
        """Save tasks to JSON file"""
        tasks_data = [task.to_dict() for task in tasks]
        with open(TASK_FILE, "w") as file:
            json.dump(tasks_data, file, indent=4)

    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary format"""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date.isoformat(),
            "course_id": self.course_id,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """Create Task instance from dictionary"""
        core_attrs = cls(
            task_id=data["task_id"],
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            course_id=data["course_id"],
            status=data["status"],
        )
        core_attrs["due_date"] = date.fromisoformat(core_attrs["due_date"])
        return core_attrs
