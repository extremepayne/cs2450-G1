from typing import List, Dict

class Task:
    def __init__(
        self, task_id: int, title: str, description: str, due_date: str, course_id: int, status: str = "pending"
    ):
        self.task_id: int = task_id
        self.title: str = title
        self.description: str = description
        self.due_date: str = due_date
        self.course_id: int = course_id
        self.status: str = status

    def create_task(task_id: int, title: str, description: str, due_date: str, course_id: int) -> 'Task':
        return Task(task_id, title, description, due_date, course_id)

    def get_task_details(self) -> Dict[str, str]:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "course_id": self.course_id,
            "status": self.status,
        }

    def update_task(self, **kwargs) -> 'Task':
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self

    def mark_complete(self) -> 'Task':
        self.status = "completed"
        return self

    def mark_pending(self) -> 'Task':
        self.status = "pending"
        return self

    def delete_task(tasks_list: List['Task'], task_id: int) -> List['Task']:
        return [task for task in tasks_list if task.task_id != task_id]
