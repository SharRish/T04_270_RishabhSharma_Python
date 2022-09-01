'''
1. x = 10. Explain in detail for CRUD operations
================================================
Create 
    x = 10. This creates a variable x with value 10.
Retrieve
    return x or print(x). This returns value of x.
Update
    x = 20. This updates the value of the variable x from 10 to 20
Delete
    del x. This deletes the instance x
    
    
2. tokens in Python. Explain all types
======================================
A token is the smallest individual unit in a python program. All statements and instructions in a program are 
built with tokens. The various tokens in python are :

>>1. Keywords: Keywords are words that have some special meaning or significance in a programming language. They can't be used as variable names, function names, or any other random purpose. 
     They are used for their special features. In Python we have 33 keywords some of them are: 
     try, False, True, class, break, continue, and, as, assert, while, for, in, raise, except, or, not, if, elif, print, import, etc.
 
>>2. Identifiers: Identifiers are the names given to any variable, function, class, list, methods, etc. for their identification.
 
>>3. Literals or Values: Literals are the fixed values or data items used in a source code. Python supports different types of literals such as:
(i)    String Literals: The text written in single, double, or triple quotes represents the string literals in Python. For example: “Computer Science”, 'sam', etc.
(ii)   Character Literals: Character literal is also a string literal type in which the character is enclosed in single or double-quotes. a = 'G', b = "W"
(iii)  Numeric Literals: These are the literals written in form of numbers. Python supports the following numerical literals:
       >>>Integer Literal: It includes both positive and negative numbers along with 0. It doesn't include fractional parts. It can also include binary, decimal, octal, hexadecimal literal.
       >>>Float Literal: It includes both positive and negative real numbers. It also includes fractional parts.
       >>>Complex Literal: It includes a+bi numeral, here a represents the real part and b represents the complex part.
(iv)   Boolean Literals: Boolean literals have only two values in Python. These are True and False.
(v)    Special Literals: Python has a special literal 'None'. It is used to denote nothing, no values, or the absence of value.
(vi)   Literals Collections: Literals collections in python includes list, tuple, dictionary, and sets.

>>4. Operators: These are the tokens responsible to perform an operation in an expression. The variables on which operation is applied are called operands. 


3. Garbage collection. How it works internally
4. Memory Management in Python
==============================================
>>Memory management in Python involves a private heap containing all Python objects and data structures. 
The management of this private heap is ensured internally by the Python memory manager.
At the lowest level, a raw memory allocator ensures that there is enough room in the private heap for storing 
all Python-related data by interacting with the memory manager of the operating system. On top of the 
raw memory allocator, several object-specific allocators operate on the same heap and implement actions 
that are defined for every object type.

>>Python deletes unwanted objects (built-in types or class instances) automatically to free the memory space. 
The process by which Python periodically frees and reclaims blocks of memory that no longer are in use is called Garbage Collection.
Python's garbage collector runs during program execution and is triggered when an object's reference count reaches zero. 
An object's reference count changes as the number of aliases that point to it changes.


5. Dynamically typed programming. Explain examples.
===================================================
Python is a dynamically typed language. What is dynamic? You don't need to declare the variable type or manage 
memory when assigning values to variables in Python. Languages such as C, C++, and Java require you to declare 
the type of a variable  before assigning it a value. Python doesnt care if you dont declare the type of your variables.
>>Indicates the run-time nature of the variable in  the program. 
>>Python also does important memory management when programming.  
Python is therefore a dynamically typed language.


6. Initializing variable in static, dynamic way
============================================
>>Static typing:
means that the types are known and checked for correctness before running your program. This is often done by the language compiler.
int number = 1
string name = "joe"
string output = string(number)+name // =1joe
>>Dynamic typing:
Means that types are only known as your program is running
number = 1
name = "joe"
output = number + name// = 1joe

Python supports initialising varibles in the dynamic way as it is a dynamically typed lamguage
 
 
7. Assigning value to multiple variables. Explain
=================================================
Python allows you to assign values to multiple variables in one line:
Example: x, y, z = "Orange", "Banana", "Cherry"
And you can assign the same value to multiple variables in one line:
Example: x = y = z = "Orange"



'''