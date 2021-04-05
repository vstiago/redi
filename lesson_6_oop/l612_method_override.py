class Student:
    def __init__(self, name, birthday, courses):
        # public attributes
        self.full_name = name
        self.first_name = name.split(' ')[0]
        self.birthday = birthday
        self.courses = courses

        # protected attributes
        self._grades = dict([(course, 0.0) for course in courses])

        # private attributes
        self.__attendance = []

    # class public methods
    def add_attendance(self, is_present):
        self.__attendance.append(is_present)

    def attendance(self):
        total = sum(self.__attendance)
        return total / len(self.__attendance)


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
lucy = Student('Lucy Schwarz', '2010-07-08', {'English', 'Math', 'Dance'})


for value in [True, True, True, False, True]:
    john.add_attendance(value)

print(f'John attendance {100 * john.attendance()}%')
# John attendance 80.0%


for value in [False, False, True]:
    lucy.add_attendance(value)


# Methods are attributes too. They can be redefined and have custom execution.

print(f'Lucy attendance {100 * lucy.attendance()}%')
# Lucy attendance 33.33333333333333%


# Defining a function that will be called instead.
def fake_attendance():
    print('Override the attendance method. Ignoring the real value.')
    return 1.0


# Assign the function as the method. Note that the function is not being called
# here.
lucy.attendance = fake_attendance


# It's called here.
print(f'Lucy attendance {100 * lucy.attendance()}%')
# Override the attendance method. Ignoring the real value.
# Lucy attendance 100.0%


# Calling the class method is not changed.
print(f'Lucy attendance {100 * Student.attendance(lucy)}%')
# Lucy attendance 33.33333333333333%%
