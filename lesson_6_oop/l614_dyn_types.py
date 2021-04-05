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


class Student:
    def __init__(self, name):
        # public attributes
        self.full_name = name


secret_value = Student('John')
print(type(secret_value))
# <class '__main__.Student'>


# abs() works for types like int
abs(42)
abs(True)


# but makes no sense for string or lists
# abs('Hello World!')
# TypeError: bad operand type for abs(): 'str'

# abs([1.414, 1.161, 2.718, 3.141, ])
# TypeError: bad operand type for abs(): 'list'
