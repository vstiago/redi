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
    def is_colleagues(self, other):
        # Verifies if the 'other' object is a instance of Student class.
        if not isinstance(other, Student):
            print(other, 'is not a instance of class Student')
            return False
        course_intersection = self.courses.intersection(other.courses)
        return len(course_intersection) != 0


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
lucy = Student('Lucy Schwarz', '2010-07-08', {'English', 'Math', 'Dance'})


mark = ('Mark Hoffmann', '2011-02-03', {'Math', 'Science'})

# Note that the error is different from before!
if mary.is_colleagues(mark):
    print(f'{mary.first_name} and {mark[0]} are colleagues')
# ('Mark Hoffmann', '2011-02-03', {'Science', 'Math'}) is not a instance of class Student

StudentTuple = namedtuple("StudentTuple", "first_name email courses")
alice = StudentTuple('Alice', 'alice@gmail.com', {'German', 'Math'})

# Before it worked, but now we are more strict!
if lucy.is_colleagues(alice):
    print(f'{lucy.first_name} and {alice.first_name} are colleagues')
# StudentTuple(first_name='Alice', email='alice@gmail.com', courses={'German', 'Math'}) is not a instance of class Student
