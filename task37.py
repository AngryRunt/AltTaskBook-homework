import math
def getlist(start, end = 0, step = 1):
    if end == 0:
        end = start
        start = 0
    list = []
    for i in range(start, end, step):
        list.append(i**2)
    return list
print(getlist(1, 10, 2))
