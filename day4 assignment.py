Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Create a list with 'n' intergers
>>> A = [1,2,3,5,7,8]
>>> 
>>> # add item into the list
>>> 
>>> A.append(9)
>>> print(A)
[1, 2, 3, 5, 7, 8, 9]
>>> # item added to list
>>> 
>>> delete item using del fucntion
SyntaxError: invalid syntax
>>> # delete item using 'del' fucntion
>>> 
>>> del(A[4])
>>> print(A)
[1, 2, 3, 5, 8, 9]
>>> del(A[2])
>>> print(A)
[1, 2, 5, 8, 9]
>>> # item deleted successfully
>>> 
>>> # store largest number of a list to a variable
>>> 
>>> high = max(A)
>>> print(high)
9
>>> # we have got the largest number from the list A
>>> 
>>> # store lowest number of a list to a variable
>>> 
>>> lo = min(A)
>>> print(lo)
1
>>> # we have got the lowest number fron the list
>>> 
>>> 
>>> # create a tuple
>>> 
>>> T = (1,2,3,4,5,6)
>>> U = reversed.T()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    U = reversed.T()
AttributeError: type object 'reversed' has no attribute 'T'
>>> u = reversedT()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    u = reversedT()
NameError: name 'reversedT' is not defined
>>> u = reversed(T)
>>> print(T)
(1, 2, 3, 4, 5, 6)
>>> print(u)
<reversed object at 0x03B0BB38>
>>> print(tuple(T))
(1, 2, 3, 4, 5, 6)
>>> print(tuple(u))
(6, 5, 4, 3, 2, 1)
>>> # reversed tuple successfully
>>> 
>>> # create tuple and convert it to list
>>> 
>>> A = (132, "demo", 3.25)
>>> B = list(A)
>>> print(B)
[132, 'demo', 3.25]
>>> 
>>> 
>>> # converted into list successfully