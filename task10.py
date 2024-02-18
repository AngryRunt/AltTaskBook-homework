import sys
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a == 0:
    x = -c / b
    print('x = ' + str(x))
    exit()
d = b**2 - 4 * a * c
x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)
if d < 0: 
    print('корней нет')
elif d > 0:
    print('x1 = ' + str(x1) + ' x2 = ' + str(x2))
