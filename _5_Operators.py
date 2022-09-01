'''
1. Explain in detail about all operators
========================================
It is defined as the symbol that is responsible for a particular operation between two operands.
>>Arithmetic operators 
	+ Addition, - subtraction, * multiplication, / division, % modulus, // floor division, ** exponential

x = 15
y = 4

print('Sum of given integers:', x+y)
print('Subtraction of given integers:', x-y)
print('Multiplication of given integers:', x*y)
print('Division of given integers:', x/y)
print('Flooor division of given integers:', x//y)
print('Exponential of given integers:', x**y)

>>Assignment operators
	= is x=5,  += is x=x+5,  -= is x=x-5,  *= is x=x*5,  /= is x=x/5,  %= is x=x%5,  
		//=,  **=,  &=,  |=,  ^=,  <<=,   >>=
  
a = 10
  
# To assign values
b = a
print("Post value assignment:", b)
  
# To add and assign value
b += a
print("Post addition and assignment:", b)
  
# To subtract and assign value
b -= a
print("Post subtraction and assignment:", b)
  
# To multiply and assign
b *= a
print("Post multiplication and assignment:", b)


>>Comparison/relational operators
	== is equals,  != is not equal,  > is greater than,  < is lesser than,  >= is greater than or equal to,  <= is lesser than or equal to
 
a = 13
b = 33

print("Is a greater than b:", a > b)
print("Is a lesser than b:", a < b)
print("Is a equal to b:", a == b)
  
	# a != b is True
print(a != b) 
	# a >= b is False
print(a >= b) 
	# a <= b is True
print(a <= b)

>>Logical operators
	'and' returns True if both values are are true, 'or'  returns True if one statement is true, 'not' will reverse the result

a = True
b = False
print(a and b)
print(a or b)
print(not a)

>>Boolean Operators
	True and False.
 
>>Identity operators
	'is' returns True if both variables are the same object,  'is not' returns True if both variables are not the same object
a = 10
b = 20
c = a
  
print(a is not b)
print(a is c)

>>Bitwise operators
	These are used to compare binary numbers
		& - AND - Sets each bit to 1 if both bits are 1
		| - OR - Sets each bit to 1 if one of two bits is 1
		^ - XOR - Sets each bit to 1 if only one of two bits is 1
		~ - NOT - Inverts all the bits
		<< - Zero fill left shift - Shift left by pushing zeros in from the right and let the leftmost bits fall off
		>> - Signed right shift - Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
a = 10
b = 4
  
print("Bitwise AND operation:", a&b)
print("Bitwise OR operation:", a|b)
print("Bitwise NOT operation:", ~a)
print("Bitwise XOR operation:", a^b)
print("Bitwise right shift operation:", a >> 2)
print("Bitwise right shift operation:", a << 2)

>>Membership Operators
    Membership operators (in) and (not in) are used to check whether an item is present in the sequence or not. They return True or False.
    For example - 'la' in "Manilla" evaluates to True and 'a' not in 'all' evaluates to False.

x = 24
y = 20
list = [10, 20, 30, 40, 50]
  
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
  
if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


2.  == vs is 
============
'==' is for value equality, to check if two objects have the same value.
'is' is for reference quality, to check if they point to the same object.


3. and & or operators. Explain 2 examples 
=======================================
and     True if both the operands are true---x and y
or      True if either of the operands is true---x or y
	x = 5
print(x > 3 and x < 10) returns True because 5 is greater than 3 AND 5 is less than 10
	x = 5
print(x > 3 or x < 4) returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)


4. Operator precedence.
=======================
P - Parentheses is the highest precedence
E - Exponentiation
M - Multiplication     (Multiplication and division have the same precedence)
D - Division
A - Addition           (Addition and subtraction have the same precedence)
S - Subtraction
:=  is the lowest precedence.

5. Subtract 2 numbers and print result program.
	- Write down all scenarios with different input values 


'''
