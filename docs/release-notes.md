# TodoListApp

## Version 0.2 Release Notes

### Dependencies

Requires Python 3.12+.

### Using the application

From the `src/` directory, run `python main.py -h` to read the help message.

Use the various flags (e.g. `python main.py -cc`) to initiate the various actions.

For your convenience, here is a list of all acceptable flags:

```
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
```

The program will prompt you for the various bits of input that are needed. Then, it will save all applicable information and exit. To perform another action, simply run the program again.

Tasks and courses are saved locally in `.json` files.

### Running the automated tests

Run `python run_tests.py` while in the respository root.

### Changes from previous version

Basically all actual fuctionality was implemented in this version. v0.1 was more of a skeleton with no real functionality.

Here are some of the things that work now:

- Adding courses
- Adding tasks
- Deleting courses
- Deleting tasks
- Editing courses
- Editing tasks
- Filtering and sorting tasks and courses
