character_name = "Rakesh chada"
print(character_name)
name, age, city = "sj", 25, "pune"
print(type(name),type(age), type(city)) #it used to check the type of only one variablr at a time.

# Rules of variables 
#  1. name starting : always name start with latters and underscore and not start with number
# for example. 
#               coustmer = "jadhav"  this valid 
#              _student= "shubham"  this valid 
#               10patient = "namdev" this not valid

#  2. case sensitive : uppercase and lowercase are consider different variables.
# for example.
#             maternal = "shanta" these are consider has a different 
#             Maternal = "sushuma"
#  3. keyword : python has its own words like if, else, for, class etc there are not use as a variables.
                # key words also case sensitive 
                    # eg. True, False, None these not show error but,
                      #   true, false, none these shows error because of case sensitive
                                                    
# multiple variables : 
#    eg. name = "sj"
#        age = 25
#        city = "nagpur" this type of variable commonly not use in python because of data confusion 

# in one line multiple variable :
#      eg name,age, city  = "sj", 25, latur 
# in one line multiple variable type() function used to check the type of one variable at a time 

# variable professional naming rules
# 1. in python mainly use snake_case 
#   ex. user_name = "sj"
#       stock_price = 100
#       employe_id_in_number = 99102

# 2. variable name should be meaningful
#   ex. x= 1000 in which what is x , any one not understand 
#       account_balance = 1000 this is meaningful

# 3. unit must be written in name
#   ex. time = 5 "5 means what second, minute, hours"
#       time_in_minute = 5

# 4. boolean variable :
#          professional programmer for boolean , is_, can_, has_ use 
#  ex. is_logged_in = True
#      can_permission = False
#      has_trade = True

# 5. type hinting (professional projects)
#    ex. account_balance: float = 500.0
# print(account_balance) when you get print dont use print(account_balance: float) bez it show error : this use for hint 

# 6. collection variables : if list variables then use plural 
# ex. users_name = ["a", "b", "c"]
#     stock_symbols = ["reliance", "tata power", "tcs"]

# 7. dictionary naming also in snake_case

# variable naming formula 
#       usally professional developer use 
#             context + information formula

# ex. studant_name = "shub"  context = studant , information = name
#     studant_age = 25       context = studant , information = age

#        information + context   
# ex.  total_mark = 95     information = total ; context = mark 
#  average_salary = 10555     information = average ; context = salary          
# # 8. avoid shortcuts 

# 9. constans : when program run thats values do not change.
#      in which upper case use for constant variables
# ex. USER_NAME = "SHUB"

# pascal case - every word has frist latter capital
#     in python pascalcase used for classes not for variables.
# ex. 
#    Frist_Name = "sj"  not use 
#    Total_mark = 25    not User
 
#  class Student Data :
#                pass =   

"""
                                        practice 

user information

user_id = 92948527
user_name = "@shubhamjadh"
last_name = "jadh"
frist_name = "shubh"
email_address = "airdropsj@gamil.com"
mobile_number = 7584236985
date_of_birth = 20/05/2002
is_active = True
created_at = 20/5/2012
last_login = 5/12/2025

e - commerce

product_id = 253462
product_name = "shampoo"
product_price = 250
stock_quantity = 100
discount_percentage = 10%

banking 

account_number = 120305564210
account_balance = 10025
transaction_amount = 5000
ifc_code = "IDFC2000"
branch_name = "idbi bank main branch"
account_holder_name = "shub jadh"
ammount_in_number = 5000
ammout_in_word = "five thousand" 
account_holder_aadhar_number = 1015565056222
account_holder_pancard_number = "jcb1545p"    """


# employee managenent 

# employee_id = 252641
# employee_name = "shubahm"
# department_name = "technical"
monthly_salary = 500000
annual_bonus = 10000
tax_percentage = 10
# joining_date = 04/05/2024
# years_of_experience = "5 to 6 years"
# working_hours = 8

tax_amount = monthly_salary * tax_percentage / 100
net_salary = monthly_salary + annual_bonus - tax_amount 
print(tax_amount)
print(net_salary)


# data analysis

# data_frame =
# column_name =
# missing_value =
# average_score = 
# max_value =
# min_value = 
# total_records =
# filtered_data =
# train_dataset =
# test_dataset =