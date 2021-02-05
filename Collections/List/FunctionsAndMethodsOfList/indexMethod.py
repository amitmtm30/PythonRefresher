# index() returns the index of the 1st occurance of duplicate element

l1 = [1, 2, 3, 4, 5, 6, 1, 2, 3, 1, 2, 3, 1, 4, 5, 6]
print(l1.index(1))  # 0
print(l1.index(2))  # 1
# print(l.index(50)) # ValueError

# Note in index method if the element of index is not there then will get  value error so to use this we have
# to first check whether element exist ot not

# How to check whether element exist or not

l2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

target_element = int(input("Enter Element which you want to be searched : "))

# if target_element in l2:
#     print("Element Found and their index is : ", l2.index(target_element))
#
# else:
#     print("Target Element Not Found")

# same above example with try except block
try:
    print("Element Found and their index is : ", l2.index(target_element))

except ValueError:
    print("Target Element Not Found")
