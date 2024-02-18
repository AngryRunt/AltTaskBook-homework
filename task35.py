def func(a, b):
    return a + ' ' + b
girls = open('girls.txt', 'r').readlines()
boys = open('boys.txt', 'r').readlines()
n = len(girls)
for i in range(0, n):
    print(func(girls[i], boys[i]))

