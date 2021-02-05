# clone the list by using copy method

x = [10, 20, 30, 40, 50, 60]

y = x.copy()
print(y)
y[1] = 777
print(x)
print(y)