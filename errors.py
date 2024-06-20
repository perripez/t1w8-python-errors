# def is_even(number):
#     return number % 2 == 0

# print(is_even(4))

# # Assertion Errors
# assert 2 + 2 == 4

# # Syntax Errors
# print("Hello World"
      
# -- Exceptions (Runtime errors) --

# Standard Exception
## IndexError: Raised when a sequence subscript is out of range.
my_list = [1, 2, 3]
print(my_list[3])

## KeyError: Raised when a dictionary key is not found
my_dict = {
    'name': 'Rachael'
}
print(my_dict['age'])

## ValueError: Raised when a function reeives an argument of the correct type but inappropriate value
int("abc")

## TypeError: Raised when an operation offunction is applied to  an object of inappropriate type.
len("123")

# Attribute Errors: Raised when an attribute reference or assignment fails
NoneType = None
NoneType.abc

# ZeroDivisionError: Raised when the second operand of a division or modulo operation is 0
print(10/0)

# FileNotFoundError: Raised when trying to fetch a file that does not exist
open('random_file.txt')

# OS Errors: Raised for system-related errors, like "disk full"

# User-defined Exceptions: Users create by subclassung the built-in Exception class
class myCustomError(Exception):
    pass

raise myCustomError("Hey mate! There is an error!")



