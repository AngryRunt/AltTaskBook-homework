n = int(input('номер в группе: '))
m = n - n%5 + 1
print('m = ' + str(m))
b = int (m + 5)
c = int (m + 10)
print('выполнить задания: ' + str(m)+ ' ' + str(b) + ' ' + str(c))