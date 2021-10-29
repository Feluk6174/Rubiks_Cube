x = 3
y = 3
print(x, id(x))
def d_2(x):
    print(x, id(x))
def d_1(x):
    print(x, id(x))
    x += 1
    x -= 1
    print(x, id(x))
    d_2(x)
d_1(x)

print(x, id(x))
x += 1
y += 1
print(x, id(x))
print(x, id(y))