import unittest
import os
from src.course import Course, CourseList, COURSE_FILE


class TestCourseMethods(unittest.TestCase):
    def setUp(self):
        # Clear the courses file before each test
        if os.path.exists(COURSE_FILE):
            os.remove(COURSE_FILE)
        self.course_list = CourseList()

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(COURSE_FILE):
            os.remove(COURSE_FILE)

    def test_add_course(self):
        # Test adding a course
        print("Running test to add a course")
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        print("Course added:", end=" ")
        print(course)
        self.assertEqual(course.name, "Test Course", "ERROR: course.name was added unsuccessfully")
        self.assertEqual(course.description, "This is a test course", "ERROR: course.description was added unsuccessfully")
        self.assertEqual(course.code, "TC101", "ERROR: course.code was added unsuccessfully")
        self.assertEqual(course.start_date, "2023-06-01", "ERROR: course.start_date was added unsuccessfully")
        self.assertEqual(course.end_date, "2023-06-30", "ERROR: course.end_date was added unsuccessfully")
        print("Course added successfully")
        print()

    def test_add_course_to_list(self):
        # Test adding a course to the CourseList
        print("Running test to add course to CourseList")
        course_list = CourseList()
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        course_list.add_course(course)
        self.assertIn(course, course_list.courses, "ERROR: Course is not found in list")
        print(course_list.courses[0].name)
        self.assertEqual(len(course_list.courses), 1, "ERROR: Expected to have only 1 Course object, but got " + str(len(course_list.courses)) + " instead")
        print("Course added successfully to list")
        print()

    def test_delete_course_from_list(self):
        # Test deleting a course from the CourseList
        print("Running test to delete a course from CourseList")
        course_list = CourseList()
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        course_list.add_course(course)
        self.assertIn(course, course_list.courses, "ERROR: Course not found in list")
        course_list.delete_course(1)
        self.assertNotIn(course, course_list.courses, "ERROR: Course should be deleted, but still exists")
        self.assertEqual(len(course_list.courses), 0, "ERROR: list should be empty, but found " + str(len(course_list.courses)) + " object(s)")
        print("Course deleted successfully from CourseList")
        print()

    def test_edit_course(self):
        # Test editing a course
        print("Running test to edit a course")
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        print("Course added:", end=" ")
        print(course)
        course.name = "Updated Test Course"
        course.description = "This is an updated test course"
        course.code = "TC102"
        course.start_date = "2023-07-01"
        course.end_date = "2023-07-31"
        print("Course after editing:", end=" ")
        print(course)
        self.assertEqual(course.name, "Updated Test Course", "ERROR: Unable to change course.name")
        self.assertEqual(course.description, "This is an updated test course", "ERROR: Unable to change course.description")
        self.assertEqual(course.code, "TC102", "ERROR: Unable to change course.code")
        print("Course edited successfully")
        print()

    def test_add_course_with_empty_name(self):
        # Test adding a course with an empty name
        print("Running test to add a course with an empty name")
        course = Course(
            1, "", "This is a test course", "TC101", "2023-06-01", "2023-06-30"
        )
        print("Course added:", end=" ")
        print(course)
        self.assertEqual(course.name, "", "ERROR: course.name should be empty")
        print("Course added successfully")
        print()

    def test_add_course_with_empty_description(self):
        # Test adding a course with an empty description
        print("Running test to add a course with an empty description")
        course = Course(1, "Test Course", "", "TC101", "2023-06-01", "2023-06-30")
        print("Course added:", end=" ")
        print(course)
        self.assertEqual(course.description, "", "ERROR: course.description should be empty")
        print("Course added successfully")
        print()

    def test_add_course_with_empty_code(self):
        # Test adding a course with an empty code
        print("Running test to add a course with an empty code")
        course = Course(
            1, "Test Course", "This is a test course", "", "2023-06-01", "2023-06-30"
        )
        print("Course added:", end=" ")
        print(course)
        self.assertEqual(course.code, "", "ERROR: course.code should be empty")
        print("Course added successfully")
        print()

    def test_add_course_with_empty_dates(self):
        # Test adding a course with empty start and end dates
        print("Running test to add a course with empty start and end dates")
        course = Course(1, "Test Course", "This is a test course", "TC101", "", "")
        print("Course added:", end=" ")
        print(course)
        self.assertEqual(course.start_date, "", "ERROR: course.start_date should be empty")
        self.assertEqual(course.end_date, "", "ERROR: course.end_date should be empty")
        print("Course added successfully")
        print()

    def test_delete_non_existent_course(self):
        # Test deleting a non-existent course from the CourseList
        print("Running test to delete a non-existent course from the CourseList, which the existing Course object in CourseList should not be deleted")
        course_list = CourseList()
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        course_list.add_course(course)
        course_list.delete_course(2)
        self.assertIn(course, course_list.courses, "ERROR: Course with course.id of 1 should not be deleted")
        self.assertEqual(len(course_list.courses), 1, "ERROR: course_list should only have 1 course, but " + str(len(course_list.courses)) + " was found")
        print("Success! Existing course is not deleted")
        print()

    def test_edit_course_with_invalid_field(self):
        # Test editing a course with an invalid field
        print("Running test to edit a course with an invalid field, which should throw an error")
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        # Instead of using vars(), we'll check slots
        expected_attrs = {
            "id",
            "name",
            "description",
            "code",
            "end_date",
            "start_date",
            "tasks",
            "completed_tasks",
        }
        actual_attrs = set(course.__slots__)
        self.assertEqual(expected_attrs, actual_attrs, "ERROR: course.__slots__ does not match the original set")
        # Test that we can't add new attributes
        print("Attempting to edit field \"invalid_field\"")
        with self.assertRaises(AttributeError):
            course.invalid_field = "Invalid"
        print("AttributeError successfully thrown, test passed")
        print()

    def test_add_course_with_duplicate_id(self):
        # Test adding a course with a duplicate ID
        print("Running test to add a course with a duplicate ID, which should throw an error")
        course_list = CourseList()
        course1 = Course(
            1,
            "Test Course 1",
            "This is a test course 1",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        print("course1 added:", end=" ")
        print(course1)
        course2 = Course(
            1,
            "Test Course 2",
            "This is a test course 2",
            "TC102",
            "2023-07-01",
            "2023-07-31",
        )
        print("course2 added:", end=" ")
        print(course2)
        course_list.add_course(course1)
        print("course1 added to CourseList")
        print("Attempting to add course2 to CourseList")
        with self.assertRaises(ValueError):
            course_list.add_course(course2)
        print("Success! ValueError is thrown due to the duplicate course_id")
        print()
        

    def test_edit_course_name(self):
        # Test editing a course name
        print("Running test to edit course name")
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        print("Course added:", end=" ")
        print(course)
        course.name = "New Course Name"
        print("Course after editing:", end=" ")
        print(course)
        self.assertEqual(course.name, "New Course Name", "ERROR: course.name edit unsuccessful")
        print("course.name successfully edited")
        print()

    def test_edit_course_description(self):
        # Test editing a course description
        print("Running test to edit course description")
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        print("Course added:", end=" ")
        print(course)
        course.description = "New Course Description"
        print("Course after editing:", end=" ")
        print(course)
        self.assertEqual(course.description, "New Course Description", "ERROR: course.description edit unsuccessful")
        print("course.description successfully edited")
        print()

    def test_edit_course_code(self):
        # Test editing a course code
        print("Running test to edit course code")
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        print("Course added:", end=" ")
        print(course)
        course.code = "NEW101"
        print("Course after editing:", end=" ")
        print(course)
        self.assertEqual(course.code, "NEW101", "ERROR: course.code edit unsuccessful")
        print("course.code successfully edited")
        print()

    def test_edit_course_dates(self):
        # Test editing a course start and end dates
        print("Running test to edit course start and end dates")
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        print("Course added:", end=" ")
        print(course)
        course.start_date = "2023-07-01"
        course.end_date = "2023-07-31"
        print("Course after editing:", end=" ")
        print(course)
        self.assertEqual(course.start_date, "2023-07-01", "ERROR: course.start_date edit unsuccessful")
        self.assertEqual(course.end_date, "2023-07-31", "ERROR: course.end_date edit unsuccessful")
        print("course.start_date and course.end_date successfully edited")
        print()


if __name__ == "__main__":
    unittest.main()
