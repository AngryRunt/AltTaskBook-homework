def func(a, b = 'hui'):
    return a + ' ' + b
s1 = input('строка1: ')
s2 = input('строка2: ')
print(func(s1, s2))
print(func(s1))
