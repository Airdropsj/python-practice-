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

