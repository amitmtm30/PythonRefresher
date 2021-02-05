# list[expression x in sequence]

list = [x+x for x in range(1, 10)]
print(list)

list1 = [x*x for x in range(1, 5)]
print(list1)

list2 = [x for x in range(1, 100) if (x%10)==0]
print(list2)