class Address:
    def __init__(self, street, number, postal_code, city):
        self.street = street
        self.number = number
        self.postal_code = postal_code
        self.city = city

    def __str__(self):
        return f'{self.street} {self.number}\n{self.postal_code} - {self.city}'


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


class Teacher:
    def __init__(self, name, address):
        # public attributes
        self.full_name = name
        # And they can be used by any class.
        self.address = address


# Objects
john = Student('John Schneider', '2010-04-05',
               Address('LandsbergerStrasse', 40, 80780, 'München'),
               {'German', 'Arts', 'History'})
tiago = Teacher('Tiago Vieira',
                Address('Zinnowitzerstrasse', 8, 10115, 'Berlin'))


john.print_address()
# LandsbergerStrasse 40
# 80780 - München

print(tiago.address.city)
# Berlin
