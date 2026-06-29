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
#    ex. 
account_balance: float = 500.0
print(account_balance)

