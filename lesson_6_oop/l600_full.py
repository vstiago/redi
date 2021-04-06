import calendar
from collections import namedtuple
from datetime import date
from math import floor
from typing import Set


class Address:
    def __init__(self, street: str, number: int, postal_code: int, city: str):
        self.street = street
        self.number = number
        self.postal_code = postal_code
        self.city = city

    def __str__(self):
        return f'{self.street} {self.number}\n{self.postal_code} - {self.city}'


# All student attributes have different types: str, date, Address, set, dict
class Student:
    # L603 - class attribute
    email = 'default@redi-school.org'

    # __init__ is called when the object is created, also called instantiating
    # or initialized
    # The first parameter is the object, it's called self by convention, but it
    # can have any other name.
    def __init__(self, name: str, birthday: date, address: Address,
                 courses: Set[str]):
        # Public Attributes
        self.full_name = name
        self.courses = courses

        # Protected Attributes
        # starts with '_'
        # Can be configured as a warning if accessed outside the class, but the
        # program will run.
        self._grades = dict([(course, 0.0) for course in courses])
        self._birthday = birthday
        # _first_name will be initialized only if first_name() is called.
        self._first_name = None

        # Private Attributes
        # starts with '__'
        # Is an error if access outside the class and the program will
        # terminate.
        self.__attendance = []
        # Attributes can be objects too.
        self.__address = address

    # Class Public Methods

    # L605 - Method
    # The first parameter is the object calling it!
    # 'self' is used as convention, but it can be any other name.
    # Other languages call it 'this'
    def is_colleague(self, other):
        course_intersection = self.courses.intersection(other.courses)
        return len(course_intersection) != 0

    # L607 - static method
    # A line starting with '@' is a decorator, it indicates that the following
    # function has a special behaviour, or is used for a different purpose.
    @staticmethod
    def from_csv(input_text):
        # csv: comma separated values
        # a static method that creates an object is also called 'Factory'
        csv = input_text.split(',')
        return Student(csv[0], date.fromisoformat(csv[1]),
                       Address(csv[2], int(csv[3]), int(csv[4]), csv[5]),
                       set(csv[6:]))

    # L608 - Protected
    def is_approved(self):
        # return all(self._grades[subject] >= 5.0 for subject in self._grades)
        for subject in self._grades:
            if self._grades[subject] < 5.0:
                return False
        return True

    def set_grade(self, subject, grade):
        # Validate the input before using it
        if grade < 0 or grade > 10:
            print(f'Invalid grade {grade}. Should be between 0 and 10.')
            return
        if subject not in self._grades:
            print(f'{self.first_name} does not course {subject}.')
            return

        # Since it is an important operation we log it for security reasons.
        print(f"Setting {self.first_name}'s {subject} grade to {grade}")
        self._grades[subject] = grade

    # Don't return the set, but a string representation of it.
    def grades(self) -> str:
        return str(self._grades)

    # L609 - Private
    def add_attendance(self, is_present: True):
        self.__attendance.append(is_present)

    def attendance(self) -> float:
        num_attendances = len(self.__attendance)
        if num_attendances == 0:
            return 0.0
        else:
            total_present = sum(self.__attendance)
            return total_present / num_attendances

    # L610 - str
    # As the __init__ method, __str__ is a reserved name used to convert an
    # object to string.
    def __str__(self):
        return f'{self.full_name}: {self._birthday} - {self.courses}'

    # L611 - Property
    @property
    def birthday(self):
        print(f'{self.first_name} birthday accessed!')
        return self._birthday

    @birthday.setter
    def birthday(self, new_value):
        if new_value < '1899':
            print('Vampires are not allowed.')
            return
        if new_value > '2100':
            print('Time travellers are not allowed.')
            return

        print(f'Changing {self.first_name}  birthday.')
        # self._birthday = new_value

    @property
    def first_name(self) -> str:
        if self._first_name is None:
            self._first_name = self.full_name.split(' ')[0]
        return self._first_name

    @first_name.setter
    def first_name(self, new_value: str):
        self._first_name = new_value

    # L613 - Composition
    def print_address(self):
        print(self.__address)

    @property
    def age(self) -> int:
        # date.today() is a static method.
        # We don't need to worry about how the date difference is calculated,
        # these details are handled by the datetime.date class.
        diff = date.today() - self.birthday
        return floor(diff.days / 365.25)

    def weekday(self) -> str:
        return calendar.day_name[self.birthday.weekday()]


