#                                            Type casting 


# It convert value of one data type other data type 
#   ex. "100" ---> 100
#        10-----> 10.0

# why need type casting --
#   in python --
#            "10"  and 10 are diffeent 

# for ex. age = input("Age") ---> suppose user give 20 input value 
 
#         in python -- type(age) ----> string 
#     if age + 5 ---> when you type it give error bez age is string 
# that why  you need type casting 

# so, age = int 


# two type of type casting --
#  1. implicit type casting 
#  2. explicit type casting 

# 1. implicit type casting (automatic)---> also known as corecion 
#     python itself convert type 
# ex. a = 10 ---> int
#     b = 2.5 ---> float 
#     c = a + b 
#  output = 12.5
#  what happen python itself convert 10 to 10.0

# 2. explicit type casting ----> also known as type conversion 
#     in which developer itself convert 
# ex.  a = "10"  ---> str
#      b = 5 --> int 
#      print(int(a)+ b) === 15




# type casting function ---
#       int()
#       float()
#       str()
#       bool()
#       list()
#       tuple()
#       set()
#       dict()
#       complex()

# 1. int()
#  ex. 
# a = 10
# b = str(a)
# print(type(a))
# print(type(b))

# 2. float()
# ex. float("25") --> 25.0
#     float(100) ---> 100.0

# 3. str()
# ex. str(500) ---> "500"

# 4. bool()
# ex. 
#  bool (0)---> False
#  bool (10)---> True
#  bool (" ") --> False 
#  bool ("python")---> True

# python think so,
#    empty ---> False
#    non empty ---> True

# professional how to use this type casting function

# name = input("enter name :")
# if name : 
#      print("name entered")
# else :
#      print("name is empty")

# if user not enter value ("") ---> if name : show False
# if user enter value ("shubham") ---> if name : show True

# Rule :- 

# 1. Truthiness Rule
#            python convert each value to bool()
# if value empty, zero or "kahich nahi" kahich show karta nasel tr ----> False
# all the rest ----> true 

# A. falsy values -- just some values are False
# ex. 
# bool(false) ---> false 
# bool(None) ---> false 
# bool (0) ---> False
# bool(0.0) ---> False
# bool(oj)   ---> false (complex zero)
# bool("") --> false 
# bool('') ---> false 
# bool ([])
# bool(())
# bool({})
# bool(set())
# bool(range(0))


# B. truthy values -- a few of above values all except are true.
#   ex.
# bool(1)
# bool(-10)
# bool(0.5)
# bool((10,20))
# bool({1,2})
# bool("false") inwhich false is string 
# bool([0]) in list zero is there it act has a element 
# bool("python")
# bool(" ") between string space thair
# bool([1])
# bool({"a",1})
# bool("0") string 

# Note -- python doesnot look at the meaning of a value it loooks at whether its empty or not 

# 5. List()
#       list ("python") this str ----> it convert in list ['p','y','t','h','o','n']

# 6. tuple()
#    tuple ([1,2,3]) this is list ----> it convert into tuple (1,2,3)

# 7. set ()
#    set([1,2,2,3]) this is list --> it convert into set

# note -- 
#   in string number is there than convertion possible 
#   in string letter is there than int() or float() convertion not possible 


# type casting type 
#  1. Temporary type casting 
#            the type only changes for that expression the original variable does not change 

# ex. age = "25"
# print(int(age) + 5) = 30

# 2. permament type casting 
#             stores the converted value back into thesame variables 
# ex. age = "25"
#     age = int(age)












# In python error means ?
   
# # error means -- python detected something wrong and could not execute the code.
# ex. print(10/0) ---> error 

# a. value error -- the data type is correct but the value in that type is incorrect 
ex. int("shub") ValueError

b. type error -- wrong data type used for operation 
ex. "10" + 5 ---> str , int (in python str and int addition not possible)

In professtional :
             once the devleoper understands what error has occurred the problem can be quickly identified

