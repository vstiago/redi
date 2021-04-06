from collections import namedtuple


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
    # The first parameter is the object calling it!
    # 'self' is used as convention, but it can be any other name.
    # Other languages call it 'this'
    def is_colleague(self, other):
        course_intersection = self.courses.intersection(other.courses)
        return len(course_intersection) != 0


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
lucy = Student('Lucy Schwarz', '2010-07-08', {'English', 'Math', 'Dance'})


# Calling the method from the class.
if Student.is_colleague(john, mary):  # True
    print(f'{john.first_name} and {mary.first_name} are colleagues')


# Or we can call it from the object.
if john.is_colleague(lucy):  # False
    print(f'{john.first_name} and {lucy.first_name} are colleagues')

if mary.is_colleague(lucy):  # True
    print(f'{mary.first_name} and {lucy.first_name} are colleagues')


# Trying with a tuple
mark = ('Mark Hoffmann', '2011-02-03', {'Math', 'Science'})

# if mary.is_colleagues(mark):
#     print(f'{mary.first_name} and {mark[0]} are colleagues')
# AttributeError: 'tuple' object has no attribute 'courses'


StudentTuple = namedtuple("StudentTuple", "first_name email courses")
alice = StudentTuple('Alice', 'alice@gmail.com', {'German', 'Math'})

# It works because the tuple has a field name 'courses'
if lucy.is_colleague(alice):
    print(f'{lucy.first_name} and {alice.first_name} are colleagues')


# But the tuple does not have the method.
# if alice.is_colleagues(lucy):
#     print(f'{alice.first_name} and {lucy.first_name} are colleagues')
# AttributeError: 'StudentTuple' object has no attribute 'is_colleagues'
