Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (In
tel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # Day3 Exercise
>>> # Creating three variables a,b,c with same value
>>>
>>> a=b=c=30
>>> # Divide a by 10
>>>
>>> Print(a/10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print(a/10)
3.0
>>>
>>> # Multiply b by 50
>>>
>>> print(b*50)
1500
>>>
>>> # Add c value by 60
>>>
>>> print(c+60)
90
>>>
>>> # Replace string of 5 character length by 3rd character with "G"
>>>
>>> Name="Dilip"
>>> x = Name.replace("l","G",2)
>>> print(x)
DiGip
>>>
>>>
>>> # Create variables int, float and convert them int to float and viceversa
>>>
>>> a,b = 12,24.30
>>> print(float(a))
12.0
>>> print(int(b))
24