# if you want to add element to list as a specific position in that case we have to use index method

list1 = [10, 30, 50]
print(type(list1))

# Now i am going to add element 20 at 1st index
list1.insert(1, 20)
print(list1)

# Now i am adding element 40 at 3rd index
list1.insert(3, 40)
print(list1)

# Note if the index is greater than the max index in that case element will be added at last index only
list1.insert(100, 60)
# 60 will be added to the last index
print(list1)
# Note if the index is less than 0 in that case element will be added to the oth index
list1.insert(-10, 5)
print(list1)