# Objects
john = Student('John Schneider', date(2010, 4, 5),
               Address('MarienPlatz', 1, 80500, 'Munich'),
               {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', date(2010, 5, 6),
               Address('LudwigStrasse', 232, 80600, 'Munich'),
               {'German', 'Math', 'Geography', 'Science'})
lucy = Student('Lucy Schwarz', date(2010, 7, 8),
               Address('LeopoldStrasse', 13, 80700, 'Munich'),
               {'English', 'Math', 'Dance'})

# Public attributes can always be accessed
print(f'{john.first_name}, {john.birthday}')
# John, 2010-04-05


# 'names_list' is just a temporary variable
# print(john.names_list)
# AttributeError: 'Student' object has no attribute 'names_list'


# The values in the attributes can be changed
mary.first_name = 'Maria'
print(f'{mary.full_name}, born in {mary.birthday} aka "{mary.first_name}"')
# Mary von Neumann, born in 2010-05-06 aka "Maria"


# New attributes can be added to an object
lucy.personal_email = 'lucy@gmail.org'
print(f'{lucy.first_name} can be contacted at {lucy.personal_email}')
# Lucy can be contacted at lucy@redi-school.org


# But the other instance does not have it.
# print(f'{john.first_name} can be contacted at {john.personal_email}')
# AttributeError: 'Student' object has no attribute 'personal_email'


# New attributes can be added to the Class.
Student.personal_email = 'default@redi-school.org'
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.personal_email}')
# John:default@redi-school.org
# Maria:default@redi-school.org
# Lucy:lucy@redi-school.org


# Changing the class attribute will be visible if the object does not have an
# attribute with the same name
Student.personal_email = 'default@redi.org'
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.personal_email}')
# John:default@redi.org
# Maria:default@redi.org
# Lucy:lucy@redi-school.org


# Changing the attribute for an object doesn't affect the class attribute.
john.personal_email = 'john@redi.org'
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.personal_email}')
# John:john@redi.org
# Maria:default@redi.org
# Lucy:lucy@redi-school.org


# Attributes can be deleted.
del john.personal_email
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.personal_email}')
# John:default@redi.org
# Maria:default@redi.org
# Lucy:lucy@redi-school.org


# So can class attributes.
del Student.personal_email
# for student in [john, mary]:
#     print(f'{student.first_name}:{student.personal_email}')
# AttributeError: 'Student' object has no attribute 'personal_email'


# But it doesn't affect the object
print(f'{lucy.first_name}:{lucy.personal_email}')

# L602 - Class Attribute


# The class attribute can be changed for a single object
lucy.email = 'lucy@redi-school.org'
print(f'{lucy.first_name} can be contacted at {lucy.email}')
# Lucy can be contacted at lucy@redi-school.org


# But it didn't change the others
print(f'{john.first_name} can be contacted at {john.email}')
# John can be contacted at default@redi-school.org


# Or for all objects that didn't have changed it.
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.email}')
# John:default@redi.org
# Mary:default@redi.org
# Lucy:lucy@redi-school.org


# Changing the class attribute will be visible if the object does not have an
# attribute with the same name
Student.email = 'default@redi.org'
for student in [john, mary, lucy]:
    # Note that there is no warning at email now.
    print(f'{student.first_name}:{student.email}')
# John:default@redi.org
# Maria:default@redi.org
# Lucy:lucy@redi-school.org


# Changing the attribute for an object doesn't affect the class attribute.
john.class_email = 'john@redi.org'
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.email}')
# John:john@redi.org
# Maria:default@redi.org
# Lucy:lucy@redi-school.org


# L603 - Attributes in different classes


# Attributes in different classes are isolated, changing one class does not
# affected the other, the same way that changing an object does not modify
# another.


email = 'contact@redi-school.org'


class Teacher:
    email = 'teacher@redi-school.org'

    def __init__(self, name: str, address: Address):
        # class public attributes
        self.full_name = name
        self.address = address


print('email:', email)
# email: contact@redi-school.org

print('Student.email:', Student.email)
# Student.email: student@redi-school.org

print('Teacher.email:', Teacher.email)
# Teacher.email: teacher@redi-school.org


tiago = Teacher('Tiago Vieira', Address('LudwigStrasse', 232, 80600, 'Munich'))

# If the instance does not have the attribute it will access the class
# attribute.
print('john.email:', john.email)
# john.email: student@redi-school.org

print('tiago.email:', tiago.email)
# tiago.email: teacher@redi-school.org


# Changing the instance attribute does not change the class.
john.email = 'john@redi-school.org'
print('john.email:', john.email)
# john.email: john@redi-school.org

print('Student.email:', Student.email)
# Student.email: student@redi-school.org


# Changing the class changes how it is visible in the object.
Teacher.email = 'python.teacher@redi-school.org'
print('Teacher.email:', Teacher.email)
# Teacher.email: python.teacher@redi-school.org

print('tiago.email:', tiago.email)
# tiago.email: python.teacher@redi-school.org


# But changing the class does not affect the instance if they have their own
# attribute.
Student.email = 'python.student@redi-school.org'
print('Student.email:', Student.email)
# Student.email: python.student@redi-school.org


