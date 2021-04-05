class Student:
    def __init__(self, name, birthday, courses):
        # class public attributes
        self.full_name = name
        self.first_name = name.split(' ')[0]
        self.birthday = birthday
        self.courses = courses
        self.attendance = []


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
lucy = Student('Lucy Schwarz', '2010-07-08', {'English', 'Math', 'Dance'})


def are_colleagues(a, b):
    course_intersection = a.courses.intersection(b.courses)
    return len(course_intersection) != 0


if are_colleagues(john, mary):  # True
    print(f'{john.first_name} and {mary.first_name} are colleagues')

if are_colleagues(john, lucy):  # False
    print(f'{john.first_name} and {lucy.first_name} are colleagues')

if are_colleagues(mary, lucy):  # True
    print(f'{mary.first_name} and {lucy.first_name} are colleagues')
