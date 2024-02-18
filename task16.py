n = int(input('n = '))
x = 0
for i in range (1, n+1):
    if x % 2 == 0:
        x = abs(x)+1
    else:
        x = (abs(x)+1) * (-1)
    print (x)