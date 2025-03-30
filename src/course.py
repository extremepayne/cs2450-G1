import json
from typing import List, Optional, Dict, Any
from datetime import date

COURSE_FILE = "courses.json"


class Course:
    """A class representing a course with basic information and associated tasks."""

    __slots__ = [
        "id",
        "name",
        "description",
        "code",
        "start_date",
        "end_date",
        "tasks",
        "completed_tasks",
    ]

    def __init__(
        self,
        id: int,
        name: str,
        description: str,
        code: str,
        start_date: date,
        end_date: date,
    ):
        """
        Initialize a new Course instance.

        Args:
            id (int): Unique identifier for the course
            name (str): Name of the course
            description (str): Description of the course
            code (str): Course code
            start_date (str): Start date of the course
            end_date (str): End date of the course
        """
        self.id: int = id
        self.name: str = name
        self.description: str = description
        self.code: str = code
        if not isinstance(start_date, date):
            raise TypeError("Start Date must be a date object")
        self.start_date: date = start_date
        if not isinstance(end_date, date):
            raise TypeError("Start Date must be a date object")
        self.end_date: date = end_date
        self.tasks: List[dict] = []
        self.completed_tasks: List[dict] = []

    def __str__(self):
        """Returns a human-readable string representation of the course."""
        return f"{{id: {self.id}, name: {self.name}, code: {self.code}, start_date: {self.start_date}, end_date: {self.end_date}}}"

    def to_dict(self) -> Dict[str, Any]:
        """Convert Course instance to dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "code": self.code,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "tasks": self.tasks,
            "completed_tasks": self.completed_tasks,
        }

    def add_task(self, task: dict) -> None:
        """
        Add a task to the course's task list.

        Args:
            task (dict): Task dictionary containing task details
        """
        self.tasks.append(task)


class CourseList:
    """A class for managing a collection of courses with persistence."""

    def __init__(self):
        """Initialize CourseList and load existing courses from storage."""
        self.courses: List[Course] = self.load_courses()

    def __str__(self) -> str:
        """Returns a human-readable string representation of the CourseList."""
        return "[" + ", ".join(str(course) for course in self.courses) + "]"

    def _create_course_from_dict(self, course_data: Dict[str, Any]) -> Course:
        """
        Create a Course instance from a dictionary.

        Args:
            course_data (Dict[str, Any]): Dictionary containing course data

        Returns:
            Course: New Course instance created from the data
        """
        # Extract core course attributes and convert date strings to date objects
        core_attrs = {
            "id": course_data["id"],
            "name": course_data["name"],
            "description": course_data["description"],
            "code": course_data["code"],
            "start_date": date.fromisoformat(course_data["start_date"]),
            "end_date": date.fromisoformat(course_data["end_date"]),
        }

        # Create course instance
        course = Course(**core_attrs)

        # Add tasks and completed tasks if they exist in the data
        course.tasks = course_data.get("tasks", [])
        course.completed_tasks = course_data.get("completed_tasks", [])

        return course

    def load_courses(self) -> List[Course]:
        """
        Load courses from the JSON file.

        Returns:
            List[Course]: List of Course instances loaded from storage
        """
        try:
            with open(COURSE_FILE, "r") as file:
                courses_data = json.load(file)
                return [
                    self._create_course_from_dict(course) for course in courses_data
                ]
        except FileNotFoundError:
            return []

    def save_courses(self) -> None:
        """Save current courses to the JSON file."""
        with open(COURSE_FILE, "w") as file:
            json.dump([course.to_dict() for course in self.courses], file, indent=4)

    def add_course(self, course: Course) -> None:
        """
        Add a new course to the list and save to storage.

        Args:
            course (Course): Course instance to add

        Raises:
            ValueError: If a course with the same ID already exists
        """
        # Check for duplicate ID
        if any(existing_course.id == course.id for existing_course in self.courses):
            raise ValueError(f"Course with ID {course.id} already exists")
        self.courses.append(course)
        self.save_courses()

    def delete_course(self, id: int) -> None:
        """
        Delete a course by its ID and save changes.

        Args:
            id (int): ID of the course to delete
        """
        self.courses = [course for course in self.courses if course.id != id]
        self.save_courses()
