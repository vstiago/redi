from datetime import date
from math import floor
import calendar


class Address:
    def __init__(self, street, number, postal_code, city):
        self.street = street
        self.number = number
        self.postal_code = postal_code
        self.city = city

    def __str__(self):
        return f'{self.street} {self.number}\n{self.postal_code} - {self.city}'


# Student attributes have all different types: str, date, Address, set, dict
class Student:
    def __init__(self, name, birthday, address, courses):
        # public attributes
        self.full_name = name
        names = name.split(' ')
        self.first_name = names[0]
        self.birthday = birthday
        self.courses = courses

        # protected attributes
        self._grades = dict([(course, 0.0) for course in courses])

        # private attributes
        self.__attendance = []
        # Attributes can be objects too.
        self.__address = address

    def print_address(self):
        print(self.__address)

    def age(self):
        # date.today() is a static method.
        # We don't need to worry about how the date difference is calculated,
        # these details are handled by the class.
        diff = date.today() - self.birthday
        return floor(diff.days / 365.25)

    def weekday(self):
        return calendar.day_name[self.birthday.weekday()]


# Other classes can use Address too
class Teacher:
    def __init__(self, name, address):
        # public attributes
        self.full_name = name
        # And they can be used by any class.
        self.address = address


# Objects
john = Student('John Schneider', date(2010, 4, 5),
               Address('LandsbergerStrasse', 40, 80780, 'München'),
               {'German', 'Arts', 'History'})
tiago = Teacher('Tiago Vieira',
                Address('Zinnowitzerstrasse', 8, 10115, 'Berlin'))


# Methods can use the attributes internally.
john.print_address()
# LandsbergerStrasse 40
# 80780 - München

print(john.age())
# 11

print(f"John's favourite weekday is {john.weekday()}")
# John's favourite weekday is Monday.


# We can access attributes inside the attributes
print(john.birthday.year)
# 2010

print(tiago.address.city)
# Berlin
