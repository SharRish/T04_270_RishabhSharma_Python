'''
1. Tell me about Python?
2. Why Python is so popular now a days?
3. Features of Python
=======================================
>>Extensive libraries with powerful functions and methods
>>Is a general-purpose language, therefore, a very wide scope for example data science, machine learning, 
  automation, etc
>>Dynamically typed. We don't declare data. The language automatically recognizes datatype with the 
  value we store in it
>>Is an interpreted language thus no code compilation before use. It executes its statements line-by-line.
>>Here, functions are first-class objects. They can be assigned to variables, returned from other functions, 
  and passed into functions. Therefore the language is object-oriented.
>>Writing python code is quick. Since running is sometimes slow, to counter this, python offers C-based 
  extensions thus clearing bottlenecks and optimizing the code. NumPy package is a good example.

>>Can be used on a server to create web applications.
>>Software development
>>Handle big data and perform mathematical functions
>>Read and modify files

>>Portable: It works on different platforms like windows, Linux, macOS, raspberry pie, etc
>>Easy to use: Has a simple syntax similar to the English language
>>Dynamically typed: The developer does not assign data types to variables at the time of coding. They get automatically assigned.
>>Python runs on an interpreter system thereby executing the code as it is typed. This allows quick prototyping
>>Extensive support of libraries
>>Data structures used in python are user-friendly.


4. Advantages and Disadvantages of Python
=========================================
Advantages
----------
>>Easy to use and learn
>>Simple nature leads to increased productivity
>>Flexible
>>Extensive library
>>Supportive community

Disadvantages
-------------
>>Speed, slower than Java or C-based
>>High memory consumption
>>Fragile for mobile developement
>>Runtime errors as language is dynamically typed


5. Interpreted vs Compiled time programming languages. Explain in detail
========================================================================
>>A compiled language is converted into machine code so that the processor can execute it whereas an 
  interpreted language is a programming language which are generally interpreted, without compiling 
  a program into machine instructions.
>>The compiled programs run faster than interpreted programs.(vice-versa)
>>Types of Compiled language - C, C++, COBOL, and Types of Interpreted language - JavaScript, Perl, Python


6. .py vs .pyc files
====================
>>.py is python source code files. 
>>.pyc contains the byte code of the python files. These are created when a code is imported from some other source.

>>Before the execution of a program, the interpreter checks for compiled files. If the file is present, the 
  virtual machine will execute it. Otherwise, it searches for a .py file, converts it into a .pyc file, and 
  then the virtual machine runs it.
  
>>Having .pyc files saves us time spent in compilation


7. How compilation will happen internally. Explain in detail
============================================================
>>The python compiler will read the source code and verify if it is correctly formatted by checking 
  the syntax of each line. ErrorMessage shows if it spots an error.
>>If there is no error, the compiler will translate it into a byte code.
>>This byte code is then sent to the Python Virtual Machine(PVM) which is an interpreter and here 
  the byte code is converted into machine-executable code.


8. Why Python is Dynamically typed programming Language. Explain
================================================================
Python is a dynamically typed language. What is dynamic? You don't need to declare the variable type or manage 
memory when assigning values to variables in Python. Languages such as C, C++, and Java require you to declare the 
type of a variable before assigning it a value. Python doesn't care if you don't declare the type of your variables. 
>>Indicates the run-time nature of the variable in the program. 
>>Python also does important memory management when programming. 


9. Python is Platform independent. Explain
==========================================
Once we write a Python program, it can run on virtually all operating systems and platforms without having to be 
re-written again.
Python uses PVM to convert python code to machine understandable code.

'''