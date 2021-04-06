from datetime import date
from math import floor
from typing import Set, List


class Student:
    # Type annotations can be used to give better warning messages and prevent
    # errors from happening.
    # We could use 'set' as the annotation, but 'Set' allows to restrict the
    # type inside the set.
    def __init__(self, name: str, birthday: date, courses: Set[str]):
        # class public attributes
        self.full_name = name
        self.birthday = birthday
        self.courses = courses

        # Attributes can also have annotations.
        self.attendance: List[bool] = []

    # class public methods
    def is_colleague(self, other) -> bool:
        course_intersection = self.courses.intersection(other.courses)
        return len(course_intersection) != 0

    @property
    def first_name(self) -> str:
        return self.full_name.split(' ')[0]

    @property
    def age(self) -> int:
        diff = date.today() - self.birthday
        return floor(diff.days / 365.25)

    def add_attendance(self, new_value: bool) -> None:
        self.attendance.append(new_value)


# Objects
john = Student('John Schneider', date(2010, 4, 5),
               ['German', 'Arts', 'History'])
# Expected type 'set', got 'List[str]' instead


mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
# Expected type 'date', got 'str' instead


# See that the warning is different from the error.
lucy = Student(3.14, date(2010, 7, 8), {'English', 'Math', 'Dance'})
# Expected type 'str', got 'float' instead


# The data can be accessed.
print(john.courses)
# ['German', 'Arts', 'History']


# But the function fails
if john.is_colleagues(mary):
    print(f'{john.first_name} and {mary.first_name} are colleagues')
# AttributeError: 'list' object has no attribute 'intersection'


# Variables can have type hints too.
# The property method works!
min_age: int = min([student.age for student in [john, lucy]])
print(min_age)
# 10


# This generates a warning, but it does not terminate the program.
max_age: int = '43'
# Expected type 'int', got 'str' instead


# The error happens here, but there is no warning.
print(mary.age)
# TypeError: unsupported operand type(s) for -: 'datetime.date' and 'str'


print(lucy.first_name)
# AttributeError: 'float' object has no attribute 'split'
