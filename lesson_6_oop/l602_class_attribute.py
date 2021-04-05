class Student:
    email = 'default@redi-school.org'

    def __init__(self, name, birthday, courses):
        # class public attributes
        self.full_name = name
        self.first_name = name.split(' ')[0]
        self.birthday = birthday
        self.courses = courses
        self.attendance = []


# Objects
john = Student('John Schneider', '2010-04-05', ['German', 'Arts', 'History'])
mary = Student('Mary von Neumann', '2010-05-06',
               ['German', 'Math', 'Geography', 'Science'])
lucy = Student('Lucy Schwarz', '2010-07-08', ['English', 'Math', 'Dance'])


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
john.email = 'john@redi.org'
for student in [john, mary, lucy]:
    print(f'{student.first_name}:{student.email}')
# John:john@redi.org
# Maria:default@redi.org
# Lucy:lucy@redi-school.org
