# to remove element from the list, we use the method remove()
# it will remove and do not return the removed element
# if element is not available in that case will get valueError
# so before removal we need to know the element should be present there
import time

list1 = [10, 20, 30, 40, 50, 60]
list1.remove(20)
print(list1)
# list1.remove(70)
# print(list1)

# WAP to remove the element from the given list
List2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
removalelement = int(input("Enter the Element which you want to be removed : "))
if removalelement in List2:
    List2.remove(removalelement)
    print("Element Removed Successfully")
    time.sleep(5)
    print(List2)
else:
    time.sleep(3)
    print("Element Not Found")
