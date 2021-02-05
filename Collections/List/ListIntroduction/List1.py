# ListIntroduction:
#     ListIntroduction are presented through square bracket
#     Hetrogeneous objects are allowed
#     Dynamic in nature means once i create the list we can add or delete the element
#     Duplicates are allowed
#     Insertion Order preserved(the way you add (in order)in the same way you can see)
#     To Create Empty ListIntroduction : list = []

##  to add element in list we have list specific method i.e appened

# TO access list element:
# through index
# through slice
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# accessing through index
print(list1[0])
print(type(list1))

#Creation of ListIntroduction order
# Dynamic ListIntroduction By using eval
# testlist = eval(input("enter the list of element: "))
# print(testlist)
# print(type(testlist))

#by using list(): this method is applicable only for string data type

s = "Amit Kumar"
l = list(s)
print(type(l))
print(l)

# By using split function- split function returns list

s = "Learning Python is very Easy"
l = s.split()
print(l)
print(type(l))

# Accessing element by using index
l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(l[0])  # forward direction
print(l[-1]) #Backward direction
#find out the length of the list
print(len(l))
print("#" * 30)
#print out all the list element
# using while loop
i = 0
while i < len(l):
    print(l[i])
    i = i + 1
print("#" * 40)
# By using For loop
for x in l:
    print(x)
# Matematical Operation for list : + and *
# + means concatenation
# * means repetation
l = [10, 20, 30]
l.insert(1,40)
print(l)
l1 = [40, 50]
l2 = (1, 2, 3)
l3 = l + l1
print(l3)
print(l1 * 3)
# Note : For concatenation operation both argument should be list only other wise will get "Type Error"
# Note : For Repetition operator one argument should be int and other argument should be list only
print(l + l2)

