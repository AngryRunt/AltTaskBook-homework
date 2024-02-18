mylist = []
fib1 = 0
fib2 = 1
n = 10
summa = 0
for i in range(n):
    summa = fib1 + fib2
    mylist.append(summa)
    fib1 = fib2
    fib2 = summa
print(mylist)
f = open('file.txt', 'w')
for el in mylist:
    f.write(str(el)+'\n')