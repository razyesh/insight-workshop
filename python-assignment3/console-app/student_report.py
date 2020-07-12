import csv


class StudentReport:
    """
    Class to present the report about the student
    """
    def __int__(self):
        print("Displaying the Report of all the student registered in our program")

    @staticmethod
    def display_all_student():
        """
        this method displays all the students
        :return:
        """
        with open('students.csv', newline='') as student_file:
            reader = csv.DictReader(student_file,  skipinitialspace=True)
            return reader

    @staticmethod
    def total_number_student():
        """
        this method returns the total number of students
        :return:
        """
        with open('students.csv', newline='') as student_file:
            student_file_reader = csv.reader(student_file)
            return len(student_file_reader)
