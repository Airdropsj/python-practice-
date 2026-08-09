                                            # lists and tuple
# List means in one variable many value Store

# in python list --- square brakets []

        #    0         1         2     3    4
friends = ["apple", "banana", "shubh", 7, False]
          #  -5        -4       -3    -2   -1 

print(type(friends))

# list --- different dtatatype Store
        #   - data in sequance 
        #   - Index
        #   - duplicate value store
        #   - change value possible
        #   - orded , mutable

# list indexing 
print(friends[2])
print(friends[3])

# list slicing 
      # 0  1     2
list = [7, 9, "harry"]
print(list[0:2])
print(list[:])

# list methods

# 1. .sort() --- ascending order
numbers_in_series = [1,8,9,5,3,7,2,4,6]
numbers_in_series.sort()
print(numbers_in_series)

# 1a. .sorted() new sorted list return
# numbers_in_series.sorted()
# print(numbers_in_series)

# 2. .reverse() 
numbers_in_series.reverse()
print(numbers_in_series)

# 3. .append() -- add value to the end 
numbers_in_series.append("nikhil")
print(numbers_in_series)

numbers = [10,3]
numbers.append([1,3])
print(numbers)
numbers_in_series.append(numbers)
print(numbers_in_series)

# 4. .insert() --- insert the value on specific index
                # .insert(index, value)
names = ["Ram", "Amit"]
names.insert(0, "raju")
print(names)

# 5. .pop()  -- specific index delete and show deleted value 
                #  .pop(index)
numbers = [10, 20, 30, 40, 52]
delete_value = numbers.pop(2)
print(numbers)
print(delete_value)
numbers.pop()
print(numbers)

# 6. .remove() -- mention the value you delete 
series = [10,2,3,"jadhv"]
series.remove(2)
print(series)

# 7. .extend() -- adding one list to another list
values1 = [1,2]
values2 = [3,4]
values1.extend(values2)
print(values1)

# 8. .clear() -- hole list will be empty 
values1.clear()
print(values1)

# 9. .index() -- which value on index it will show
varities = [10, "name", 20, 52]
print(varities.index(20))

# 10. .count() ---- the repetation of value 
repits = [1,22,22,2, 22]
print(repits.count(22))

# 11. .copy() -- copy the list
copy1 = [1, 2 ,3 ]
copy2 = copy1.copy()
print(copy2)
copy2.append(500)
print(copy1)
print(copy2)

# nested list list inside list
nested = [[1 ,2], [85, 21]]
print(nested[0])
print(nested[1])

# 12. len()
length = ["attention", "jadhav", 15, 25, 10.5]
print(len(length))

# 13. max() -- find max value 
max_number = [17 , 52, 555 , 1000005]
print(max(max_number))
max_alpha = ["shubham", "jadhav", "apple"]
print(max(max_alpha))

# 14. min() --- find small value 
min_naumber = [1, -1 , 20, 25 ,47]
print(min(min_naumber))

# 15. sum() -- number of sum
total_naumber = [10, 25 , 15]
print(sum(total_naumber))


                                        #    Tuple
# - ordered 
# - immutable 
# - duplicate value allow
# - any data type allow

                         # tupe ---- round brackets()
# tuple indexing 
# same indexing as  list
            #     0       1  2    3
alnum_data = ("shubham", 25, 7, 12.03)
            #    -4      -3 -2   -1 

print(type(alnum_data))
print(alnum_data[0])
print(alnum_data[3])
print(alnum_data[-2])

# tuple slicing
print(alnum_data[1:2])
print(alnum_data[:3])
print(alnum_data[0:4:2])

tuple = ()
print(type(tuple))

single_tuple =(10,)
print(type(single_tuple))
print(single_tuple)

# without parenthesess (packing)
packing = 10, 25 ,33 
print(packing)
print(type(packing))

# unpacking 
data = (10, 25, 62)
name, age, weight = data
print(name)
print(age)
print(weight)

# extended unpacking
       # 0   1      2     3     
data = (25, 65, "175cm", 34 )
print(type(data))
age ,*weight, hightchest = data
print(age)
print(weight)
print(hightchest)

numbers = (10,12,15,15,78,25,39)
frist_series, *second_series, last_number = numbers
print(frist_series)
print(second_series)
print(last_number)

# tuple methods

# 1. .count()
print(numbers.count(15))

# 2. .index() -  show the value of position
print(numbers.index(78))

# tuple operators 

# 1. + concatenation -- combine two tuples
my_t1 = (2, 3)
my_t2 = (1, 2)
my_t3 = my_t1 + my_t2
print(my_t3)

# 2. * repetition 
that_t_repitation = (1, 2)
print(that_t_repitation*4)

# 3. in/not in 
is_value_in = (10, 20, "shubham")
print("shubham" in is_value_in)
print(20 not in is_value_in)

# 4. comparison operators
print((101, 200, 545) == (101, 200, 545))
print((11, 22) == (11, 55))

# mutable objest inside tuple
mutable_t = (10, [20,30],40)
mutable_t[1].append(888)
print(mutable_t)

# tuple conversion -- list to tuple and tuple to list
# list2 = ("none", 10, 52, 54)
# list1 = list(list2)
# print(list1)

convertion_t = [10, 20, 32, 54, 64]
t1 = tuple(convertion_t)
print(t1)

convert_1 = (101, 51, 666 , 85)
h1 = list(convert_1)
print(h1)