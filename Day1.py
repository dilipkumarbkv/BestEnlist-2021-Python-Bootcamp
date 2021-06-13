C:\Users\DILIP-PC\PycharmProjects\BootCampDay1.py\venv\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.1\plugins\python-ce\helpers\pydev\pydevconsole.py" --mode=client --port=55189
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\DILIP-PC\\PycharmProjects\\BootCampDay1.py', 'C:/Users/DILIP-PC/PycharmProjects/BootCampDay1.py'])
PyDev console: starting.
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
print("30 days 30 hour challenge") print('30 days 30 hour challenge')
  File "<input>", line 1
    print("30 days 30 hour challenge") print('30 days 30 hour challenge')
                                       ^
SyntaxError: invalid syntax
print("30 days 30 hour challenge") print('30 days 30 hour challenge')
  File "<input>", line 1
    print("30 days 30 hour challenge") print('30 days 30 hour challenge')
                                       ^
SyntaxError: invalid syntax
print('30 days 30 hour challenge')
30 days 30 hour challenge
print("30 days 30 hour challenge")
30 days 30 hour challenge
print('"30 days 30 hour challenge"')
"30 days 30 hour challenge"
print("'30 days 30 hour challenge'")
'30 days 30 hour challenge'
print("'30 days 30 hour challenge")
'30 days 30 hour challenge
#Assigning string to variable
Hours = "thirty" print(Hours)
  File "<input>", line 1
    Hours = "thirty" print(Hours)
                     ^
SyntaxError: invalid syntax
Hours = "thirty" 
print(Hours)
thirty
#Indexing using string
Days="Thirty in a month"
print(Days[6])
 
#Output is blank because 6 is occupied by space 
Days="Thirty in a month"
print(Days[8])
n
#print the particular character from certain text:
Challenge= "I will win"
print(Challenge[2:4])
wi
print(Challenge[7:10])
win
print(Challenge[1:])
 will win
print(Challenge[1:1])
print(Challenge[1:2])
 
print(Challenge[1:3])
 w
print(Challenge[1:5])
 wil
print(Challenge[2:5])
wil
print(Challenge[3:5])
il
#Print the length of Character:
Challenge= "I will win"
Challenge= "I will win"
print(len(Challenge))
10
#Convert String into lower character:
Challenge= "World is beautiful"
print(Challenge.lower())
world is beautiful
#convert string into upper case character:
Challenge= "World is beautiful"
print(Challenge.upper())
WORLD IS BEAUTIFUL
#String Concatenation – Joining two strings:
a="Stay safe"
b=" Use mask"
c=a+b
print(c)
Stay safe Use mask
a="Stay safe"
b=" Use mask"
print(a + "" +b)
Stay safe Use mask
#casefold() - Usage
text = "Thirty days and Thirty hours"
x = text.casefold()
print(x)
thirty days and thirty hours
#DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU.
text ="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
x=text.lowercase()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'str' object has no attribute 'lowercase'
x=text.islower()
print(x)
False
x=text.find()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: find() takes at least 1 argument (0 given)
text ="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
x=text.find()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: find() takes at least 1 argument (0 given)
x=text.find(T)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'T' is not defined
text ="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
x=text.find(T)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'T' is not defined
text ="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
x=text.capitalize()
print(x)
Don’t trouble trouble until trouble troubles you.
text ="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
x=text.find()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: find() takes at least 1 argument (0 given)
text ="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
x=text.find("trouble")
print(x)
-1
text ="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
x=text.find("TROUBLE")
print(x)
6
#-1 represents that it has not found an exact match
#any number displayed means that match is found at location 
text ="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
x=text.isaplha()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'str' object has no attribute 'isaplha'
text ="DON’T TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU."
x=text.isalpha()
print(x)
False
text ="DON’T TROUBLE TROUBLE"
x= text.isalpha()
print(x)
False
text ="DON’T"
x= text.isalpha()
print(x)
False
text ="DONT TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
x= text.isalpha()
print(x)
False
text ="PYTHON"
x= text.isalpha()
print(x)
True
text ="BOOTCAMP"
x= text.isalpha()
print(x)
True
# on using isaplha() if the statement has any other characters or symbols or spaces it will not consider as alphabet. 
text ="DONT TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
x= text.isnum()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'str' object has no attribute 'isnum'
text ="DONT TROUBLE TROUBLE UNTIL TROUBLE TROUBLES YOU"
x= text.isalnum()
print(x)
False
text ="BOOTCAMP9"
x= text.isalnum()
print(x)
True
