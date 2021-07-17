# To print normal array

array = [10, 3, 7, 5]
print(array)

# To access the array we have use indexing: indexes starts with 0
print(array[0])
print(array[2])

# To get all the items from the array
print(array[:])

# To get first 3 items
print(array[:3])

# to access the elements from index 1 and 2
print(array[1:3])

# to access all elements except the last
print(array[:-1])

# to update any item
array[2] = 'Shubham'
print(array)

# To find the max element
# It is called as the linear search

array = [10,42,55,2,0]

max = array[0]

for num in array:
    if num > max:
        max = num

print(max)

# To find the minimum element from the array

array = [10,42,55,2,0]

min = array[0]

for num in array:
    if num < min:
        min = num

print(min)


