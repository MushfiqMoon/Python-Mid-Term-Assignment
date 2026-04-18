
class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.student_list.append(self)

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_is_enrolled(self):
        return self.__is_enrolled

    def enroll_student(self):
        if self.__is_enrolled:
            print(f"Student {self.__student_id} is already Enrolled.")
        else:
            self.__is_enrolled = True
            print(f"Student {self.__student_id} has been Enrolled.")

    def drop_student(self):
        if not self.__is_enrolled:
            print(f"Student {self.__student_id} is not Enrolled.")
        else:
            self.__is_enrolled = False
            print(f"Student {self.__student_id} has been Dropped.")

    def view_student_info(self):
        print(f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}")


class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


s1 = Student("S101", "Alice Smith", "Computer Science", True)
s2 = Student("S102", "Bob Johnson", "Mathematics", False)
s3 = Student("S103", "Charlie Lee", "Physics", True)


def menu():
    while True:

        print("\n===== Student Management System =====")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            for student in StudentDatabase.student_list:
                student.view_student_info()

        elif choice == "2":
            student_id = input("Enter Student ID to enroll: ")
            found = False

            for student in StudentDatabase.student_list:

                if student.get_student_id() == student_id:
                    student.enroll_student()
                    found = True
                    break

            if not found:
                print("Invalid Student ID. Student not found.")

        elif choice == "3":
            student_id = input("Enter Student ID to drop: ")
            found = False

            for student in StudentDatabase.student_list:
                if student.get_student_id() == student_id:
                    student.drop_student()
                    found = True
                    break

            if not found:
                print("Invalid Student ID. Student not found.")

        elif choice == "4":
            print("Exit... Goodbye!!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

menu()
