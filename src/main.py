import sys
import json
from typing import List, Dict, Any
from datetime import date

# No "menu" setup, we will run this CLI app by the flags we set
# -h, help
# -cc -create course
# -lc -list course
# -dc -delete course
# -ec -edit course
# -ct -create task
# -lt -list task
# -dt -delete task
# -et -edit task

COURSE_FILE = "courses.json"
TASK_FILE = "tasks.json"


class DataManager:
    """Handles loading and saving data for courses and tasks."""

    @staticmethod
    def load_courses() -> List[Dict[str, Any]]:
        """
        Loads courses from the JSON file.

        Args:
            courses (List[Dict[str, Any]]): list of courses
        """
        try:
            with open(COURSE_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_courses(courses: List[Dict[str, Any]]) -> None:
        """
        Saves courses to the JSON file.

        Args:
            courses (List[Dict[str, Any]]): list of courses
        """
        with open(COURSE_FILE, "w") as file:
            json.dump(courses, file, indent=4)

    @staticmethod
    def load_tasks() -> List[Dict[str, Any]]:
        """
        Loads tasks from the JSON file.

        Args:
            tasks (List[Dict[str, Any]]): list of tasks
        """
        try:
            with open(TASK_FILE, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_tasks(tasks: List[Dict[str, Any]]) -> None:
        """
        Saves tasks to the JSON file.

        Args:
            tasks (List[Dict[str, Any]]): list of tasks
        """
        with open(TASK_FILE, "w") as file:
            json.dump(tasks, file, indent=4)


class CourseManager:
    """Manages course-related operations."""

    def __init__(self, data_manager: DataManager):
        """
        Initializes a CourseManager object.

        Args:
            data_manager (DataManager): manages loading and saving data
        """

        self.data_manager = data_manager
        self.courses = data_manager.load_courses()

    def create_course(self) -> None:
        """Creates a new course."""
        new_course = {
            "id": len(self.courses) + 1,
            "name": input("Enter course name: "),
            "description": input("Enter course description: "),
            "code": input("Enter course code: "),
            "start_date": input("Enter start date (YYYY-MM-DD): "),
            "end_date": input("Enter end date (YYYY-MM-DD): "),
        }
        self.courses.append(new_course)
        self.data_manager.save_courses(self.courses)
        print(f"Course created successfully. The ID is {new_course['id']}")

    def list_courses(self) -> None:
        """Lists all courses."""
        for course in self.courses:
            print(f"ID: {course['id']}, Name: {course['name']}, Code: {course['code']}")

    def delete_course(self) -> int:
        """
        Deletes a course

        Returns:
            ID of the deleted course.
        """
        course_id = int(input("Enter course ID to delete: "))
        deleted_course_id = None
        self.courses = [
            course
            for course in self.courses
            if not (course["id"] == course_id and (deleted_course_id := course_id))
        ]
        self.data_manager.save_courses(self.courses)
        if deleted_course_id is not None:
            print("Course deleted successfully.")
            return deleted_course_id
        else:
            print("Course not found.")
            return None

    def edit_course(self) -> None:
        """Edits an existing course."""
        while True:
            try:
                course_id = int(input("Enter course ID to edit: "))
                if course_id not in [course["id"] for course in self.courses]:
                    print("Invalid course ID. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid course ID.")
                continue
            break

        for course in self.courses:
            if course["id"] == course_id:
                course["name"] = input("Enter new course name: ")
                course["description"] = input("Enter new course description: ")
                course["code"] = input("Enter new course code: ")
                course["start_date"] = input("Enter new start date (YYYY-MM-DD): ")
                course["end_date"] = input("Enter new end date (YYYY-MM-DD): ")
                break
        self.data_manager.save_courses(self.courses)
        print("Course edited successfully.")

    def get_course_ids(self) -> List[int]:
        """
        Gets a list of all course IDs.

        Returns:
            List of course IDs.
        """
        return [course["id"] for course in self.courses]


class TaskManager:
    """Manages task-related operations."""

    def __init__(self, data_manager: DataManager):
        """
        Initializes a TaskManager object.

        Args:
            data_manager (DataManager): manages loading and saving data
        """

        self.data_manager = data_manager
        self.tasks = data_manager.load_tasks()

    def create_task(self, course_manager: CourseManager) -> None:
        """
        Creates a new task.

        Args:
            course_manager (CourseManager): manager for courses
        """
        course_ids = course_manager.get_course_ids()

        while True:
            try:
                course_id = int(input("Enter course ID: "))
                if course_id not in course_ids:
                    print("Invalid course ID. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid course ID.")
                continue
            break

        new_task = {
            "task_id": len(self.tasks) + 1,
            "title": input("Enter task title: "),
            "description": input("Enter task description: "),
            "due_date": input("Enter due date (YYYY-MM-DD): "),
            "course_id": course_id,
            "status": "pending",
        }
        self.tasks.append(new_task)
        self.data_manager.save_tasks(self.tasks)
        print("Task created successfully.")

    def list_tasks(self) -> None:
        """Lists all tasks."""
        for task in self.tasks:
            print(
                f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
            )

    def delete_task(self) -> None:
        """Deletes a task."""
        while True:
            try:
                task_id = int(input("Enter task ID to delete: "))
                if task_id not in [task["task_id"] for task in self.tasks]:
                    print("Invalid task ID. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
                continue
            break
        self.tasks = [task for task in self.tasks if task["task_id"] != task_id]
        self.data_manager.save_tasks(self.tasks)
        print("Task deleted successfully.")

    def edit_task(self, course_manager: CourseManager) -> None:
        """
        Edits an existing task.

        Args:
            course_manager (CourseManager): manager for courses
        """

        while True:
            try:
                task_id = int(input("Enter task ID to edit: "))
                if task_id not in [task["task_id"] for task in self.tasks]:
                    print("Invalid task ID. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
                continue
            break

        for task in self.tasks:
            if task["task_id"] == task_id:
                task["title"] = input("Enter new task title: ")
                task["description"] = input("Enter new task description: ")
                task["due_date"] = input("Enter new due date (YYYY-MM-DD): ")
                while True:
                    try:
                        course_id = int(input("Enter new course ID: "))
                        if course_id not in course_manager.get_course_ids():
                            print("Invalid course ID. Please try again.")
                            continue
                    except ValueError:
                        print("Invalid input. Please enter a valid course ID.")
                        continue
                    break
                task["course_id"] = course_id
                task["status"] = input("Enter new status: ")
                break
        self.data_manager.save_tasks(self.tasks)
        print("Task edited successfully.")

    def filter_tasks_by_due_date(self, due_date: str) -> None:
        """
        Filters tasks by due date.

        Args:
            due_date (str): due date to filter by.
        """

        filtered_tasks = [task for task in self.tasks if task["due_date"] == due_date]
        for task in filtered_tasks:
            print(
                f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
            )

    def filter_tasks_by_course(self, course_id: int) -> None:
        """
        Filters tasks by course ID.

        Args:
            course_id (int): course ID
        """

        filtered_tasks = [task for task in self.tasks if task["course_id"] == course_id]
        for task in filtered_tasks:
            print(
                f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
            )

    def sort_tasks_by_due_date(self) -> None:
        """Sorts tasks by due date."""
        sorted_tasks = sorted(self.tasks, key=lambda task: task["due_date"])
        self.data_manager.save_tasks(sorted_tasks)
        for task in sorted_tasks:
            print(
                f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
            )

    def sort_tasks_by_course_id(self) -> None:
        """Sorts tasks by course ID."""
        sorted_tasks = sorted(self.tasks, key=lambda task: task["course_id"])
        self.data_manager.save_tasks(sorted_tasks)
        for task in sorted_tasks:
            print(
                f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Course ID: {task['course_id']}, Status: {task['status']}"
            )

    def delete_tasks_by_course(self, course_id: int) -> None:
        """
        Deletes all tasks associated with a given course ID.

        Args:
            course_id (int): course ID
        """

        self.tasks = [task for task in self.tasks if task["course_id"] != course_id]
        self.data_manager.save_tasks(self.tasks)


class CLI:
    """Handles command-line interface interactions."""

    def __init__(self, course_manager: CourseManager, task_manager: TaskManager):
        self.course_manager = course_manager
        self.task_manager = task_manager
        self.commands = {
            "-h": self.help,
            "-cc": self.course_manager.create_course,
            "-lc": self.course_manager.list_courses,
            "-dc": self.delete_course_and_tasks,
            "-ec": self.course_manager.edit_course,
            "-ct": lambda: self.task_manager.create_task(self.course_manager),
            "-lt": self.task_manager.list_tasks,
            "-dt": self.task_manager.delete_task,
            "-et": lambda: self.task_manager.edit_task(self.course_manager),
            "-fd": self.filter_tasks_by_due_date,
            "-fc": self.filter_tasks_by_course,
            "-sd": self.task_manager.sort_tasks_by_due_date,
            "-sc": self.task_manager.sort_tasks_by_course_id,
        }

    def help(self) -> None:
        """Displays the help message."""
        print(
            """
            Usage: main.py [flag]
            Flags:
            -h   Show this help message
            -cc  Create a new course
            -lc  List all courses
            -dc  Delete a course
            -ec  Edit a course
            -ct  Create a new task
            -lt  List all tasks
            -dt  Delete a task
            -et  Edit a task
            -fd  Filter tasks by due date
            -fc  Filter tasks by course ID
            -sd  Sort tasks by due date
            -sc  Sort tasks by course ID
            """
        )

    def filter_tasks_by_due_date(self) -> None:
        """Filters tasks by due date."""
        due_date = input("Enter due date to filter tasks (YYYY-MM-DD): ")
        self.task_manager.filter_tasks_by_due_date(due_date)

    def filter_tasks_by_course(self) -> None:
        """Filters tasks by course ID."""
        course_ids = self.course_manager.get_course_ids()
        while True:
            try:
                course_id = int(input("Enter course ID to filter tasks: "))
                if course_id not in course_ids:
                    print("Invalid course ID. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid course ID.")
                continue
            break
        self.task_manager.filter_tasks_by_course(course_id)

    def delete_course_and_tasks(self) -> None:
        """Deletes a course and its associated tasks."""
        deleted_course_id = self.course_manager.delete_course()
        if deleted_course_id is not None:
            self.task_manager.delete_tasks_by_course(deleted_course_id)
            print("Course and associated tasks deleted successfully.")

    def run(self) -> None:
        """Parses command-line arguments and executes the corresponding command."""
        if len(sys.argv) < 2:
            print("No flags provided. Use -h for help.")
            return

        flag = sys.argv[1]
        if flag in self.commands:
            print(f"Flag detected: {flag}")
            self.commands[flag]()
        else:
            print("Unknown flag. Use -h for help.")


def main() -> None:
    """Main function to initialize and run the application."""
    data_manager = DataManager()
    course_manager = CourseManager(data_manager)
    task_manager = TaskManager(data_manager)
    cli = CLI(course_manager, task_manager)
    cli.run()


if __name__ == "__main__":
    main()
