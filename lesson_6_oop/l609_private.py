class Student:
    def __init__(self, name, birthday, courses):
        # public attributes
        self.full_name = name
        self.first_name = name.split(' ')[0]
        self.birthday = birthday
        self.courses = courses

        # protected attributes
        # starts with '_'
        # Can be configured as a warning if accessed outside the class, but the
        # program will run.
        self._grades = dict([(course, 0.0) for course in courses])

        # private attributes
        # starts with '__'
        # Is an error if access outside the class and the program will
        # terminate.
        self.__attendance = []

    # class public methods
    def add_attendance(self, is_present):
        self.__attendance.append(is_present)

    def attendance(self):
        num_attendances = len(self.__attendance)
        if num_attendances == 0:
            return 0.0
        else:
            total_present = sum(self.__attendance)
            return total_present / num_attendances


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
lucy = Student('Lucy Schwarz', '2010-07-08', {'English', 'Math', 'Dance'})


# Protected fields can be accessed (but it's not a good practice)
print('John grades:', john._grades)
# John grades: {'German': 0.0, 'Arts': 0.0, 'History': 0.0}


# Private attributes will generate an error if accessed outside the class.
# print('Attendance:', john.__attendance)
# AttributeError: 'Student' object has no attribute '__attendance'

for value in [True, True, True, False, True]:
    john.add_attendance(value)

print(f'John attendance {100 * john.attendance()}%')


for value in [False, False, False, True]:
    lucy.add_attendance(value)


# You can override it locally ...
lucy.__attendance = [True]


# ... and then reference it ...
print(lucy.__attendance)
# [True]


# ... but inside the class the value didn't change.
print(f'Lucy attendance {100 * lucy.attendance()}%')
# Lucy attendance 25.0%


# There is one way to access the private attribute.
# __attribute is expanded to _ClassName__attribute.
# But please, don't do that!
print(lucy._Student__attendance)
# [False, False, True]


# It is possible to see all exiting attributes
print(vars(lucy))
# {'full_name': 'Lucy Schwarz', 'first_name': 'Lucy', 'birthday': '2010-07-08',
# 'courses': {'Math', 'Dance', 'English'},
# '_grades': {'Math': 0.0, 'Dance': 0.0, 'English': 0.0},
# '_Student__attendance': [False, False, False, True],
# '__attendance': [True]}
