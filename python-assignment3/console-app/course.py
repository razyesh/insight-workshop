class Course:
    """
    Simple Course class where the detail outline of the course can be defined
    """
    def __init__(self):
        pass

    @staticmethod
    def view_course_outline():
        with open('course_info.txt') as course_file:
            return course_file.read()