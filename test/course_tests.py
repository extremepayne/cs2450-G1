import unittest
from src.course import Course
from src.course import CourseList


class TestCourseMethods(unittest.TestCase):

    def test_add_course(self):
        # Test adding a course
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        self.assertEqual(course.name, "Test Course")
        self.assertEqual(course.description, "This is a test course")
        self.assertEqual(course.code, "TC101")
        self.assertEqual(course.end_date, "2023-06-01")
        self.assertEqual(course.start_date, "2023-06-30")

    def test_add_course_to_list(self):
        # Test adding a course to the CourseList
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
        self.assertIn(course, course_list.courses)
        self.assertEqual(len(course_list.courses), 1)

    def test_delete_course_from_list(self):
        # Test deleting a course from the CourseList
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
        self.assertIn(course, course_list.courses)
        course_list.delete_course(1)
        self.assertNotIn(course, course_list.courses)
        self.assertEqual(len(course_list.courses), 0)

    def test_edit_course(self):
        # Test editing a course
        course = Course(
            1,
            "Test Course",
            "This is a test course",
            "TC101",
            "2023-06-01",
            "2023-06-30",
        )
        course.name = "Updated Test Course"
        course.description = "This is an updated test course"
        course.code = "TC102"
        course.end_date = "2023-07-01"
        course.start_date = "2023-07-31"
        self.assertEqual(course.name, "Updated Test Course")
        self.assertEqual(course.description, "This is an updated test course")
        self.assertEqual(course.code, "TC102")


if __name__ == "__main__":
    unittest.main()
