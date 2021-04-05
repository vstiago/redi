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
    def is_colleague(self, other):
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
        return Student(csv[0], csv[1], set(csv[2:]))


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})


# Creating a object with the from_csv function
lucy = Student.from_csv('Lucy Schwarz,2010-07-08,English,Math,Dance')


print(lucy.first_name, lucy.birthday, lucy.courses)
# Lucy 2010-07-08 {'Dance', 'Math', 'English'}


# Both objects have the same type.
print(type(mary))
# <class '__main__.Student'>

print(type(lucy))
# <class '__main__.Student'>


# type() returns the name of the module and the class.
# The name of the module changes when the module is loaded directly and when it
# is imported.
# If we import this file, the same code will print something like:
# <class 'lesson_6.l607_class_method.Student'>
