# pop method : pop method is used to remove element from the list but it will remove the element from
# last index and returns the remove element

# pop method without argument
list1 = [10, 20, 30, 40, 50, 60, 70]
print(list1.pop()) # 70
print(list1.pop()) # 60

# if list is empty and then try to remove the element using pop method then will get indexError

# list2 = []
# print(list2.pop())

# pop method with argument
# pop(index) - - if you want to remove element from the specified index

List3 = [10, 20, 30, 40, 50, 60, 70, 100]
print(List3.pop(1)) # 20