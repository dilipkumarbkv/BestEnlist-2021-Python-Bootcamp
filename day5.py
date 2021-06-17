#Merging 2 dictionaries:

def merge( dict1, dict2 ):
    return (dict2.update (dict1) )


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(merge(dict1, dict2))

print(dict2)


#Remove a key from dictionary.

myDict = {'a':1,'b':2,'c':3,'d':4}

print(myDict)

if 'a' in myDict:
    del myDict['a']

print(myDict)

#Mapping 2 lists in a dictionary

keys = ['yellow', 'red', 'green', 'blue']

values = [1,2,3,4]

color_dictionary = dict(zip(keys, values))

print(color_dictionary)


#Find the length of set.


set1 = set()


set1.add(8)
set1.add(9)
set1.add((6, 7))

print("The length of set is:", len(set1))

#Remove the intersection of a 2nd set from the 1st set

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print("Original sets:")
print(s1)
print(s2)

print("\nRemove the intersection of a 2nd set from the 1st set:")

for i in s1&s2:
    s1.remove(i)

print("s1: ", s1)
print("s2: ", s2)

