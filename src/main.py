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
        # Need to account for a user entering in data in an incorrect format
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
    tasks = load_tasks()
    course_id = int(input("Enter course ID to delete: ")) # Need to account for trying to delete an invalid course
    tasks = [task for task in tasks if task["course_id"] != course_id]
    courses = [course for course in courses if course["id"] != course_id]
    save_tasks(tasks)
    save_courses(courses)
    print("Course and associated tasks deleted successfully.")


def edit_course():
    courses = load_courses()
    course_id = int(input("Enter course ID to edit: ")) # Need to account for trying to edit an invalid course
    for course in courses:
        # Could we introduce an option here if a user wants to keep specific details the same?
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
        # Need to account for a user entering in data in an incorrect format
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
    task_id = int(input("Enter task ID to delete: ")) # Need to account for trying to delete an invalid task
    tasks = [task for task in tasks if task["task_id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully.")


def edit_task():
    tasks = load_tasks()
    task_id = int(input("Enter task ID to edit: ")) # Need to account for trying to edit an invalid task
    for task in tasks:
        if task["task_id"] == task_id:
            # Again, introducing an option to keep certain details the same could be nice
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


def sort_tasks_by_due_date():
    """
    Sorts tasks by due date and prints them to CLI
    """
    tasks = load_tasks()
    sorted_tasks = sorted(tasks, key=lambda task: task["due_date"]) # Assumes format is YYYY-MM-DD

    for task in sorted_tasks:
        print(
            f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Status: {task['status']}"
        )


def sort_tasks_by_course_id():
    """
    Sorts tasks by course ID and prints them to CLI
    """
    tasks = load_tasks()
    sorted_tasks = sorted(tasks, key=lambda task: task["course_id"])

    for task in sorted_tasks:
        print(
            f"ID: {task['task_id']}, Title: {task['title']}, Due Date: {task['due_date']}, Course ID: {task['course_id']}, Status: {task['status']}"
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
        "-sd": "sort_by_due_date",
        "-sc": "sort_by_course",
    }

    if len(sys.argv) < 2:
        # User won't know any flags when first executing the program. Maybe print the list here as well?
        print("No flags provided. Use -h for help.")
        return

    flag = sys.argv[1]
    if flag in flags:
        print(f"Flag detected: {flags[flag]}")

        # Code detects flags, but doesn't do anything except for help flag
        # Switches would be good to use here

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
            -sd  Sort tasks by due date
            -sc  Sort tasks by course ID
            """
            )
    else:
        print("Unknown flag. Use -h for help.")


def main():
    parse_flags()


if __name__ == "__main__":
    main()
