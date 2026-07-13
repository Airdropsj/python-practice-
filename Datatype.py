                                        # Datatype 
# Dataype is a classification that defines the kind of value a variable can store the operations that can 
# be performed on it and how it is represent in memory.


#                 classification of datatype

# 1. Numeric type 
#            int 
#            float
#            bool 
#            complex

# 2. tex type (sequance)
#            str 

# 3. sequance type 
#         list 
#         tuple
#         range

# 4. set type 
#        set 
#        frozenset 

# 5. mapping type
#        dict 

# 6. binary type 
#        bytes 
#        bytearray

# 7. special type 
#       None




# 1. Numeric type 
            
# A. integer (int)
#             immutable datatype,
#             it is whole number ,in this not decimal point 

# ex. number = 10
#     munber1 = -5
#     number2 = 0
#     number3 = 1502223 these are int

#     positive, negative and zero integer
#      10  positive int 
#     -10  negative int
#      0   Zero

# no size limit for integer in Python
#  x= 66666666666666666666666666666666666  thats valid 

#         In python interger written in four type
#  1. Decimal number (base 10)
#                 we daily used this number system 
#                  also no prefix use 
#   ex. 0123456789
#                  number = 25
#                  print(number)

#  2. Binary number (base 2)
#                 computer language and in which orefix use "ob"
#   ex.  01
#          number = ob1010
#          print(number)

#  3. octal number system (base 8)
#    ex. 01234567

#  4. hexadecimal number system (base 16)

# this example of integer
a= 10
b =a 
a+=1
print(a)

# B. floating type (float)
#            it represent in decimal point number 
#            immutable 
# ex.  price = 100.10

price_of_stock : float = 10.51
print(type(price_of_stock))

# real use of floating 

# 1. scientific calculation ex. gravity 9.88
# 2. temperature = ex. 35 c
# 3. machine learning = ex. accuracy 98.52
# 4. graphics programming 

# avoid using float for 

# 1. money
# 2. banking System
# 3. Gst calculation
# 4. Accounting software
# 5. stock treading settlement

# why not use float fot money
#    bez In float decimal value store in binary that why precision error wil be occourse. 

# therefore this type of error avoid using that

#  from decimal import Decimal
#    account = decimal ("0.1")
#    tax = deciaml ("0.2") 

# Note = "Use float when approximation is acceptable use decimal when exactness is mandatory"

# C. Boolan type 
#       boolan is an immutable built in numaric type representing truth values : True and False 

# ex. is_logged_in = True
#     is_admin = False 

# d. String (str)
#  collection os characters 
#  immutable 

# user_name = "shunaha"

# E. list 
#    list is uesd for many values in orderd 
#    mutable data type 

# fruit = ["apple", "banana", "mango"]

# F. tuple 
#    tuple means orderd but immutable 

# coordination= (101,022)

# G. set 
#    set means collection of unordered unique values
#    he dont kept duplicate values 
#    mutable 

# number = {1,2,3,4}

# H. frozenset
#    immutable set known frozenset

# colour = ({"red","blue", "green"})

# I. dictionary (dict)
#    dictionary means to key value pair in data store 

# student = {
#    "name" : "shubham",
#    "age" : 32
# }

# J. range

number = range(5)

for i in range (5):
  print(i)

K. None type

result = None



