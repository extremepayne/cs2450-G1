import sys
import json

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


def load_courses():
    try:
        with open(COURSE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_courses(courses):
    with open(COURSE_FILE, "w") as file:
        json.dump(courses, file, indent=4)


def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def create_course():
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


def list_course():
    courses = load_courses()
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}, Code: {course['code']}")


def delete_course():
    courses = load_courses()
    course_id = int(input("Enter course ID to delete: "))
    courses = [course for course in courses if course["id"] != course_id]
    save_courses(courses)
    print("Course deleted successfully.")


def edit_course():
    courses = load_courses()
    course_id = int(input("Enter course ID to edit: "))
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


def create_task():
    tasks = load_tasks()
    new_task = {
        "task_id": len(tasks) + 1,
        "title": input("Enter task title: "),
        "description": input("Enter task description: "),
        "due_date": input("Enter due date: "),
        "course_id": int(input("Enter course ID: ")),
        "status": "pending",
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task created successfully.")


def list_task():
    tasks = load_tasks()
    for task in tasks:
        print(
            f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
        )


def delete_task():
    tasks = load_tasks()
    task_id = int(input("Enter task ID to delete: "))
    tasks = [task for task in tasks if task["task_id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully.")


def edit_task():
    tasks = load_tasks()
    task_id = int(input("Enter task ID to edit: "))
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


def filter_tasks_by_due_date(due_date):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task["due_date"] == due_date]
    for task in filtered_tasks:
        print(
            f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
        )


def filter_tasks_by_course(course_id):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if task["course_id"] == course_id]
    for task in filtered_tasks:
        print(
            f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
        )


def parse_flags():
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
        if flag == "-h":
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
    else:
        print("Unknown flag. Use -h for help.")


def main():
    parse_flags()


if __name__ == "__main__":
    main()
