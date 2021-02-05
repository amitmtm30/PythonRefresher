# extend method is used to extend the list with the elements of the other list
# Note : extend method does not return any thing it returns None only so we cannot assign this to any variable
# Note by using the extend method it will change the list elements

list1 = [10, 20, 30]
list2 = [40, 50, 60]
list1.extend(list2)
print(list1) # in this case we are extending the list1 with the elements of list2

################################# None ##################################################

list3 = [70, 80, 90, 100]
list4 = [200, 300, 400]
list5 = list3.extend(list4)
print(list5)

##############################################################################
# if you donot want to change any thing in the existing list and want to extend the list then better use the + operator

list6 = [500, 600, 700]
list7 = [800, 900, 1000]
list8 = list6 + list7
print(list8)
print(list6)
print(list7)
