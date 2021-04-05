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

abs(42)
# abs('Hello World!')
# TypeError: bad operand type for abs(): 'str'
abs(True)
# abs([1.414, 1.161, 2.718, 3.141, ])
# TypeError: bad operand type for abs(): 'list'
