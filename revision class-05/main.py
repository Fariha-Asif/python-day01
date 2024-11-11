# non-primitive data types:
# aisi data types jn me multiple values store hojayen

# list: (multiple data types)

li = [1,2,3,4,"Fariha", 5.4, True]

# finding number of elements in list

length = len(li)
print(length)

# slicing, indexing, stepping

print(li[5]) # indexing

li2 = li[1:5] #slicing (agr child me changing ho to koi farq nh pre ga lekin agr parent me changing hogi to slice b chng hojye ga)
print(li2)
print(li)
# numpy me slice chng hogi to parent b chng hogi
# jo slice c copy nikle gi wo shallow copy hti hy yani uska effect parent pe nh hta
# aisi copy js c parent me b changing hojye wo deep copy hti hy

li3 = li[1:5:2]
print(li3)

# negative indexing:

print(li[-2])

# list functions:

li1 = [1,2,3,4,"Fariha", 5.4, True]

# if we want to add something in list so there are 3 function we have

# insert (specific position pr value add krni ho to)
li1.insert(3, "Faraz")

# append (values add at the end)
li1.append(10)

# extend (2 list ko merge krne k liye use hta hy)
li3 = ["a", "b", "c", "d"]
li1.extend(li3)
print(li1)

# agr value remove krni ho to uske b 4 functions hen

# remove (remove by name) 
li1.remove("Fariha") 

# pop (remove at the end if we don't give any value) it also has return type
remove_element = li1.pop() # remove end
print(remove_element)

remove_element1 = li1.pop(4) #remove specific index
print(remove_element1)

# clear (pori list clear ho kr empty list bn jye gi)
li1.clear()

# delete (yeh overall function hy yeh list, tuple, dict sb pe work krta hy)
# del li1(4)
# print(li1)

# count: (yeh btata hy k 1 value ktni dafa a rh hy list me)
li.count(1)

# copy: opri list ki copy bnane k liye
li5 = li1.copy()
print(li5) 

# sort (ascending/ descending order)
li1.sort() # ascending
print(li1)

li1.sort(reverse=True) # descending
print(li1)


# reverse

li1.reverse()
print(li1)

# index: (yeh btata hy k value knse index pr hy)
index_var = li.index("Fariha")
print(index_var)

# maximum
max = max(li1)
print(li1)

# minimum
min = min(li1)
print(min)

# sum
sum = sum(li1)
print(sum)


# tuple: (immutable yani changing nh ho skti)

tu = (1,2,3,4,4,4, "Fariha", True, 5.8)

count = tu.count(4)
print(count)

tu.index(3)
print(tu)

# single value tuple bnane k liye

tu1 = (1,)
print(tu1)

#if we want to take list of things from user:

list4 = []

for x in range(1,4):
    user_input = int(input(f"Enter {x} number: "))
    list4.append(user_input)
print(list4)

# we can convert list into tuple with the help of type casting

print(tuple(list4))

tu1 = (1,2,3,4)
tu2 = (2,3,4,5)

print(tu1 + tu2)
print(tu1 * 3) # values ko repeat krta hy

# nested list and tuple
tu3 = (1,)
tu4 = (2,3,4)
tu5 = (tu3, tu4)

print(tu5)

tu6 = [1,]
tu7 = [2,3,]
tu8 = [tu6, tu7]

print(tu8)

# Practice:

name = input("write you name: ")
edu = input("write your education: ")
roll_num = input("write you roll_num: ")
tup = (1,name, 2, edu, 3, roll_num)
print(f"Original tuple: {tup}")
list5 = list(tup)
print(f"Converted list: {list5}")
list5[1] = "Faraz" 
print(f"Updated list: {list5}")

list2 = [10,22,34,45,52,16,37,18]
user_input = int(input("write which highest number you want: "))
sorted_list = sorted(list2, reverse=True)
print(f"Numbers from highest to lowest: {sorted_list}")
print(f"{user_input}highest number is: {sorted_list}")
