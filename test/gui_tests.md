Test Adding a Course:
1. Click "+ Add Course" button
2. Verify new window opens with fields:
   - Course Name
   - Course Code
   - Description
   - Start Date
   - End Date
3. Enter test data:
   - Name: "Software Engineering"
   - Code: "CS 2450"
   - Description: "Test course description"
   - Start Date: "2024-03-01"
   - End Date: "2024-06-30"
4. Click Save
5. Verify success message appears
6. Verify course appears in filter dropdown

Test Adding a Task:
1. Click "+ Add Task" button
2. Verify new window opens with fields:
   - Task Name
   - Description
   - Due Date
   - Course (dropdown)
   - Status
3. Enter test data:
   - Name: "Complete Project"
   - Description: "Test task description"
   - Due Date: "2024-04-01"
   - Course: "CS 2450"
   - Status: "Not Started"
4. Click Save
5. Verify success message appears
6. Verify task appears in main window

Test Editing a Task:
1. Click edit icon on existing task
2. Verify edit window opens with pre-filled data
3. Modify fields:
   - Change name to "Updated Project"
   - Change status to "In Progress"
4. Click Save
5. Verify changes appear in task list

Test Deleting a Task:
1. Click delete icon on existing task
2. Verify confirmation dialog appears
3. Click Yes
4. Verify task disappears from list

Test Task Visual Elements:
1. Verify each task card shows:
   - Task name (bold)
   - Description
   - Course code
   - Due date
   - Edit button
   - Delete button
2. Verify proper spacing between tasks
3. Confirm white background for task cards
4. Check edit/delete icons are visible

Test Navigation Bar:
1. Verify height is 75px
2. Confirm light blue background
3. Check button hover effects
4. Verify button text is readable

Test Input Validation:
1. Try adding course with empty required fields
2. Try adding task with invalid date format
3. Try editing task with empty name
4. Verify appropriate error messages

Test Edge Cases:
1. Add many tasks (>20) and verify scrolling works
2. Try deleting course with associated tasks
3. Test filter with no tasks in selected course

Test Save/Load:
1. Add several courses and tasks
2. Close application
3. Reopen application
4. Verify all data is restored:
   - Courses in filter dropdown
   - Tasks in main view
   - All task details preserved