class Course:
    def __init__(self, id, name, description, code, end_date, start_date):
        self.id = id
        self.name = name
        self.description = description
        self.code = code
        self.end_date = end_date
        self.start_date = start_date
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)


class CourseList:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def delete_course(self, id):
        self.courses = [course for course in self.courses if course.id != id]
