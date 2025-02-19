import sys
import json
from typing import List, Dict, Any

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


def load_courses() -> List[Dict[str, Any]]:
    try:
        with open(COURSE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_courses(courses: List[Dict[str, Any]]) -> None:
    with open(COURSE_FILE, "w") as file:
        json.dump(courses, file, indent=4)


def load_tasks() -> List[Dict[str, Any]]:
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def create_course() -> None:
    courses = load_courses()
    new_course = {
        "id": len(courses) + 1,
        "name": input("Enter course name: "),
        "description": input("Enter course description: "),
        "code": input("Enter course code: "),
        "start_date": input("Enter start date: "),
        "end_date": input("Enter end date: "),
    }
    courses.append(new_course)
    save_courses(courses)
    print("Course created successfully.")


def list_course() -> None:
    courses = load_courses()
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}, Code: {course['code']}")


def delete_course() -> None:
    courses = load_courses()
    course_id = int(input("Enter course ID to delete: "))
    courses = [course for course in courses if course["id"] != course_id]
    save_courses(courses)
    print("Course deleted successfully.")


def edit_course() -> None:
    courses = load_courses()
    while True:
        try:
            course_id = int(input("Enter course ID to edit: "))
            if course_id not in [course["id"] for course in courses]:
                print("Invalid course ID. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid course ID.")
            continue
        break
    for course in courses:
        if course["id"] == course_id:
            course["name"] = input("Enter new course name: ")
            course["description"] = input("Enter new course description: ")
            course["code"] = input("Enter new course code: ")
            course["start_date"] = input("Enter new start date: ")
            course["end_date"] = input("Enter new end date: ")
            break
    save_courses(courses)
    print("Course edited successfully.")


def create_task() -> None:
    tasks = load_tasks()
    courses = load_courses()
    course_ids = [course["id"] for course in courses]

    # while loop to validate course_id input
    while True:
        try:
            course_id = int(input("Enter course ID: "))
            if course_id not in course_ids or type(course_id) != int:
                print("Invalid course ID. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid course ID.")
            continue
        break

    new_task = {
        "task_id": len(tasks) + 1,
        "title": input("Enter task title: "),
        "description": input("Enter task description: "),
        "due_date": input("Enter due date: "),
        "course_id": course_id,
        "status": "pending",
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task created successfully.")


def list_task() -> None:
    tasks = load_tasks()
    for task in tasks:
        print(
            f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
        )


def delete_task() -> None:
    tasks = load_tasks()

    # while loop to validate task_id input
    while True:
        try:
            task_id = int(input("Enter task ID to delete: "))
            if task_id not in [task["task_id"] for task in tasks]:
                print("Invalid task ID. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")
            continue
        break
    tasks = [task for task in tasks if task["task_id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully.")


def edit_task() -> None:
    tasks = load_tasks()
    # while loop to validate task_id input
    while True:
        try:
            task_id = int(input("Enter task ID to edit: "))
            if task_id not in [task["task_id"] for task in tasks]:
                print("Invalid task ID. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")
            continue
        break
    for task in tasks:
        if task["task_id"] == task_id:
            task["title"] = input("Enter new task title: ")
            task["description"] = input("Enter new task description: ")
            task["due_date"] = input("Enter new due date: ")
            task["course_id"] = int(input("Enter new course ID: "))
            task["status"] = input("Enter new status: ")
            break
    save_tasks(tasks)
    print("Task edited successfully.")


def filter_tasks_by_due_date(due_date: str) -> None:
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task["due_date"] == due_date]
    for task in filtered_tasks:
        print(
            f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
        )


def filter_tasks_by_course(course_id: int) -> None:
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task["course_id"] == course_id]
    for task in filtered_tasks:
        print(
            f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
        )


def parse_flags() -> None:
    flags = {
        "-h": "help",
        "-cc": "create_course",
        "-lc": "list_course",
        "-dc": "delete_course",
        "-ec": "edit_course",
        "-ct": "create_task",
        "-lt": "list_task",
        "-dt": "delete_task",
        "-et": "edit_task",
        "-fd": "filter_due_date",
        "-fc": "filter_course",
    }

    if len(sys.argv) < 2:
        print("No flags provided. Use -h for help.")
        return

    flag = sys.argv[1]
    if flag in flags:
        print(f"Flag detected: {flags[flag]}")
        match flag:
            case "-h":
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
                """
                )
            case "-cc":
                create_course()
            case "-lc":
                list_course()
            case "-dc":
                delete_course()
            case "-ec":
                edit_course()
            case "-ct":
                create_task()
            case "-lt":
                list_task()
            case "-dt":
                delete_task()
            case "-et":
                edit_task()
            case "-fd":
                due_date = input("Enter due date to filter tasks: ")
                filter_tasks_by_due_date(due_date)
            case "-fc":
                while True:
                    try:
                        course_id = int(input("Enter course ID to filter tasks: "))
                        if course_id not in [course["id"] for course in load_courses()]:
                            print("Invalid course ID. Please try again.")
                            continue
                    except ValueError:
                        print("Invalid input. Please enter a valid course ID.")
                        continue
                    break
                filter_tasks_by_course(course_id)
    else:
        print("Unknown flag. Use -h for help.")


def main() -> None:
    parse_flags()


if __name__ == "__main__":
    main()
