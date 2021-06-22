# 1.add 2 to every item of a list.
list = [1,2,3,4,5,6,7,8,9,40]
x = []
for i in list:
    x.append(i+2)
print(x)

# 2.pattern
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

# 3.fibonacci series
def Fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    if n<0:
        print("Incorrect Input")
    elif n == 1 or n == 2:
        print('1')
    else :
         while count < n:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
Fibonacci(10)

# 4.armstrong number
num = int(input("Enter a number: "))
sum1 = 0
temp1 = num
while temp1 > 0:
    digit1 = temp1 % 10
    sum1 += digit1**3
    temp1 //= 10
if num == sum1:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


# 5.multiplication table of 9
for i in range(1,11):
    print("9 x ",i,' = ',i*9 )


# 6.check program
i=[0,2,+3,-9,6,+8,-55]
for j in i:
    if j >=0:
        print(j," is positive")
    else :
        print(j,' is negative ')


# 7.convert number of days to age
def find( number_of_days ):
    year = int(number_of_days / 365)
    print(year,'Years ago !')

no_days=798
find(no_days)


# 8.trigonometry using math function
import math
def trigo(n,m):
    if n=='sin':
        return math.sin(m)
    elif n=='cos':
        return math.cos(m)
    elif n=='cosin':
        return math.cosine(m)
    elif n=='tan':
        return math.tan(m)
    elif n=='sec':
        return math.sec(m)
    elif n=='cosec':
        return math.cosec(m)

trigo('sin',30)

trigo('cos',60)

trigo('tan',90)


# 9. calculator using if
def calculator():
    print('+')
    print('-')
    print('*')
    print('/')
    print('%')
    print('**')
    operation = input("Select an operator:n")
    print("Enter two numbers")
    number_1 = int(input())
    number_2 = int(input())

    if operation == '+': # To add two numbers
        print(number_1 + number_2)
    elif operation == '-': # To subtract two numbers
        print(number_1 - number_2)
    elif operation == '*': # To multiply two numbers
        print(number_1 * number_2)
    elif operation == '/': # To divide two numbers
        print(number_1 / number_2)
    elif operation == '%': # To remainder two numbers
        print(number_1 % number_2)
    elif operation == '**': # To num1 exponent num2
        print(number_1 ** number_2)
    else:
        print('Invalid Input')

calculator()


