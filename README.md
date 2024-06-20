# t1w8-python-errors

### 4 Pillars od OOP (cont..)
- Banking System [banking system code](banking_system.py)

## __repr__method
[repr code](repr.py)
- Special method like __init__ used to define a string representation for an object.
- Particularly used for debugging and development because it can give detailed info about an object. 

## Composition of OOP
[coposition code](composition.py)
- Design principle where a class is composed of one or more objects from other classes.
- It's an alternative to Inheritance and is often times more flexible and modular.
- Avoids Inheritance's pitfall: Changes in base class can unintentionaly affect the derived class, which may break their functionality.
- Composition does not directly affect the composed class, as the class inherits with component classes through well-defined interfaces.

## Error Handling
### Taxonomy of Python Errors:
- Silent Logical Errors - Codes that run perfectly fine, but are logically incorrect.
- Assertion Errors - Raised when 'assert' statement fails. If condition is true,nothing happens, if false raises AssertionError.
- Syntax Errors - Errors in the written syntax that Python interpreter cannot unserstand.
- Exceptions - Runtime error which occurs during program excecution. Python has built-in exception to handle common errors.

## Stack Trace Interpretation
- Text that appears when Python encounters an exception, "stack trace".
- When exceptiom occurs, the interpreter prints a stack trace that shows where the error happened and how the code reached that point.
- Start with: Exception, then the trace

# Try / Except / Finally
- Comprehensive way to handle exceptions.
- Ensures code always runs, regrdless if error occurs.
- 'try' block has code that may raise exception
- 'except' block hascode that handles the exception
- 'finally' block always has the code that should always be executed
