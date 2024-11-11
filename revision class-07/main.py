# Error handling:

#type error 
x = 5
y = "Fariha"

try:
    print(x + y)
except TypeError as d:
    print(d)

print("Fariha")

# zero division error
x = 5
y = 0

try:
    print(x / y)
except ZeroDivisionError: # agr variable me stor nh krwana to print statement koi likhni lazmi hy
    print("Error occured")


x = 5
y = 0

try:
    print(x / y)
except ZeroDivisionError as b: 
    print(b)


x = 5
y = 0
z = "Fariha"

try:
    print(x + z)
    print(x / y)
    print(x + y)
except ZeroDivisionError as b: 
    print(b)
except TypeError as c:
    print(c)


x = 5
y = 0
z = "Fariha"

try:
    print(x + z)
    print(x / y)
    print(x + y)
except ZeroDivisionError as b: 
    print(b)
except TypeError as c:
    print(c)
else:
    print("No exception occurred") # agr error nh aye ga to else chle ga 
finally:
    print("This will always run") # finally hmesha chle ga

# syntax error: (direct handle nh ho skta yeh ata hy compiled time pe)

try:
    exec("x === 5")
except SyntaxError as e:
    print("Caught a Syntax Error:", e)

# when we don't know which type of error is coming:

x = 5
y = 0
z = "Fariha"

try:
    print(x + z)
    # print(x / y)
    # print(x + y)
except Exception as b: # handle overall errors
    print(b)

# raise error: (jo hm khud error raise krte hen)

user = input("Enter you age")
type1 = type(user)
print(type1)

if type(user) == str:
    raise ("this is not a valid input")

# File handling:

r = open("file.txt" , "r")

# read the content of the file
content = r.read()

r.close()

print(content)

# write the content: (override kr deta hy data ko)

w = open("file.txt" , "w")

w.write("This is new data")

w.close()

r = open("file.txt" , "r")

content = r.read()

r.close()

print(content)

# if file doesnot exist: (it will create new file)

w = open("file1.txt", "w")

w.write("This is new file data")

w.close()

r = open("file1.txt" , "r")

content = r.read()

r.close()

print(content)

# append the data  (jtni dfa code run hoga utni hi lines add hti chli jyen gi)

a = open("file.txt" , "a")

a.write("\nThis is second new data")

a.close()

r = open("file.txt" , "r")

content = r.read()

r.close()

print(content)

# override the data:

r = open("file1.txt" , "r+")
r.write("This written using r+")
r.seek(3) # words  hide kr deta hy
content = r.read()

r.close()

print(content)

r = open("file1.txt" , "r")

content = r.read()

r.close()

print(content)

# w+ (read and write both we can do)
# a+ (read and append both we can do)

# automatically close hojye file open hone k baad

with open("file.txt", "w+") as d:
    d.write("\nFariha")
    d.seek(0)
    content = d.read()
    print(content)
