from student import Student
from course import Course
from student_report import StudentReport


def main():
    print("Welcome to first ever Console App of our learning Center")


if __name__ == "__main__":
    member_type = input("Are you Student (y/n): ")
    if member_type.lower() == 'y':
        s1 = Student()
        res = 'y'
        while res.lower() == 'y':
            user_input = int(input("Choose an Option: \n 1 -> Viewing Course \n 2 -> Registering in Course \n"))
            if user_input == 2:
                res = s1.register_student()
                print(res)
            elif user_input == 1:
                c1 = Course()
                print(c1.view_course_outline())

            res = input("Do You wanna continue (y/n): ")
            if res.lower() != 'y':
                print("Bye Bye")
                break

    else:
        report = StudentReport()
        res = 'y'
        while res.lower() == 'y':
            user_input = int(input("Choose an Option: \n 1 -> View All Student \n 2 -> Total Number of Student  \n"))
            if user_input == 1:
                print('name', 'email', 'address', 'deposited_amount', 'remaining_amount')
                result = report.display_all_student()
                for row in result:
                    print(row)
            elif user_input == 2:
                result = report.total_number_student()
                print(result)

            res = input("Do You wanna continue (y/n): ")
            if res.lower() != 'y':
                print("Bye Bye")
                break
