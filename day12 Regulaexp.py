# program for all the cases which can check a string

import re
matcher = re.finditer("[a-zA-Z0-9]","GopalReddy123")
for match in matcher:
    print(match.start(),"...",match.group())
    
print("\n")

# program that matches a word containing 'ab'.

matcher = re.finditer("ab","abaabaaabaaaab")
for match in matcher:
    print(match.start(),"...",match.end(),"...",match.group())
print()


# program to check for a number at the end of a word/sentence

def end_num(string):
    text= re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False
print(end_num("abcdef"))
print(end_num("abcef3"))

print()


# program to search the numbers (0-9) of length between 1 to 3 in a given string

results =re.finditer("([0-9]{1,3})","exercises number 1,12,13,and 345 are important")
print("number of lenth 1to3")
for n in results:
    print(n.group())
print("\n")

# program to match a string that contains only uppercase letters

matcher =re.finditer("[A-Z]","AbCDEfGH")
for match in matcher:
    print(match.start(),"...",match.group())
