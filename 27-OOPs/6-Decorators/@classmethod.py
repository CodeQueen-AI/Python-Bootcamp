class Student:
    school_name = "ABC School"

    @classmethod
    def show_school(cls):
        print("School Name:", cls.school_name)

Student.show_school()
