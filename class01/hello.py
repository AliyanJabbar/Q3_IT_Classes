# "rivayat of Hello World"

# print("hello world!")



# **"variables"

# name = "rohan"
# age = 13
# bollValue = False 
# print(name)
# print(age)
# print(bollValue)

# PI = 3.14 #all letters capitals to indicate the variable as constant. It's only converntion
# print(PI)



# F string
# name = "ali"
# fullName = f"My name is {name}"
# print(fullName)



# ** data types
# python is a dynamically typed language which means we don't have to specify the data type of the variable. The python will automatically detect the data type of the variable.
# int(), float(), str(), bool(), list(), set(), tuple(), dict(), complex(), None

# name:str() = 'ali'
# print(name)

# age:int() = 13
# print(f"age is {age}") #this is know as fstring and this is the replacement of the template literals in typescript

# num :float()= 11.5
# print(num)

# isMarried:bool() = False
# print(isMarried)

# myList:list() = [1,2,3,4,"5"]
# print(myList)

# mySet:set() = {1,2,3,4,"5"} #set is unordered
# print(mySet)

# myTuple:tuple() = (1,2,3,4,"5")
# print(myTuple)

# myDict:dict() = {"name":"ali","age":13}
# print(myDict)

# myComplex:complex() = 2j+3
# print(myComplex)

# none:None = None
# print(none)

# Difference between List, Tuple

# names1 = ["Okasha", "Ali", "Ahmed"] # Mutable
# names2 = ("Okasha", "Ali", "Ahmed") # Immutable
# names1[0] = "Aneeq"
# print(names1)
# names2[0] = "Aneeq"
# print(names2) #TypeError: 'tuple' object does not support item assignment

# Differece between List, set

# nums_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# nums_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(nums_list[0]) #1
# print(nums_set[0]) #cannot get elements of set through indexes because it is unordered that's why this line will give error "TypeError: 'set' object is not subscriptable"
# print(f"list: {nums_list}") #list: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(f"set: {nums_set}") #set: {1, 2, 3, 4, 5} , means set will not allow the duplicate values



# **"Operators"
# arithmetic operators 
# comparision operators
# logical operators
# assignment operators

# 1. arithmetic operators 
# +,-,*,/,=,+=,-=,**,%,//
# '**' is known as power or exponent 
# num =4
# num = num**2
# print(num) #16
# # % is known as modulus which gives remainder after division
# num = num+5
# num = num %4
# print(num) #1
# # "//" it will give the value after round off; like if the answer is 2.3 it will give 2
# num = num +10
# num = num // 2
# print(num) #5 #11 divide by 2 will give 5.5 but it is removing the decimal and giving 5 only

# 2.comparision operators
# <,>,==, <=, >=, !=
# examples
# a = 5
# b = 10
# print(a<b) #True
# print(a>b) #False
# print(a==b) #False
# print(a<=b) #True
# print(a>=b) #False
# print(a!=b) #True


# 3.assignment operators
# =,+=,-=,/=,*=,**=,//=,%=
# a = 5
# a += 5
# print(a) #10
# a -= 5
# print(a) #5
# a *= 5
# print(a) #25
# a /= 5 # the division will always give the float(in decimal) value
# print(a) #5.0

# 4.logical operators
# and, or, not
# a = 5
# b = 10
# c = 15
# print(a<b and b<c) #True
# print(a<b and b>c) #False
# print(a<b or b>c) #True
# print(not a<b) #False
# print(not a>b) #True




# ** conditional statements
# if, elif, else => here elif is the 'else if' in the typescript

# name = "ali"
# age = 13

# if name == "ali" and age == 17:
#  print(f"your name is {name} & your age is {age}") # the gap given at the start of this line is known as indentation and it is compulsory after the colon ":". The indentations represent the block "{}" in python 
# elif name =="ali" or age == 17:
#  print(f"your name is {name} & your age can vary which is {age}")

# else:print(f"your name is {name}")


# ** loops
# for, while

# for loop

# hobbies = ["cricket","football","swimming","reading","coding"]

# for hobby in hobbies:
#  print(hobby)

# for i in range(10): #range(10) will give the values from 0 to 9
#   print(i)

# for i in range(1,10): #range(1,10) will give the values from 1 to 9
#     print(i)

# for i in range(1,10,2): #range(1,10,2) will give the values from 1 to 9 with the gap of 2
#     print(i)


# while loop 

# i = 0
# while i<10:
#   print(i)
#   i+=1



# ** functions or definitions or methods

# 1.greeting function
# def greet(name:str):
#     print(f"hello {name}")
# greet("ali")


# 2.addition function
# def add(a:float,b:float):
#     return a+b

# print(add(2,5))