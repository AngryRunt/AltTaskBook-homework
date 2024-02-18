f =  open('hw1.txt', 'w')
for i in range(1, 100):
    s = str(i) + '\t' + str(i ** 2) + '\t' + str(i ** 3)
    f.write(s + '\n')
f.close()
