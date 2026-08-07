                                                #   operatures
# an operator is a symbol or keyword used to perform an operation on values or variables in python.
total_salary = 10000
tax_total = 2000
total_income = total_salary - tax_total 
print(total_income)

# types---

# 1. Arithmetic opeartor
# 2. Assignment 
# 3. comparison 
# 4. logical 
# 5. other

# 1. arithematic -- this used for mathematical calculation 

# a. Addition (+) :-
making_cost_toy = 400
tax_on_toy = 10
total_cost = making_cost_toy + tax_on_toy
print(total_cost)

# b. subtraction
profit_in_share = 100
loss_in_share = 20
total_profit = profit_in_share - loss_in_share
print(total_profit)

# c. multiplication
quantity_of_share = 50
price_of_one_share = 20
total_amount = quantity_of_share*price_of_one_share
print(total_amount)

# d. division 
invest_ammount = 500
share_price = 15
buy_quantity = invest_ammount/share_price
print(buy_quantity)

# e. floor division 
invest_ammountnvest_ammount = 500
share_price = 15
buy_quantity_roundfiger = invest_ammount//share_price
print(buy_quantity_roundfiger)

# f. modulus/remainder
invest_ammountnvest_ammount = 500
share_price = 15
quantity_remaning = invest_ammount%share_price
print(quantity_remaning)

# g. power
side = 10
area = side**2
print(area)
# (in 10 square root)/
number = 2
result = number**3
print(result)
# (2 cube)

# 2. Assignment 
# ex.
variable1 = 15
variable2= variable1
# value of variable1 assign into variable2

# Assignment operators

# 1. Assign ---(=)
value = "name"

# 2. Add and assign ---(+=)
number = 5
number += 10
print(number)

# 2. subtract and assign --(-=)
number = 52
number -= 25
print(number)

# 3. multiply and assign --(*=)
number = 8
number *= 2
print(number)

# 4. Divide and assign --(/=)
number = 7
number /= 2
print(number)

# 5. floor divide and assign --(//=)
number = 7
number //= 2
print(number)

# 6.  remainder and assign --(%=)
number = 9
number %= 2
print(number)

# 7. power and assign ---(**)
number = 2
number **= 3
print(number)

# 3. comparison operators 

# a. equal --(==)
stored_password = "abc123"
enterd_passward = "abc123"
print(stored_password == enterd_passward)

# b. Not equal --(!=)
stored_password = "abc123"
enterd_passward = "ab123"
print(stored_password != enterd_passward)

# c. greater than --(>) 
# left side value is greater than right side 
max_salary = 10000
min_salary = 15000
greater_value = max_salary > min_salary
print(greater_value)

# d. less than --(<)
# left side value is less than right side 
max_salary = 10000
min_salary = 15000
greater_value = max_salary < min_salary
print(greater_value)

# g. greater than equal to -- (>=)
a = 10 >= 15
print(a)

# f. less than equal to -- (<=)
a = 10 <= 15
print(a)

# string comparison 
print("apple" == "origan")
print("apple" == "apple")

# chained comparison 
age = 25
print( 18 <= age <= 60)

#4. logical opertaors 

# A. and --(both condition are true)
# ex . 1
age = 25
print(age >= 18 and age <= 60)
# ex 2.
age = 65
print(age >= 18 and age <= 60)

# B. or --(any one condition are true )
marks = 85
print(marks >= 90 or marks >= 80)

# C. not --(true to false and false to True)
print(not True)
print(not False)

# D. identity operators 
# both variables point towards the same object .
a = [1,2,3]
b = a 
print(a is b )

a = [1,2,3]
b = a 
print(a is not b )

# E. membership operators 
# that check value in collection (collection = list, tuple, set, string, dictionary)
fruits = ["apple" , "banana", "mango"]
print("orange" in fruits)
print("orange" not in fruits)

# in string 
name = "shubham"
print("shu" in name)






 

