import math
def func(a, b):
    return a + ' ' + b
girls = open('girls.txt', 'r').readlines()
boys = open('boys.txt', 'r').readlines()
n = len(girls)
m = len(boys)
for i in range(0, min(n, m)):
    print(func(girls[i], boys[i]))
