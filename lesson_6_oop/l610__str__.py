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
    # As the __init__ method, __str__ is a reserved name used to convert an
    # object to string.
    def __str__(self):
        return f'{self.full_name}: {self.birthday} - {self.courses}'


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
lucy = Student('Lucy Schwarz', '2010-07-08', {'English', 'Math', 'Dance'})


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
