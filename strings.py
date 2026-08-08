                                                    # string 
# String is a data type in python.
# string is sequence of characters enclosed in quotes.
# ex.  "name"

# string can contain any of the following :--
# - Alphabet     - symbols
# - numbers      - spaces  - emojis  
# ex. "A" , "123" , "@#$%" , "python" , "hello 123" 

# single quotes :
name = 'shubham'

# Double quotes : 
name = "shubham"

# triple quotes :
name = '''my name is 
          shubbham'''

# string is immutable
# name = "python"
# name[0] = "j" ---(it give type error)

# index :-- ([])
      
    #   p    y   t   h   o   n
    #   0    1   2   3   4   5

language = "python"
print(language[2])
print(language[1])

# Negative Index

    #   p  y  t  h  o  n
    #  -6 -5 -4 -3 -2 -1 
print(language[-3])

# membership operators
# it check to any charater or word in the incide string 
text = "python"
print("p" in text)
print("x" in text)

# string concatenation -- (+)
# used to two string combine
frist = "hello"
second = "world"
print(frist + second)

# for space 
print(frist + " " + second)

# string repetition
print("python"*3)

# string slicing : --
        #  0   1   2   3   4
        #  h   a   p   p   y
        # -5  -4  -3  -2  -1

name = "happy"

# 1. basic slicing : -- 
print(name[0:4])
print(name[2:3])
print(name[:4])
print(name[1:])
print(name[:])

# slicing with skip value 
    #     0  1  2  3  4  5
    #     p  y  t  h  o  n
    #    -6 -5 -4 -3 -2 -1 

text = "python"
print(text[0:6:2])
print(text[::3])
print(text[-4:-1])

# string function/ method

# 1. checking methods
# 1. len() -- to find the lenght of string 
name = "shubham"
print(len(name))

# 2. .startswith() 
name = "shubham"
print(name.startswith("shu"))

# 3. .endswith()
print(name.endswith("ham"))

# 4. .isalpha()
print(name.isalpha())

# 5. .isdigit()
print(name.isdigit())

# 6. .isalnum()
print(name.isalnum())
age = "abc123"
hight = "123"
weight = "@@"
print(age.isalnum())
print(hight.isalnum())
print(weight.isalnum())

# 7. .islower()
print(name.islower())

# 8. .isupper()
print(name.isupper())

# 9. .isspace()
print(name.isspace())

# 2. case conversion 

# 1. .capitalize()
text = "python programming"
print(text.capitalize())

# 2. .upper()
print(text.upper())

# 3. .lower()
lower = "SHUBHAM"
print(lower.lower())

# 4. .title()
print(text.title())

# 5. .swapcase()
easy = "PyThOn"
print(easy.swapcase())


# 3. replacement method 
# 1. .replace()
employee = "ramesh"
print(employee.replace("remesh", "suresh"))

fruit = "banana"
print(fruit.replace("a", "@"))
print(fruit.replace("a","@",1))

# 3. search method 

# 1. .find() --(index)
position = "shubham  jadhav"
print(position.find("shubham"))
print(position.find(" "))
print(position.find("h"))
print(position.find("jadhav"))
print(position.find("ram"))

text = "banana"
print(text.find("a"))

# 2. .index() -- same has find but difference is when text is not found it get error.
text = "python"
print(text.index("n"))
# print(text.index("java")) --- value error

# 3. .rfind() --- find right side 
text = "banana"
print(text.rfind("n"))

# 4. .rindex()
print(text.rindex("a"))

# 5. .count() --- it count repetation of word
print(text.count("a"))


# 3. space handling method 
# 1. .strip() -- remove the extra space (left and right both side space remove)
text = "   python   "
print(text.strip())

# 2. .lstrip() -- left side space will be remove 
print(text.lstrip())

# 3. .rstrip() -- reight side space wiil be remove 
print(text.rstrip())

# 4. split and join method
# split and join thes two are most used string method 

# 1. .split()
text = "apple mango banana orange"
print(text.split())

# fruits = ['apple', 'mango', 'banana'] ----split for string not for list
# print(fruits.split())

# split(maxsplit) -- how many string will be split
print(text.split(" " , 2))

# 2. .rsplit() - it break from right side
print(text.rsplit(" ", 2))

# 3. .splitlines()
text = "apple\nmango\nbanana"
print(text.splitlines())

# 4. .join() --- list to string 
colours = ["red", "blue", "green"]
print(" ".join(colours))

# escape sequance characters
# --- always use backslash (\)

# 1. \n (new line) : new line
new_line = "hello\npython"
print(new_line)

# 2. \t (large space tap)
tab_space = "name\tage"
print(tab_space)

# 3. \\ (backslash) to print backslash
print("c:\\user\\shubham")

# 4. \' (single quote) for print '
print("i\'m shubham")

# 5. \" (double quote) for print double quote
print("he said \"hello\"")

# 6. \b (backspace) 
print("helloa\b")
print("shubhamk\b")

# 7. \r(carriage return)
print("hello\rhi")

# 8. raw String (r" ")
print(r"hello\nshubham")

# f string 
    #  f"{}"

name = "Ram"
age = 20
print(f"my name is {name}")
print(f"my age is {age}")
print(f"my name is{name} and i am {age} years old")

number1 = 10
number2 = 25
print(f"sum={number1 + number2}")

# method
name = "python"
print(f"{name.upper()}")

# indexing
text = "python"
print(f"length = {len(text)}")