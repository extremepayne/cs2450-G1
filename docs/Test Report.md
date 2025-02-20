# CLI Prototype Test Report
## Test cases:

* `Course(id, name, description, code, end\_date, start\_date)`:
  * Adding a course `(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")`
    * Add course with empty name
      * `(1, "", "This is a test course", "TC101", "2023-06-01", "2023-06-30")`
    * Add course with empty desc.
      * `(1, "Test Course", "", "TC101", "2023-06-01", "2023-06-30")`
    * Add course with empty code
      * `(1, "Test Course", "This is a test course", "", "2023-06-01", "2023-06-30")`
    * Add course with empty dates
      * `(1, "Test Course", "This is a test course", "TC101", "", "")`
    * Add course with duplicate ID
      * Course 1:(1, "Test Course 1", "This is a test course 1", "TC101", "2023-06-01", "2023-06-30")
      * Course 2:(1, "Test Course 2", "This is a test course 2", "TC102", "2023-07-01", "2023-07-30")
        * Expected to return “ValueError” because course\_id with 1 already exists
  * Adding a course to courseList (Expected to add course to courseList list at index 0\)
  * Deleting a course from courseList (The delete course is expected to be removed from courseList)
    * Delete non-existent course
      * Course 1 existes in the list, attempting to delete course with course\_id of 2 (not existent) will not delete course 1
  * Editing a course: From (1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
    * Edit course name
      * “Test Course” \-\> “New Course Name”
    * Edit course desc.
      * “This is a test course” \-\> New Course Description”
    * Edit course code
      * “TC101” \-\> “NEW101”
    * Edit course date
      * “2023-06-01", "2023-06-30” \-\> "2023-07-01", "2023-07-30"
    * Edit course with invalid field
      * Made up a new invalid field named “invalid\_field” and variable set to “invalid”. Expected to return “AttributeError” since no “invalid\_field” exist in course()

* Tasks (task\_id, title, description, due\_date course\_id, status):
  * Creating a task (1, "Test Task", "This is a test task", "2023-06-01", 1, status \= “pending”)
    * Create task with empty title
      * (1, "", "This is a test task", "2023-06-01", 1\)
    * Create task with empty desc.
      * (1, "Test Task", "", "2023-06-01", 1\)
    * Create task with empty due date
      * (1, "Test Task", "This is a test task", "", 1\)
    * Create task with invalid course ID
      * (1, "Test Task", "This is a test task", "2023-06-01", \-1)
        * Code confirms id is invalid (-1)
  * Mark Status
    * Mark as pending
      * (status \= “pending”)
    * Mark as pending on already pending task
      * (status \= “pending”) \-\> (status \= “pending”)
        * status stays “pending” with no errors
    * Mark as complete
      * (status \= “complete”)
    * Mark as complete on already completed task
      * (status \= “complete”) \-\> (status \= “complete”)
        * status stays “complete” with no errors
    * Update task (ids cannot be changed)
      * (1, "Test Task", "This is a test task", "2023-06-01", 1\) \-\> (1, "Updated Task", "This is an updated task", "2023-07-01", 1\)
    * Update task with invalid field
      * Attempt to update task() with (invalid\_field="Invalid")
        * Show throw AttributeError because “invalid\_field” does not exist
  * Delete Task
    * Deleting non existent task
      * tasks\_list held task1(1, "Test Task 1", "This is a test task 1", "2023-06-01", 1). Attempted to delete 2nd task in the list (non existent). task1 should not be deleted.

## Test environment and test results:

* Used VSCode python debugger to run all tests via run\_tests.py (unittest).
  * 29 tasks passed in 0.007s.

## Bugs:

* Swapped variables for course(): end\_date and start\_date swapped positions.
  * Issue was fixed as of writing this report
* Test for invalid course\_id for task() confirms the id is an invalid number (-1) instead of throwing errors (minor concern).
  * Should be fine as \-1 does indicate errors
