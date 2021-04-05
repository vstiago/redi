class Student:
    def __init__(self, name, birthday, courses):
        # public attributes
        self.full_name = name
        self.first_name = name.split(' ')[0]
        self.courses = courses

        # protected attributes
        self._birthday = birthday
        self._grades = dict([(course, 0.0) for course in courses])

        # private attributes
        self.__attendance = []

    # class public methods
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
        self._birthday = new_value


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
lucy = Student('Lucy Schwarz', '2010-07-08', {'English', 'Math', 'Dance'})


john.birthday = '1880-11-21'
# Vampires are not allowed.


print(john.birthday)
# John birthday accessed!
# 2010-04-05


mary.birthday = '2100-05-23'
# Time travellers are not allowed.

print(mary.birthday)
# Mary birthday accessed!
# 2010-05-06


lucy.birthday = '2000-01-01'
# Changing Lucy birthday.


print(lucy.birthday)
# Lucy birthday accessed!
# 2000-01-01
