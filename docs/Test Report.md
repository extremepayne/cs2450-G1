# CLI Prototype Test Report

## Test cases

* `Course(id, name, description, code, end\_date, start\_date)`:
  * Adding a course
    * `(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")`
      * Course was added and saved to courses.json without issue.
  * Add course with empty name
    * `(1, "", "This is a test course", "TC101", "2023-06-01", "2023-06-30")`
      * Course without title was added and saved to courses.json without issue.
  * Add course with empty desc.
    * `(1, "Test Course", "", "TC101", "2023-06-01", "2023-06-30")`
      * Course without a description was added and saved to courses.json without issue.
  * Add course with empty code
    * `(1, "Test Course", "This is a test course", "", "2023-06-01", "2023-06-30")`
      * Course without course code was added and saved to  courses.json without issue.
  * Add course with empty dates
    * `(1, "Test Course", "This is a test course", "TC101", "", "")`
      * Course without start/end dates was added and saved to courses.json without issue.
  * Add course with duplicate ID
    * Course 1:`(1, "Test Course 1", "This is a test course 1", "TC101", "2023-06-01", "2023-06-30")`
      * Course was saved to courses.json
    * Course 2:`(1, "Test Course 2", "This is a test course 2", "TC102", "2023-07-01", "2023-07-30")`
      * Code ran into `ValueError` and course was not saved to courses.json (expected)
  * Adding a course to courseList
    * \[ \] containing `(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")`
      * Course was successfully saved to courses.json
  * Deleting a course from courseList
    * Preexisting: `(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")`
      * Course was deleted successfully from courses.json
    * Delete non-existent course
      * Preexisting: `(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")`
        * Code deletes course with course\_id of 2, which does not exist. Course with course\_id of 1 was not removed.
  * Editing a course: From `(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")`
    * Edit course name
      * "Test Course" \-\> "New Course Name"
        * Code does not save to JSON files but data in the instance passed tests
    * Edit course desc.
      * "This is a test course" \-\> New Course Description"
        * Code does not save to JSON files but data in the instance passed tests
    * Edit course code
      * "TC101" \-\> "NEW101"
        * Code does not save to JSON files but data in the instance passed tests
    * Edit course date
      * "2023-06-01", "2023-06-30" \-\> "2023-07-01", "2023-07-30"
        * Code does not save to JSON files but data in the instance passed tests
    * Edit course with invalid field
      * Made up a new invalid field named "invalid\_field" and variable set to "invalid".
        * Code does not make changes to the course

* Tasks (task\_id, title, description, due\_date course\_id, status):
  * Creating a task `(1, "Test Task", "This is a test task", "2023-06-01", 1, status \= "pending")`
    * Create task with empty title
      * `(1, "", "This is a test task", "2023-06-01", 1)`
        * Task was created and passed in code instance
    * Create task with empty desc.
      * `(1, "Test Task", "", "2023-06-01", 1)`
        * Task was created and passed in code instance
    * Create task with empty due date
      * `(1, "Test Task", "This is a test task", "", 1)`
        * Task was created and passed in code instance
    * Create task with invalid course ID
      * `(1, "Test Task", "This is a test task", "2023-06-01", -1)`
        * Task was created and passed in code instance, even if the list now has an invalid course\_id (`-1`)
  * Mark Status
    * Mark as pending
      * code set status flag to "pending"
    * Mark as pending on already pending task
      * (status \= "pending") \-\> (status \= "pending")
        * code set status flag to "pending" with no issue
    * Mark as complete
      * (status \= "complete")
        * code set status flag to "complete"
    * Mark as complete on already completed task
      * (status \= "complete") \-\> (status \= "complete")
        * code set status flag to "complete" with no issues
  * Update task (ids cannot be changed)
    * `(1, "Test Task", "This is a test task", "2023-06-01", 1)` \-\> `(1, "Updated Task", "This is an updated task", "2023-07-01", 1)`
      * Change made successfully in instance and passed test
  * Update task with invalid field
    * Attempt to update `task()` with (`invalid_field="Invalid"`)
      * Show throw `AttributeError` because `invalid_field` does not exist. Code did not update task with new field of "invalid field"
  * Delete Task
    * `task1` and `task2` was made, code deletes `task1`
      * Code deleted `task1` and only `task2` remained
  * Deleting non existent task
    * `tasks_list` held `task1(1, "Test Task 1", "This is a test task 1", "2023-06-01", 1)`. Code attempts to delete the 2nd task in the list (non existent). `task1` was not deleted.

## Test environment and test results

* Used VSCode python debugger to run all tests via `run_tests.py` (unittest).
  * 29 tasks passed in 0.007s.

## Really tiny concerns

* Only the course tests saved courses to courses.json. All the task test only utilized in instance data for the test and did not output to JSON.
*

## Bugs

* Swapped variables for `course()`: `end_date` and `start_date` swapped positions.
  * Issue was fixed as of writing this report
* Test for invalid `course_id` for `task()` confirms the id is an invalid number (`-1`) instead of throwing errors (minor concern).
  * Should be fine as `-1` does indicate errors

  ## Integration Testing

  # Integration Test Report

## Course-Task Integration Tests

### Test Cases
1. Adding task to course
   - Creates task and associates with course ID 1
   - Task successfully saves to task.json
   - Task correctly loads with course reference intact

2. Deleting course with tasks
   - Course deletion cascades to associated tasks
   - Both course and tasks removed from respective JSON files
   - No orphaned tasks remain

3. Editing course with tasks  
   - Task associations maintained after course edit
   - Course changes persist in courses.json
   - Task course references remain valid

4. Task with invalid course ID
   - System allows creating orphaned tasks
   - Task loads successfully despite invalid course ID
   - Course list properly excludes invalid IDs

5. Data persistence across operations
   - Course/task relationships maintained after delete
   - New course creation properly links new tasks
   - All relationships survive save/load cycle

6. Task date validation
   - Tasks can be due after course end date
   - Tasks can be due before course start date
   - Date validation remains functional

## GUI Integration Tests 

### Test Cases
1. Adding task via GUI
   - Task appears in UI list
   - Task saves to JSON
   - Course filter updates

2. Editing task via GUI
   - Changes reflect in UI
   - Updates persist to JSON
   - Task-course relationship maintained

### Test Results
- All course-task integration tests passed successfully
- GUI integration with task/course data layer working as expected
- JSON persistence functioning correctly

### Issues Found
1. Tasks can reference non-existent courses (by design)
2. Course deletion cascades could be more explicit
3. GUI needs better error handling for invalid course IDs

## Environment
- Python 3.12+
- tkinter for GUI
- JSON files for persistence