print('john.email:', john.email)
# john.email: john@redi-school.org


# L604 - Function


def are_colleagues(a, b):
    course_intersection = a.courses.intersection(b.courses)
    return len(course_intersection) != 0


if are_colleagues(john, mary):  # True
    print(f'{john.first_name} and {mary.first_name} are colleagues')

if are_colleagues(john, lucy):  # False
    print(f'{john.first_name} and {lucy.first_name} are colleagues')

if are_colleagues(mary, lucy):  # True
    print(f'{mary.first_name} and {lucy.first_name} are colleagues')


# L605 - Method


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
#      print(f'{mary.first_name} and {mark[0]} are colleagues')
# AttributeError: 'tuple' object has no attribute 'courses'


StudentTuple = namedtuple("StudentTuple", "first_name email courses")
alice = StudentTuple('Alice', 'alice@gmail.com', {'German', 'Math'})


# It works because the tuple has a field name 'courses'
if lucy.is_colleague(alice):
    print(f'{lucy.first_name} and {alice.first_name} are colleagues')


# But the tuple does not have the method.
# if alice.is_colleague(lucy):
#      print(f'{alice.first_name} and {lucy.first_name} are colleagues')
# AttributeError: 'StudentTuple' object has no attribute 'is_colleague'


# L606 - isinstance


print(isinstance(john, Student))
# True

print(isinstance(mark, Student))
# False

print(isinstance(alice, Student))
# False

print(isinstance(tiago, Teacher))
# True


# L607 - Class Method


# Creating a object with the from_csv function
other_lucy = Student.from_csv('Lucy Schwarz,2010-07-08,LeopoldStrasse,13,80700,Munich,English,Math,Dance')

print(other_lucy.first_name, other_lucy.birthday, other_lucy.courses)
# Lucy 2010-07-08 {'Dance', 'Math', 'English'}


# Both objects have the same type.
print(type(mary))
# <class '__main__.Student'>


print(type(other_lucy))
# <class '__main__.Student'>


# type() returns the name of the module and the class.
# The name of the module changes when the module is loaded directly and when it
# is imported.
# If we import this file, the same code will print something like:
# <class 'lesson_6.l607_class_method.Student'>


# L608 - Attributes Protected


# False since all grades are initialized with 0.0
if john.is_approved():
    print(f'Congrats {john.first_name}')

# The protected fields can be accessed (but it's not a good practice)
print('John grades:', john._grades)
# John grades: {'German': 0.0, 'Arts': 0.0, 'History': 0.0}


# When an attribute is accessed freely it can receive unexpected values
mary._grades['Math'] = 11.0
print('Mary grades:', mary._grades)
# Mary grades: {'German': 0.0, 'Math': 11.0, 'Geography': 0.0, 'Science': 0.0}


# When using the proper methods the class can verifies and sanitize the input.
lucy.set_grade('English', 8.3)
lucy.set_grade('Math', 9.4)
lucy.set_grade('Dance', 6.7)

lucy.set_grade('German', 5.4)
# Lucy does not course German.


lucy.set_grade('Math', 11.0)
# Invalid grade 11.0. Should be between 0 and 10.


# Student.grades() don't access the protected attribute directly, but receives
# the string created from it.
print('Lucy grades:', lucy.grades())
# Lucy grades: {'English': 8.3, 'Dance': 6.7, 'Math': 9.4}

# Private attributes will generate an error if accessed outside the class.
# print('Attendance:', john.__attendance)
# AttributeError: 'Student' object has no attribute '__attendance'


for value in [True, True, True, False, True]:
    john.add_attendance(value)

print(f'John attendance {100 * john.attendance()}%')
# John attendance 80.0%


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
# [False, False, False, True]


# It is possible to see all existing attributes
print(vars(lucy))
# {'full_name': 'Lucy Schwarz', 'first_name': 'Lucy', 'birthday': '2010-07-08',
# 'courses': {'Math', 'Dance', 'English'},
# '_grades': {'Math': 0.0, 'Dance': 0.0, 'English': 0.0},
# '_Student__attendance': [False, False, False, True],
# '__attendance': [True]}


# L609 - Private


# Private attributes will generate an error if accessed outside the class.
# print('Attendance:', john.__attendance)
# AttributeError: 'Student' object has no attribute '__attendance'


for value in [True, True, True, False, True]:
    john.add_attendance(value)

print(f'John attendance {100 * john.attendance()}%')
# John attendance 80.0%


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
# [False, False, False, True]


# It is possible to see all existing attributes
print(vars(lucy))
# {'full_name': 'Lucy Schwarz', 'first_name': 'Lucy', 'birthday': '2010-07-08',
# 'courses': {'Math', 'Dance', 'English'},
# '_grades': {'Math': 0.0, 'Dance': 0.0, 'English': 0.0},
# '_Student__attendance': [False, False, False, True],
# '__attendance': [True]}


