class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
        StudentDatabase.add_student(self)


class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


s1 = Student("S101", "Alice Smith", "Computer Science", True)
s2 = Student("S102", "Bob Johnson", "Mathematics", False)
s3 = Student("S103", "Charlie Lee", "Physics", True)
