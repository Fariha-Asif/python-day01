# for loop:
# there is only for in loop

# number = 2 (we can't iterate over one number for running loop there must be multiple values or characters like list, tuple, string)

# for loop in string:

name = "Fariha"

for characters in name:
    print(characters)

# for loop in list:

number = [1,2,3,4,5,6,7,8,9]

for x in number:
    print(x)

# we can also store directly without making list or string variable

for n in "Faraz":
    print(n)

# range loop:
# (start, end, step)

for x in range(1,4):
    print("Fariha")

for x in range(1,10):
    print(x)

for x in range(0,11,2):
    print(x)

# enumerator function: (agr bht bra string ho to yeh lga den)
# yeh hmen 2 chizen return krta hy character k sth index b return kr k deta hy

name_1 = "Fariha"

for index, char in enumerate(name_1):
    print(index, ":", char)

# nested for loop:

for x in range(1,4):
    for y in range(1,4):
        print(x, y)


# while loop:
# while k loop me condition false hona zruri hy wrna phr infinite loop chl jye ga

count = 0

while count < 3:
    print("Hello Fari")
    count += 1


# control statement:

for x in range(1, 10):
    if x == 5:
        continue
    print(x)


for x in range(1, 10):
    if x == 5:
        break
    print(x)


count = 0

while count < 3:
    print("Hello Fari")
    break
    count += 1 # yeh forcefully break hogya hy jc hi break ka keyword remove hoga yeh phr run hone lg jye ga


# count = 0

# while count < 3:
#     print("Hello Fari")
#     continue
#     count += 1  # yeh infinite loop run hojye ga

count_1 = 0

while count < 5:
    print("Hello Fari")
    count += 1
    if count == 1:
        print("Continue")
        
        
count_1 = 0

while count < 5:
    print("Hello Fari")
    count += 1
    if count == 1:
        continue


condition = True
while condition:
    user_input = input("write your name: ")
    if user_input == "exit":
        condition = False
    print("type exit to close. ")


condition = True
while condition:
    user_input = input("write your name: ")
    if user_input == "exit":
        break
    print("type exit to close. ")


# practice:

user_input = int(input("write table number"))
for x in range(1,11):
    print(f"{user_input} x {x} = {user_input**x}")



for x in range(1,6):
    print("*****")
    

# count = 0
# while count <= 5:
#     print("*")
#     count += 1

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)