class Student:
    def __init__(self, name, birthday, courses):
        # public attributes
        self.full_name = name
        names_list = name.split(' ')
        self.first_name = names_list[0]
        self.birthday = birthday
        self.courses = courses
        self.attendance = []


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
lucy = Student('Lucy Schwarz', '2010-07-08', {'English', 'Math', 'Dance'})


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
lucy.email = 'lucy@redi-school.org'
print(f'{lucy.first_name} can be contacted at {lucy.email}')
# Lucy can be contacted at lucy@redi-school.org


# But the other instance does not have it.
# print(f'{john.first_name} can be contacted at {john.email}')
# AttributeError: 'Student' object has no attribute 'email'


# New attributes can be added to the Class.
Student.email = 'default@redi-school.org'
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.email}')
# John:default@redi-school.org
# Maria:default@redi-school.org
# Lucy:lucy@redi-school.org


# Changing the class attribute will be visible if the object does not have an
# attribute with the same name
Student.email = 'default@redi.org'
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.email}')
# John:default@redi.org
# Maria:default@redi.org
# Lucy:lucy@redi-school.org


# Changing the attribute for an object doesn't affect the class attribute.
john.email = 'john@redi.org'
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.email}')
# John:john@redi.org
# Maria:default@redi.org
# Lucy:lucy@redi-school.org


# Attributes can be deleted.
del john.email
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.email}')
# John:default@redi.org
# Maria:default@redi.org
# Lucy:lucy@redi-school.org


# So can class attributes.
del Student.email
# for student in [john, mary]:
#     print(f'{student.first_name}:{student.email}')
# AttributeError: 'Student' object has no attribute 'email'


# But it doesn't affect the object
print(f'{lucy.first_name}:{lucy.email}')
