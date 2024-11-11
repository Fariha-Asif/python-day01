#two dimension list:
li = [1,2,3,4,5,6,7,8,["a","b","c","d",[12,13,14]]]

li2 = li[8]
print(li2)

print(li2[1])

print(li[8][4][2]) # multi indexing

for x,y in enumerate(li):
    print(x,y)

# dictionary:

dict5 = {
    "a": 1,
    "b": 2,
    "c": 3,
}
print(dict5)
print(dict5["b"])

dict1 = {
    "a": [1,2,3],
    "b": (1,2,3),
    "c": {
        "d": [5,6,7]
    }
}
print(dict1)
print(dict1["b"])
print(dict1["b"][1])
print(dict1["c"]["d"][2])

dict2 = {
    1: [1,2,3],
    2: (1,2,3),
    3: {
        4: [5,6,7]
    }
}
print(dict2[3][4][2])

dict3 = {}
print(dict3)

dict3["a"] = 1
dict3["b"] = 2
dict3["c"] = 3
dict3["d"] = 4
dict3["e"] = 5

print(dict3)

dict4 = {}
print(dict4)

dict3["a"] = int(input("write any number: "))
dict3["b"] = 2
dict3["c"] = 3
dict3["d"] = 4
dict3["e"] = 5

print(dict3)

dict4 = {}
print(dict4)

dict3[int(input("write a key: "))] = int(input("write any number: "))
dict3["b"] = 2
dict3["c"] = 3
dict3["d"] = 4
dict3["e"] = 5

print(dict3)

dic = dict([(1, "a"), (2, "b"), (3, "c")])
print(dic)


del dic[1]
dic.clear() # full empty krdy ga
print(dic)

# formkeys method:

seq = ("a", "b", "c")
print(dict.fromkeys(seq, None))

tu = (1,2,3,4,5)
print(dict.fromkeys(tu, "Fariha"))


# get method:

dic2 = dict([(1,"a"),(2,"b"),(3,"c")])
print(dic2)

print(dic2.get(2))

print(dic2.get(4)) # agr yeh wala index likhen to is c error nh aye ga blke none ajye ga


