# Task Manager
This is a task manager for students.

# Installation
Download the corresponding .zip file for your system, extract it, and open up the TaskManager app found inside of it.

# Requirements
For MacOS, this application is built specifically for Apple Silicon processors and is not compatible with Intel-based Macs.

`tkcalendar` is required to run this application. If it is not installed on your computer, install it using an CLI application. (Windows users for example can open PowerShell and type `pip install tkcalendar`)

# Features

- Task Management
    - Create, edit, and delete tasks
    - Set task deadlines with date picker
    - Add task descriptions
    - Mark tasks as complete/incomplete

- Course Management
    - Create, edit, and delete courses
    - Associate tasks with specific courses
    - Course filtering and organization

- User Interface
    - Modern graphical user interface using tkinter
    - Calendar integration with tkcalendar
    - Intuitive task and course management controls
    - Clean and responsive design

- Organization Features
    - Filter tasks by course
    - Sort tasks by due date
    - Sort tasks by course
    - View upcoming deadlines
    - Task status tracking

- Data Management
    - Automatic saving of tasks and courses
    - JSON-based data storage
    - Local file persistence
    - JSON export and import

# Instructions
In the default home page of the application, courses and tasks are shown in nested lists where the task associated with the course will be put into the course's list. Default sorting is by due date.

- Tasks:
    - Add: Click the "add task" button to add a task, enter a title, due date and description. The course it is associated with can be selected with a drop down menu. Select the date with the calendar. Click "Save Task" to confirm changes.
    - Edit: Click the "pencil with a note" button to edit a course, the interface is similar to the one in adding tasks. Click "Save Task" to confirm changes.
    - View details: (Double) Click the task and a window containing its details (Title, due date, description) will pop out. Click "X" to close.
    - Delete: Click the red trash can button in the task. A red window pop up asking for confirmation. Click "Yes" to delete, "No" to cancel.
- Courses:
    - Add: Click the "add course" button to add a course, enter a title, code and description. Use the calendar to choose start/end dates. Click "Save Course" to confirm changes.
    - Edit: Click the "pencil with a note" button to edit a course, the interface is similar to the one in adding courses. Click "Save Course" to confirm changes.
    - Delete: Click the red trash can button in the course. A red window should pop up asking for confirmation. Click "Yes" to delete, "No" to cancel.
- Filter and Sort:
    - Filter: Click the 3-lines menu button on the top left-corner. There you can filter task but its course and due date. Click apply to apply sorting.
    - Sort: On the top-right corner is a drop down menu, which contains sorting options for the tasks.
# Artifacts
**ZenHub board:** [https://app.zenhub.com/workspaces/2450-group-1-67a67af4a0f29f0029d41e97/board](https://app.zenhub.com/workspaces/2450-group-1-67a67af4a0f29f0029d41e97/board)

**Presentation:** [[.pptx](https://github.com/extremepayne/cs2450-G1/blob/main/docs/Group%201%20Presentation.pptx)]
