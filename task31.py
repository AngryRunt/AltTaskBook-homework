import math
import numpy as np
pi = math.pi
f =  open('hw2.csv', 'w')
for i in np.arange(0, pi * 2, pi / 24):
    s = str(i) + ';' + str(math.sin(i)) + ';' + str(math.cos(i))
    f.write(s + '\n')
f.close()
