print("Fariha")
#Variable:
name: str = "Fariha"
NAME: str = "Fariha"

# Escape sequence:

print("""someone said \n\t\t"ali\" is a 'good' boy \n\tbut \nhe often make mistakes """)

# f-string:

name:str = "Fariha Asif"
age:int = 24
email:str = "farihadua70@gmaiil.com"

print(f"My name is {name}, my age is {age} and my email is {email}")

# number:
num:int = 123
print(type(num))

#complex:
number = 1+2j
print(type(number))

#type casting:
#number, boolean can be converted into string but string can't be converted into number...

num1:int = 3
string:str = str(num1)
print(type(string))

#operators:
# Arithmetic operators:
a:int = 5
b:int = 4
print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division (answer in float)
print(a // b) # division (answer in real number)
print(a ** b) # power
print(a % b) # remainder

# comparative operators:

print(a > b) # greater than
print(a < b) # less than
print(a == b) # equals to
print(a >= b) # greater than equal to
print(a <= b) # less than equal to

#unary operators:

a += 5
print(a)

b -= 4
print(b)


