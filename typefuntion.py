                       
            # type() function 

# this is python built in function 
# this function used to find the data type of given variable in python (to cheack the data type of a object)

# for ex. 
price_in_number = 10
print(type(price_in_number))

# In a python every value has object 

#          = 555
#          =3.14
#          ="python"
#          =[1,2,3]

# these all are object and type() that objact class show 


# what is syntax 
#         The correct way to write something.(rule)

# for ex. type(10) correct way 
#         type("hello) incorrect way 
             
# when you learn python every function has two thing will be remember 
#  1. syntax (how to type ya how to write)
#  2. purpose (what to use it for)
             
# when professional developer type () function use?

# 1. debugging 
            # Debugging is the process of finding and fixing bugs (error) in a program.
# ex. 
# age = int (input("enter age :"))
# print("your age is ", age)

# what is done during debugging?
#     find SyntaxError
#     find RuntimeError
#     find logicalerror
#     check variable values (using print() statement or a debugger)
#     Run the code step by step to identify and fix problem 

# 2. ApI response 
# 3. Data base 
# 4. Machine learning 
# 5. type() limitation 

# A. isinstance() vs type()
#    this function more use than type() function bez in inheritance it will be work well


# # dtype and astype are specially use in pands 
 
# * type() :- (python built in function)
#         we were learn before 

# mark_in_number = 525
# print(type(mark_in_number))

# this tells the type of one object at a Time.

# * dtype = (data type) --- (.dtype)
#        this shows data type of pandas series or data frame colomn.
# ex. 
# import pandas as pd 
# age = pd.Series([20,22,52,])
# print(age.dtype)

# note : this use in data analysis, data science.
#        whole colomn data type shows


# # * astype -- (.astype)
#              it use to convert one data type to another data type 
#              it use in pandas 
# ex. 
import pandas as pd 
age = pd.Series(["20","55","355"])
print(age.dtype)
age = age.astype(int)
print(age.dtype)

note = whole column ya series convert it 
       it use data analysis, data cleaning 


