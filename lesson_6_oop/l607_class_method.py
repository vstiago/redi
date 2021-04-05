class Student:
    # class initialization method
    def __init__(self, name, birthday, courses):
        # class public attributes
        self.full_name = name
        self.first_name = name.split(' ')[0]
        self.birthday = birthday
        self.courses = courses
        self.attendance = []

    # class public methods
    def are_colleagues(self, other):
        course_intersection = self.courses.intersection(other.courses)
        return len(course_intersection) != 0

    # A line starting with '@' is a decorator, it indicates that the following
    # function has a special behaviour, or is used for a different purpose.
    # @staticmethod
    @staticmethod
    def from_csv(input_text):
        # csv: comma separated values
        # a static method that creates an object is also called 'Factory'
        csv = input_text.split(',')
        return Student(csv[0, csv[1]], set(csv[2:]))


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
# Creating a object with the from_csv function
lucy = Student.from_csv('Lucy Schwarz,2010-07-08,English,Math,Dance')
