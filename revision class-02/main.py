# input function:

name:str = input("Write your name: ")
print("My name is: " + name)

age = input("write your age: ") # input ki type by default string hoti hy
print("Your age is: " + age)
age_int = int(age)
print(type(age))



# string:

#string is an immutable data type it can't be changed if we want to change it we have to store string in other variable..
# it can be created by ('') single quoted,  ("") double quoted and ("""  """) tripple quoted
datatype = "uzair yasin is 20 20.5 true"
print(type(datatype))

# slicing
name:str = "Fariha Asif"
name1:str = "Fariha Faraz Faham Falak"

# slicing will be
#(name [start, end]) end -1
print(name[0:5])


# indexing  (indexes are of two types positive and negative)

print(name[0])
print(name[-1])

print(name1[0])
print(name1[1])
print(name1[2])
print(name1[3])
print(name1[4])
print(name1[5])


print(name1[0] , end="")
print(name1[1] , end="")
print(name1[2] , end="")
print(name1[3] , end="")
print(name1[4] , end="")
print(name1[5])

for z,y in enumerate(name):
    print(f"{z}: {y}")   # yeh fucntion btata hy knsa character knse index pe rkha hua hy


# steping

#(name[start, end, step]) step means wo utne words skip kr dy ga
print(name1[0:10:2]) 
print(name1[::3]) # total pr apply hoga yeh
print(name[::1]) # total as it is  print hojye ga 1 steping dene c
print(name[::-1]) # is -1 steping dene c pori string reverse kr deta hy
print(name[::-2]) # reverse me 1,1 character chor deta hy

intro:str = "My name is Fariha and my age is 24 and my qualification is inter."

for x,y in enumerate(intro):
    print(f'{x} : {y}')

# print(intro[11:17], end=" ")
# print(intro[32:34], end=" ")
# print(intro[59:64])

print(intro [11:17], intro[32:34], intro[59:64])

number = "123456789"

print(number[1:9:2])

# string function

name2:str = "Fariha Asif"

name3 = name2.lower()
print(name3)

name4 = name2.upper()
print(name4)

name5 = name2.title()
print(name5) # All words ka first character capital

name6 = name2.capitalize() # 1st word k 1st ko bs capital baqi sbko small
print(name6)

name7 = name2.casefold() # string ko lower case me convert krta hy
print(name7)

name8 = name2.swapcase() #jo upper hon ge wo lower hojyen ge or jo lower hon ge wo upper hojyen ge
print(name8)

name9 = name2.center(20, ".") # is me jtni value den ge wo left or right pe space utni dy dega or text center me ly aye ga
print(name9)

name10 = name2.endswith("a") # yeh hmen btata hy k hmari string is word pe end ho rh hy ya nh ho rh agr ho rh hti hy to true ajata hy wrna false ajata hy
print(name10)

name11 = name2.count("a") # yeh btata hy string me ek character ktni br a rha hy count kr k btata hy
print(name11)

name12 = name2.expandtabs(17) # yeh \t ko expand kr deta hy jc \t 8 spaces ati hen to mazeed hm is c control krte hen spaces ko
print(name12)

name13 = name2.find("h") # yeh sirf first occurence pe jo character mile ga uska index return kr k dy deta hy 
print(name13)

name14 = name2.index("h") #yeh dono words same kam krte hhen bs ek difference hy k jo exist nh krta us me error generate hojata hy index k through jb k find -1 index dy deta hy uska
print(name14)

print("-".join(name2)) # yeh 2 kamon k liye use hta hy
print("  ".join(name2))
print("__".join(name2))

li = list(name2)
print(li)
name15 = "".join(li)
print(name15) # join ka method list ko string me convert krne k liye b use hti hy

name_1 = "Fariha"
li1 = list(name_1)
print(li1)

name_3 = li1.pop()
print(name_3)

name_2 = "".join(li1)
print(name_2)



# if statement

# types of if statement
# 1. if statement  (agr condition true hui to run hojye gi wrna agr false hogi to kch b print nh hoga)
# 2. if else statement 
# 3. elif statement
# 4. nested if statement
# 5. ternary statement | short hand if else statement

i = 10
if (i == 10):
    print("i is smaller than 5")


if (i < 5):
    print("i is equals to 10")
else:
    print("i is not equals to 10")


j = 25
if (j == 10):
    print("j is equals to 10")
elif (j == 15):
    print("j is equals to 15")
elif (j == 25):
    print("j is equals to 25")
else:
    print("j is not present")

# nested if

k = 10
if (k == 10):
    print("parent if")
    if(k > 5):
        print("child if")
    else:
        print("child else")
else:
    print("parent else")




if (k == 10):
    print("parent if")
    if(k < 5):
        print("child if")
    else:
        print("child else")
else:
    print("parent else")



if (k != 10):  # is me wo child pe jye ga hi nh agr if ki condition false hui to nested pe nh jye ga direct parent else pe jye ga
    print("parent if")
    if(k > 5):
        print("child if")
    else:
        print("child else")
else:
    print("parent else")

# grading assignment:

mark = int(input("Kindly write your marks "))

if (mark >= 90):
    print("A grade")
elif (mark >= 80):
    print("B grade")
elif (mark >= 70):
    print("B+ grade")
elif (mark >= 60):
    print("B- grade")
elif (mark >= 50):
    print("C grade")
else:
    print("Fail")