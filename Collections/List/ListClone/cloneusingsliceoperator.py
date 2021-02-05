x = [10, 20, 30, 40, 50]
# x = y # this is not cloning it is just a single list and both x and y is pointing to it
# Not recommended to use it as if any changes occures in x it will reflected to y

# cloning means complete same copy with different object reference
y = x[:]
print(id(x))
print(id(y))
print(x)
print(y)