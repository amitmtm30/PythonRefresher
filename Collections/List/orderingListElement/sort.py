# reverse method reverse the list element by natural sorting order
# Natural sorting order for number is acccending order
# Natural sorting order for string is alphabetical order
# for sorting list should contains Homogeneous Order

list1 = [5, 20, 6, 8, 1, 19, 10, 3]
list1.sort(reverse=True)
print(list1)
list1.sort(reverse=False)
print(list1)
# if you do not want the natural sorting order then you have to pass the argument in reverse method as
# reverse = True --> it will sort the list in descending order

