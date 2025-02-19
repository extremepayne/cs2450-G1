import json
from typing import List, Optional, Dict, Any

COURSE_FILE = "courses.json"


class Course:
    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        code: str,
        end_date: str,
        start_date: str,
    ):
        self.id: int = id
        self.name: str = name
        self.description: str = description
        self.code: str = code
        self.end_date: str = end_date
        self.start_date: str = start_date
        self.tasks: List[dict] = []
        self.completed_tasks: List[dict] = []

    def add_task(self, task: dict) -> None:
        self.tasks.append(task)


class CourseList:
    def __init__(self):
        self.courses: List[Course] = self.load_courses()

    def _create_course_from_dict(self, course_data: Dict[str, Any]) -> Course:
        # Extract core course attributes
        core_attrs = {
            "id": course_data["id"],
            "name": course_data["name"],
            "description": course_data["description"],
            "code": course_data["code"],
            "end_date": course_data["end_date"],
            "start_date": course_data["start_date"],
        }

        # Create course instance
        course = Course(**core_attrs)

        # Add tasks if they exist in the data
        if "tasks" in course_data:
            course.tasks = course_data["tasks"]
        if "completed_tasks" in course_data:
            course.completed_tasks = course_data["completed_tasks"]

        return course

    def load_courses(self) -> List[Course]:
        try:
            with open(COURSE_FILE, "r") as file:
                courses_data = json.load(file)
                return [
                    self._create_course_from_dict(course) for course in courses_data
                ]
        except FileNotFoundError:
            return []

    def save_courses(self) -> None:
        with open(COURSE_FILE, "w") as file:
            json.dump([course.__dict__ for course in self.courses], file, indent=4)

    def add_course(self, course: Course) -> None:
        self.courses.append(course)
        self.save_courses()

    def delete_course(self, id: int) -> None:
        self.courses = [course for course in self.courses if course.id != id]
        self.save_courses()
