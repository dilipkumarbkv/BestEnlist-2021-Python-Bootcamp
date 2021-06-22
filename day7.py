# 1.Python script to merge
def Merge(dict1, dict2):
    return (dict2.update(dict1))

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(Merge(dict1, dict2))

# changes made in dict2
print("merged dict is:",dict2)

# 2.List to set and in descending order

a = [252, 224, 23, 3, 5, 74, 34, 53, 435]
x = sorted(a, reverse = True)
print("The sorted list:", x)
y = set(x)
print("The set is:", y)

# 3. List number of items in a dictionary.

dic1={'x': [82, 87, 21, 23], 'y': [77, 99, 24, 32], 'z': [43, 67, 27, 8], 'w':[22, 889, 25, 4]}
result={a:sorted(dic1[a]) for a in sorted(dic1)}
print(result)

def f1(dic1):
    res = dict()
    for key in sorted(dic1):
        res[key] = sorted(dic1[key])
    return res

f1(dic1)

def f2(dic1):
    res = dict()
    min1 = dic1[key]
    for key in sorted(dic1):
        if dic1[key] < min1:
            min1 = dic1[key]
            res[key] = min1
    return res

f1(dic1)

# 4. Input string from user

def str():
    user = input("Enter the string :")
    word = "String given by user! "
    return user + word[6:]

str()

def str1():
    user = input("Enter the string :")
    word = "String is given by user  "
    return word.replace('String', user)

str1()

# 5. capitalise first character

def c():
    user=input("Enter the string :")
    return user.capitalize()

c()

def change_char(str1):
    char = str1[0]
    str1 = str1.replace(char, str1[0].upper())
    str1 = char + str1[1:]
    return str1
change_char('hello world ! this is a python program')


# 6.find repeated lists
from collections import Counter

L1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
d = Counter(L1)
print(d)

new_list = list([item for item in d if d[item] > 1])
print(new_list)

def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))

# 7.check sum of three elements
a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
sum=a+b+c
print("Sum is: ",sum)
user=int(input("Enter the number to divide sum!"))
if sum% user==0:
    print("The given input divide")
else :
    print("The given input does not divide sum1")

# 8.mean median and mode
given_numbers = [1,2,2]
addition = 0
for i in given_numbers:
    addition = addition +i
print("addition",addition)
length = len(given_numbers)
mean = addition/length
print("mean :",mean)

given_numbers.sort()
if length%2==0:
    median1 = given_numbers[length//2]
    median2=given_numbers[length//2-1]
    median = (median1+median2)/2
else:
    median = given_numbers[length//2]
print("median is:",median)
import statistics
mode1=statistics.mode(given_numbers)
print("mode is :",mode1)

# 9.swap cases
a="dilip"
b="Hello world"
tep=a
a=b
b=tep
print(a,b)
x = a
y = b
x, y = y, x
print(x,y)


# 10.integer to binary and octa
def decToOctal(n):
    octalNum = [0] * 100
    i = 0
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        print(octalNum[j], end="")

n=25
decToOctal(n)

n=12
decToOctal(n)






