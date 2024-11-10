# Functions:
# types of functions
# 1. built-in function (those who already defined)
# 2. user defined function (those which we make by ourself)

#built-in function:

list = [1,2,3,4]
print(sum(list)) # it's a built-in function

# write code again and again:

user_input = int(input("write any number"))

if user_input % 2 == 0:
    print("Even number")
else:
    print("Odd number")  # if we want to write code again and again so we use function instead of repetition

# simple function:

def fun():
    print("welcome to GFG")

fun()
fun()
fun()
fun()


# with parameters: (with variables)

def even_odd(user_input):
    if user_input % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

even_odd(user_input)

# with parameter and arguments:

def add(a,b):
    print(a + b)

add(3,4)

# print function (function me hmesha return use hta hy bcz print piche ziada memory use krta hy backend pe tbi)
# return function: (iske baad wala code nh chlta wahin pr code return kr deta hy or is me print likh k funcntion call krna hy)

# return function


def add1(a,b):
    z = a + b
    return z

print(add1(3,4))

# return and print both in function


def add1(a,b):
    z = a + b
    print(z)
    z += 1
    return z

ans = add1(3,4)
print(ans)


# default parameter:

def add2(a, b = 2):
    z = a + b
    return z

print(add2(3))

def add2(a, b = 2):
    z = a + b
    return z

num1 = int(input("number 1: "))
num2 = int(input("number 2: "))

print(add2(num1, num2))

# positional parameter: 

def intro(name, age):
    print(f"My name is: {name}, and my age is: {age}")

intro("Fariha", 24)

# keyword parameters:

def intro1(name, age, qualification, city, grade, degree):
    print(f"My name is {name} and my age is: {age} and qualification is: {qualification} and my city is: {city} and my grade is: {grade} and my degree is: {degree}")

# intro("Fariha", 24, "inter", "karachi", "B", "inter")

intro1(city = "Karachi", grade= "B", name = "Fariha", age = 24, degree = "inter", qualification= "inter")

# Arbitrary argument: (unlimited)

def add5(*a):
    return sum(a)

print(add5(1))
print(add5(1,4,6))
print(add5(1,4,3,2,124,56,5))

# Arbitrary keyword argument: (unlimited)

def add6(**a):
    return sum(a.values())

print(add6(num1 = 1, num2 = 4, num3 = 6))
print(add6(num1 = 1, num2 = 4, num3 = 3, num4 = 2, num5 = 124, num6 = 56, num7 = 5))

# arbitrary argument and non-keyword argument both are same
# arbitrary argument hmen tuple return krta hy
# keyword argument hmen dictionary return krta hy

# keyword argument:
def add7(**a):
    for x, y  in a.items():
        print(f"{x} = {y}")

add7(num1 = 1, num2 = 4, num3 = 3, num4 = 2, num5 = 124, num6 = 56, num7 = 5)

# anonymus function: (lambda function) it has no name

add = lambda x, y : x + y
print(add(2, 2))

mul = lambda x : x**2
print(mul(3))

# docstring: function k andr comments dalna or hm isey print b krwa skte hen

def even_odd1(user_input):
    """ This Function is used to update weather number is even or odd..."""
    if user_input % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

even_odd1(user_input)
print(even_odd1.__doc__)

print(print.__doc__)

# practice:
# reverse string
# count vowels


reverse_input = input("kindly write any word for reverse function. ")
def reverse_string(reverse_input):
    return reverse_input[::-1]

output = reverse_string(reverse_input)
print(output)

vowel = "aeiouAEIOU"

vowel_input = input("kindly write any word for vowel search function. ")
def vowel_string(vowel_input):
    for char in vowel_input:
        if char in vowel:
            print(f"Vowel found: {char}")



vowel_string(vowel_input)