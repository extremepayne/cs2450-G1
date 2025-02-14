class Task:
    def __init__(
        self, task_id, title, description, due_date, course_id, status="pending"
    ):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.course_id = course_id
        self.status = status

    @staticmethod
    def create_task(task_id, title, description, due_date, course_id):
        return Task(task_id, title, description, due_date, course_id)

    def get_task_details(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "course_id": self.course_id,
            "status": self.status,
        }

    # Update
    def update_task(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self

    def mark_complete(self):
        self.status = "completed"
        return self

    def mark_pending(self):
        self.status = "pending"
        return self

    @staticmethod
    def delete_task(tasks_list, task_id):
        return [task for task in tasks_list if task.task_id != task_id]
