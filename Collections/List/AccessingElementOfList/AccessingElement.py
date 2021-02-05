# Access Element using Index

l1 = [10, 20, 30, 40, 50, 60]

print(l1[0])  # Accessing 1st element
print(l1[1])  # accessing 2nd element
# print(l1[6]) # Lis index out of range error will get

# Access Element using slice
print(l1[0:10])
print(l1[0::])
print(l1[::])
print(l1[1::])
print(l1[::-1])

# Mutable concept List are mutable
l1[0] = 70
print(l1)

#### Example 2
l2 = [10, 20, 30]
l2[1] = 777
print(l2)

# Traversing the element of list
# 1. By using  loop

lst = [10, 20, 30, 40]
for x in lst:
    print(x)

print(" Trversing List Element by using While loop  ")
# 2 By using while loop
i = 0
while i < len(lst):
    print(lst[i])
    i = i + 1
