'''
1. Importance of DataTypes.
===========================
Data types are used to classify one particular type of data. This is important because the specific 
data type you use will determine what values you can assign to it and what you can do to it (including what operations you can perform on it).


2. Different data types, data structures available in Python
============================================================
Data types are the classification or categorization of data items. It represents the kind of value that 
tells what operations can be performed on a particular data.

>>Numeric type represents the data that has a numeric value. A numeric value can be integer, floating number,
  or even a complex number. These values are defined as int, float, and complex class in Python.
a. Integers - This value is represented by int class. It contains positive or negative whole numbers 
   (without fraction or decimal). In Python, there is no limit to how long an integer value can be.
b. Float - This value is represented by float class. It is a real number with a floating point representation. 
   It is specified by a decimal point. 
c. Complex Numbers - Complex number is represented by a complex class. 

>>Sequence type is the ordered collection of similar or different data types. Sequences allow storing multiple 
  values in an organized and efficient fashion. There are several sequence types in Python 
a. String - are arrays of bytes representing Unicode characters. A string is a collection of one or more characters 
   put in a single quote, double-quote, or triple quote.
b. List - are just like the arrays, declared in other languages which is an ordered collection of data. It is very 
   flexible as the items in a list do not need to be of the same type.
c. Tuple - is also an ordered collection of Python objects. The only difference between tuple and list is that tuples are immutable.

>>Boolean Data type with one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true), 
  and those equal to False are falsy (false). But non-Boolean objects can be evaluated in Boolean context as well and determined to be true or false.

>>Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of 
  elements in a set is undefined though it may consist of various elements. (Set is mutable and thus cannot be used as a 
  key for a dictionary. On the other hand, frozenset is immutable and thus, hashable, and can be used as a dictionary key or as 
  an element of another set.)

>>Dictionary(Mapping type) is an ordered collection of data values, used to store data values like a map, unlike other 
  Data Types that hold only a single value as an element, a dictionary holds key-value pair. 
  Key-value is provided in the dictionary to make it more optimized.

Data structures - Strings, Lists, Tuples, Dictionaries, Sets


3. int vs float
===============
>>Integers - This value is represented by int class. It contains positive or negative whole numbers 
  (without fraction or decimal). In Python, there is no limit to how long an integer value can be.
>>Float - This value is represented by float class. It is a real number with a floating point representation. 
  It is specified by a decimal point. 

4. Boolean. give all scenarios
==============================
>>Greater Than (>)
	The condition turns TRUE if value of left operand is greater than right operand value.
	a>b
>>Less Than (<)
	The condition turns TRUE if value of left operand is lesser than right operand value.
	a<b
>>Equal to (==)
	If the value of left and right operand is same the condition turns TRUE.
	a==b
>>Not equal (!=)
	If values of two operands are not equal then the condition turns TRUE.
	a!=b
>>Greater than or equal to (>=)
	The condition turns TRUE if the left operand value greater than the right operand value.
	a>=b
>>Less than or equal to (<=)
	The condition turns TRUE if the left operand value less than the right operand value.
	a<=b

>> and  -  True if both are True---x and y
>> or   -  True if at least one is True---x or y
>> not  -  True only if False---not x


5. 0 vs null
============
null/none is an object- It says that there is no value.( for none, there is no null value)
0 means that the value itself is 0


6. Explain each data type, data structure with real life examples.


7. CRUD Operations. Give examples for each
==========================================
For any application which is associated with a database, we perform some operations for inserting the record 
[C= Create], reading the records [R=Read], updating the existing record with new value [U=Update] or 
deleting the record from the database [D=Delete]. 


8. Sequences. Types of sequences. Sequence operations
=====================================================
Python supports six different types of sequences. These are strings, lists, tuples, byte sequences, byte arrays, and range objects.
most commonly, lists, tuples, strings and range objects

Operations
----------
    Concatenation
The operator (+) is used to concatenate the second element to the first.
For example - [1,3,4] + [1,1,1] will evaluate to [1,3,4,1,1,1].

    Repeat/Multiplying
The operator (*) is used to repeat a sequence n number of times.
For example - (1,2,3) * 3 will evaluate to (1,2,3,1,2,3,1,2,3).

    Membership Operators and Identity Operators.
Membership operators (in) and (not in) are used to check whether an item is present in the sequence or not. They return True or False.
For example - 'la' in “Manilla” evaluates to True and 'a' not in 'all' evaluates to False.

    Slicing Operator
All the sequences in Python can be sliced. The slicing operator can take out a part of a sequence from the sequence.

For example:
print( "The new york times"[4:10] )
print( (1,2,3,4,5)[1:3] )
Output:
'new yo'
(2,3)

Sequence operations include 
1.  indexing   
2.	slicing    
3.	adding     
4.	multiplying and    
5.	checking for membership.    


9. Explain about below functions and give examples
==================================================
print()----------Prints to the standard output device
id()-------------Returns the id of an object
type()-----------Returns the type of an object
int()------------Returns an integer number
float()----------Returns a floating point number
complex()--------Returns a complex number
bool()-----------Returns the boolean value of the specified object
input()----------Allowing user input
len()------------Returns the length of an object


'''