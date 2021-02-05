# List inside list is known as nested list
# we can present as Matrix
l = [10, 20, 30, [40, 50, 60]]
print(l[3])
print(l[3][0])
print(" ######################################## ")

# matrix Representation
x = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# i want to read only row wise
for r in x:
    print(r)
print("$$$$$$$$$$$$$$$$$$$$$$$$$")
# for matrix style
for i in range(len(x)):
    for j in range(len(r)):
        print(x[i][j], end = ' ')