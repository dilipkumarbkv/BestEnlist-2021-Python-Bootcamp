Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A = [1,2,3,4]
>>> B = [a,b,c,d]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    B = [a,b,c,d]
NameError: name 'a' is not defined
>>> B = ['a', 'b', 'c', 'd']
>>> A.append(10)
>>> B.append(k)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    B.append(k)
NameError: name 'k' is not defined
>>> B.append('j')
>>> print(A)
[1, 2, 3, 4, 10]
>>> print(B)
['a', 'b', 'c', 'd', 'j']
>>> A.extend(B)
>>> print(A)
[1, 2, 3, 4, 10, 'a', 'b', 'c', 'd', 'j']
>>> print(B)
['a', 'b', 'c', 'd', 'j']
>>> A.insert(6,6)
>>> print(A)
[1, 2, 3, 4, 10, 'a', 6, 'b', 'c', 'd', 'j']
>>> A.insert(4,9)
>>> print(A)
[1, 2, 3, 4, 9, 10, 'a', 6, 'b', 'c', 'd', 'j']
>>> del(A[1])
>>> print(A)
[1, 3, 4, 9, 10, 'a', 6, 'b', 'c', 'd', 'j']
>>> del(A[4])
>>> print(A)
[1, 3, 4, 9, 'a', 6, 'b', 'c', 'd', 'j']
>>> del(A[9:J])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    del(A[9:J])
NameError: name 'J' is not defined
>>> del(A[9:j])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    del(A[9:j])
NameError: name 'j' is not defined
>>> del(A[9:'j'])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    del(A[9:'j'])
TypeError: slice indices must be integers or None or have an __index__ method
>>> print(A)
[1, 3, 4, 9, 'a', 6, 'b', 'c', 'd', 'j']
>>> del(A[5:9])
>>> print(A)
[1, 3, 4, 9, 'a', 'j']
>>> x = A.pop()
>>> print(x)
j
>>> print(A)
[1, 3, 4, 9, 'a']
>>> x = A.pop(3)
>>> print(x)
9
>>> A.append(9)
>>> print(A)
[1, 3, 4, 'a', 9]
>>> A.remoove('a')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    A.remoove('a')
AttributeError: 'list' object has no attribute 'remoove'
>>> A.remove('a')
>>> print(A)
[1, 3, 4, 9]
>>> lo = min(A)
>>> print(lo)
1
>>> hig = max(A)
>>> print(hig)
9
>>> A.sort()
>>> print(A)
[1, 3, 4, 9]
>>> A.append(6)
>>> print(A)
[1, 3, 4, 9, 6]
>>> A.sort()
>>> print(A)
[1, 3, 4, 6, 9]
>>> A.append(5)
>>> print(A)
[1, 3, 4, 6, 9, 5]
>>> out.sorted(A)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    out.sorted(A)
NameError: name 'out' is not defined
>>> out = sorted(A)
>>> print(A)
[1, 3, 4, 6, 9, 5]
>>> print(out)
[1, 3, 4, 5, 6, 9]
>>> 
>>> 
>>> 
>>> # Tuples
>>> my_tuple=(1,2,3,4,5)
>>> print(my_tuple)
(1, 2, 3, 4, 5)
>>> my_tuple1 = (1, "hello", 'z', 3.14)
>>> print(my_tuple1)
(1, 'hello', 'z', 3.14)
>>> print(my_tuple1[0])
1
>>> print(my_tuple1[1])
hello
>>> 
>>> 
>>> 
>>> # Excercise
>>> 
>>> 