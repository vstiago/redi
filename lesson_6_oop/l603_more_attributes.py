# Attributes in different classes are isolated, changing one class does not
# affected the other, the same way that changing an object does not modify
# another.


email = 'contact@redi-school.org'


class Student:
    email = 'student@redi-school.org'

    def __init__(self, name, birthday, courses):
        # class public attributes
        self.full_name = name
        self.first_name = name.split(' ')[0]
        self.birthday = birthday
        self.courses = courses
        self.attendance = []


class Teacher:
    email = 'teacher@redi-school.org'

    def __init__(self, name):
        # class public attributes
        self.full_name = name


print('email:', email)
# email: contact@redi-school.org

print('Student.email:', Student.email)
# Student.email: student@redi-school.org

print('Teacher.email:', Teacher.email)
# Teacher.email: teacher@redi-school.org


# Objects
john = Student('John Schneider', '2010-04-05', ['German', 'Arts', 'History'])
tiago = Teacher('Tiago Vieira')

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
