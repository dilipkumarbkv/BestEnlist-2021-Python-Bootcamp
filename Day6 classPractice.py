Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> defmyFun(num): 
  		 num[0] =20
  
list =[1, 2, 3, 4, 5]  
myFun(list)
print(list)#list will be changed after the function call

SyntaxError: invalid syntax
>>> defmyFun(num): 
  		 num[0] =20
  

SyntaxError: invalid syntax
>>> defmyfunc(num):
	
SyntaxError: invalid syntax
>>> def myfunc(num):
	num[0] = 20

	
>>> list =[1, 2, 3, 4, 5]  

>>> myfunc(list)
>>> print(list)
[20, 2, 3, 4, 5]
>>> def myfunc():
	print("print enter my num")

	
>>> myfunc()
print enter my num
>>> def csk(fname):
	print("enter player name:" + fname)

	
>>> csk("Dhoni")
enter player name:Dhoni
>>> csk("Raina")
enter player name:Raina
>>> def ipl(csk_cap,rcb_cap):
	print(csk_cap + "Vs" +rcb_cap)

	
>>> ipl("Dhoni", "Kholi")
DhoniVsKholi
>>> def myteam(*team)
SyntaxError: invalid syntax
>>> def myfunc(*team)
SyntaxError: invalid syntax
>>> def myfunc(*team):
	print("enter the younger player name" + team[0])

	
>>> myfunc("tom", "sam", "Ram")
enter the younger player nametom
>>> def mychildren(child1, child2, child3):
	print("The elder child name is: " + child1)
	print("The younger child name is: " +child3)

	
>>> mychildren(child1 = "Ram", child2 = "Laxman", child3 = "Bharat")
The elder child name is: Ram
The younger child name is: Bharat
>>> def myplayers(**players):
	print("The player lastname is :" +lname)
	print("The player firstname is :" +fname)
	print("The player name is:" +name)

	
>>> myplayers(fname = "Reddy", lname = "Ram", name = "Shri Ram", name = "Hanuman")
SyntaxError: keyword argument repeated
>>> myplayers(fname = "Reddy", lname = "Ram", name = ("Shri Ram", "Sita", "Hanuman"))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    myplayers(fname = "Reddy", lname = "Ram", name = ("Shri Ram", "Sita", "Hanuman"))
  File "<pyshell#38>", line 2, in myplayers
    print("The player lastname is :" +lname)
NameError: name 'lname' is not defined
>>> def myplayers(**players):
	print("The player lastname is :" players["+lname"]
	print("The player firstname is :" players["+fname"]
	print("The player name is:" players["+name"]
	      
SyntaxError: invalid syntax
>>> def myplayers(**players):
	print("The player lastname is :" +lname)
	print("The player firstname is :" +fname)
	print("The player name is:" +name)

	
>>> myplayers(name = "Ram", fname = "laxman", lname = "sita")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    myplayers(name = "Ram", fname = "laxman", lname = "sita")
  File "<pyshell#43>", line 2, in myplayers
    print("The player lastname is :" +lname)
NameError: name 'lname' is not defined
>>> myplayers(name = "Ram", fname = "laxman")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    myplayers(name = "Ram", fname = "laxman")
  File "<pyshell#43>", line 2, in myplayers
    print("The player lastname is :" +lname)
NameError: name 'lname' is not defined
>>> def myplayers(**players):
	print("The player lastname is :" players["+lname"]
	print("The player firstname is :" players["+fname"]

	
SyntaxError: invalid syntax
>>> def myplayers(**players):
	print("The player lastname is :" players["+lname"]
	print("The player firstname is :" players["+fname"]
	print("The player name is:" players["+name"]
	      

SyntaxError: invalid syntax
>>> def myplayers(**players):
	print("The player lastname is :" +lname)
	print("The player firstname is :" +fname)
	print("The player name is:" +name)


>>> myplayers(fname = "Ram", lname = "sita")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    myplayers(fname = "Ram", lname = "sita")
  File "<pyshell#48>", line 2, in myplayers
    print("The player lastname is :" +lname)
NameError: name 'lname' is not defined
>>> def myplayers(**players):
	print("The player lastname is :" players["lname"]
	print("The player firstname is :" players["fname"]
	print("The player name is:" players["name"]
	      
SyntaxError: invalid syntax
>>> def myplayers(**players):
	print("The player lastname is :" + players["lname"]
	print("The player firstname is :" + players["fname"]
	print("The player name is:" + players["name"]
	      
SyntaxError: invalid syntax
>>> def myplayers(**players):
	print("The player lastname is :" + players["lname"]
	print("The player firstname is :" + players["fname"]

	
SyntaxError: invalid syntax
>>> def myplayers(**players):
	
	print("The player lastname is :" + players["lname"])
	print("The player firstname is :" + players["fname"])
	print("The name of the player is:" + players["name"])

	
>>> myplayers(fname = "Ram", lname= "sita", name = "hanuma")
The player lastname is :sita
The player firstname is :Ram
The name of the player is:hanuma
>>> def myfunc(x):
	return5 * x

	
>>> print(myfunc(5))
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print(myfunc(5))
  File "<pyshell#85>", line 2, in myfunc
    return5 * x
NameError: name 'return5' is not defined
>>> def myfunc(x):
	return 5 * x

>>> print(myfunc(5))
25
>>> print(myfunc(9))
45
>>> def csk(fname = "Dhoni")
SyntaxError: invalid syntax
>>> def csk(fname = "Dhoni"):
	print("captain of csk is:" + fname)

	
>>> csk()
captain of csk is:Dhoni
>>> 