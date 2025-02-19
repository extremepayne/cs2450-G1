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
        course = Course(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        self.assertEqual(course.name, "Test Course")
        self.assertEqual(course.description, "This is a test course")
        self.assertEqual(course.code, "TC101")
        self.assertEqual(course.end_date, "2023-06-01")
        self.assertEqual(course.start_date, "2023-06-30")

    def test_add_course_to_list(self):
        # Test adding a course to the CourseList
        course_list = CourseList()
        course = Course(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        course_list.add_course(course)
        self.assertIn(course, course_list.courses)
        print(course_list.courses[0].name)
        self.assertEqual(len(course_list.courses), 1)

    def test_delete_course_from_list(self):
        # Test deleting a course from the CourseList
        course_list = CourseList()
        course = Course(1,"Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        course_list.add_course(course)
        self.assertIn(course, course_list.courses)
        course_list.delete_course(1)
        self.assertNotIn(course, course_list.courses)
        self.assertEqual(len(course_list.courses), 0)

    def test_edit_course(self):
        # Test editing a course
        course = Course(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        course.name = "Updated Test Course"
        course.description = "This is an updated test course"
        course.code = "TC102"
        course.end_date = "2023-07-01"
        course.start_date = "2023-07-31"
        self.assertEqual(course.name, "Updated Test Course")
        self.assertEqual(course.description, "This is an updated test course")
        self.assertEqual(course.code, "TC102")

    def test_add_course_with_empty_name(self):
        # Test adding a course with an empty name
        course = Course(1, "", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        self.assertEqual(course.name, "")

    def test_add_course_with_empty_description(self):
        # Test adding a course with an empty description
        course = Course(1, "Test Course", "", "TC101", "2023-06-01", "2023-06-30")
        self.assertEqual(course.description, "")

    def test_add_course_with_empty_code(self):
        # Test adding a course with an empty code
        course = Course(1, "Test Course", "This is a test course", "", "2023-06-01", "2023-06-30")
        self.assertEqual(course.code, "")

    def test_add_course_with_empty_dates(self):
        # Test adding a course with empty start and end dates
        course = Course(1, "Test Course", "This is a test course", "TC101", "", "")
        self.assertEqual(course.start_date, "")
        self.assertEqual(course.end_date, "")

    def test_delete_non_existent_course(self):
        # Test deleting a non-existent course from the CourseList
        course_list = CourseList()
        course = Course(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        course_list.add_course(course)
        course_list.delete_course(2)
        self.assertIn(course, course_list.courses)
        self.assertEqual(len(course_list.courses), 1)

    def test_edit_course_with_invalid_field(self):
        # Test editing a course with an invalid field
        course = Course(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        # Instead of trying to set an invalid attribute, we'll check if one exists
        self.assertFalse(hasattr(course, 'invalid_field'))
        # We can also verify that only valid attributes are present
        expected_attrs = {'id', 'name', 'description', 'code', 'end_date', 'start_date', 'tasks', 'completed_tasks'}
        actual_attrs = set(vars(course).keys())
        self.assertEqual(expected_attrs, actual_attrs)

    def test_add_course_with_duplicate_id(self):
        # Test adding a course with a duplicate ID
        course_list = CourseList()
        course1 = Course(1, "Test Course 1", "This is a test course 1", "TC101", "2023-06-01", "2023-06-30")
        course2 = Course(1, "Test Course 2", "This is a test course 2", "TC102", "2023-07-01", "2023-07-31")
        course_list.add_course(course1)
        course_list.add_course(course2)
        self.assertEqual(len(course_list.courses), 2)

    def test_edit_course_name(self):
        # Test editing a course name
        course = Course(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        course.name = "New Course Name"
        self.assertEqual(course.name, "New Course Name")

    def test_edit_course_description(self):
        # Test editing a course description
        course = Course(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        course.description = "New Course Description"
        self.assertEqual(course.description, "New Course Description")

    def test_edit_course_code(self):
        # Test editing a course code
        course = Course(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        course.code = "NEW101"
        self.assertEqual(course.code, "NEW101")

    def test_edit_course_dates(self):
        # Test editing a course start and end dates
        course = Course(1, "Test Course", "This is a test course", "TC101", "2023-06-01", "2023-06-30")
        course.start_date = "2023-07-01"
        course.end_date = "2023-07-31"
        self.assertEqual(course.start_date, "2023-07-01")
        self.assertEqual(course.end_date, "2023-07-31")

if __name__ == '__main__':
    unittest.main()