class Course:
    def __init__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.enrollments = ()

    def get_course_id(self):
        return self.course_id

    def get_course_name(self):
        return self.course_name

    def get_course_code(self):
        return self.course_code


    def get_instructor_name(self):
        return self.instructor_name

    def assign_teacher(self, teacher):
        self.instructor_name = f"{teacher.first_name} {teacher.last_name}"

    def update_course_info(self, course_code, course_name, instructor_name):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor_name = instructor_name

    def display_course_info(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor_name}")

    def get_enrollments(self):
        return self.enrollments

    def get_teacher(self):
        return self.instructor_name

'''c=Course(11,"cse_ml",11,"Anji")
c.display_course_info()'''