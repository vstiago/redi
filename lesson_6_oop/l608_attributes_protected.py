class Student:
    def __init__(self, name, birthday, courses):
        # public attributes
        self.full_name = name
        self.first_name = name.split(' ')[0]
        self.birthday = birthday
        self.courses = courses

        # protected attributes
        # starts with '_'
        # Can be configured as a warning if accessed outside the class, but the
        # program will run.
        self._grades = dict([(course, 0.0) for course in courses])

    # class public methods
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
    def grades(self):
        return str(self._grades)


# Objects
john = Student('John Schneider', '2010-04-05', {'German', 'Arts', 'History'})
mary = Student('Mary von Neumann', '2010-05-06',
               {'German', 'Math', 'Geography', 'Science'})
lucy = Student('Lucy Schwarz', '2010-07-08', {'English', 'Math', 'Dance'})

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


# Don't access the protected attribute directly, but receives the string created
# from it.
print('Lucy grades:', lucy.grades())
# Lucy grades: {'English': 8.3, 'Dance': 6.7, 'Math': 9.4}