# L610 - __str__


# It can be called as simple as:
print(john)
# John Schneider: 2010-04-05 - {'German', 'Arts', 'History'}


# explicitly as a method
print(mary.__str__())
# Mary von Neumann: 2010-05-06 - {'German', 'Math', 'Science', 'Geography'}


# or via the class syntax.
print(Student.__str__(lucy))
# Lucy Schwarz: 2010-07-08 - {'English', 'Math', 'Dance'}


# It will be called always when python needs to make the string conversion.
john_str = str(john)
mary_str = f'Hello, {mary}'
lucy_str = 'Welcome %s' % lucy

print(john_str, mary_str, lucy_str, sep='\n')
# John Schneider: 2010-04-05 - {'History', 'Arts', 'German'}
# Hello, Mary von Neumann: 2010-05-06 - {'Math', 'Geography', 'Science', 'German'}
# Welcome Lucy Schwarz: 2010-07-08 - {'English', 'Dance', 'Math'}


# L611 - Property


# The code that uses does not does not change.
print(john.birthday)
# John birthday accessed!
# 2010-04-05

john.birthday = '1880-11-21'
# Vampires are not allowed.

mary.birthday = '2100-05-23'
# Time travellers are not allowed.


# The assignment failed and the attribute didn't change.
print(mary.birthday)
# Mary birthday accessed!
# 2010-05-06


lucy.birthday = '2000-01-01'
# Changing Lucy birthday.


print(lucy.birthday)
# Lucy birthday accessed!
# 2000-01-01


# L612 - Method override


for value in [True, True, True, False, True]:
    john.add_attendance(value)

print(f'John attendance {100 * john.attendance()}%')
# John attendance 80.0%


for value in [False, False, False, True]:
    lucy.add_attendance(value)

# Methods are attributes too. They can be redefined and have custom execution.

print(f'Lucy attendance {100 * lucy.attendance()}%')


# Lucy attendance 25.0%


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
# Lucy attendance 25.0%


# L613 - Composition
# Methods can use the attributes internally.
john.print_address()
# LandsbergerStrasse 40
# 80780 - München

print(john.age)
# 11

print(f"John's favourite weekday is {john.weekday()}")
# John's favourite weekday is Monday.


# We can access attributes inside the attributes
print(john.birthday.year)
# 2010

print(tiago.address.city)
# Berlin


# L614 - dynamic types

# The type of a variable can change during program execution.

secret_value = 42
print(type(secret_value))
# <class 'int'>

secret_value = 'Hello World!'
print(type(secret_value))
# <class 'str'>

secret_value = True
print(type(secret_value))
# <class 'bool'>

secret_value = [1.414, 1.161, 2.718, 3.141, ]
print(type(secret_value))
# <class 'list'>

secret_value = john
print(type(secret_value))
# <class '__main__.Student'>

# Some functions only make sense for some type of date.
# abs() works for types like bool, int, float.
abs(42)
abs(True)

# but makes no sense for string or lists
# abs('Hello World!')
# TypeError: bad operand type for abs(): 'str'

# abs([1.414, 1.161, 2.718, 3.141, ])
# TypeError: bad operand type for abs(): 'list'


# L615 - Type Annotation

# Objects
bad_john = Student('John Schneider', date(2010, 4, 5),
                   Address('MarienPlatz', 1, 80500, 'Munich'),
                   ['German', 'Arts', 'History'])
# Expected type 'set', got 'List[str]' instead


bad_mary = Student('Mary von Neumann', '2010-05-06',
                   Address('LudwigStrasse', 232, 80600, 'Munich'),
                   {'German', 'Math', 'Geography', 'Science'})
# Expected type 'date', got 'str' instead


# See that the warning is different from the error.
bad_lucy = Student(3.14, date(2010, 7, 8),
                   Address('LeopoldStrasse', 13, 80700, 'Munich'),
                   {'English', 'Math', 'Dance'})
# Expected type 'str', got 'float' instead


# The data can be accessed.
print(bad_john.courses)
# ['German', 'Arts', 'History']


# But the function fails
if bad_john.is_colleague(mary):
    print(f'{bad_john.first_name} and {bad_mary.first_name} are colleagues')
# AttributeError: 'list' object has no attribute 'intersection'


# Variables can have type hints too.
# The property method works!
min_age: int = min([student.age for student in [bad_john, bad_lucy]])
print(min_age)
# 10


# This generates a warning, but it does not terminate the program.
max_age: int = '43'
# Expected type 'int', got 'str' instead


# The error happens here, but there is no warning.
print(bad_mary.age)
# TypeError: unsupported operand type(s) for -: 'datetime.date' and 'str'


print(bad_lucy.first_name)
# AttributeError: 'float' object has no attribute 'split'
