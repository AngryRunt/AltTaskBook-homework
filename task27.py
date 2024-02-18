n = int(input('кол-во гостей: '))
kuski = 0
while kuski < n + n//2 + 1:
    kuski = kuski + 2
print(kuski/2)