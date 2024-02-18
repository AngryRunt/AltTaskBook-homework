i = int(input('количество дюймов: '))
miles = ((i // 12) //3) // 1760
yards = ((i // 12) //3) % 1760
foots = (i - miles * 1760 * 3 * 12 - yards * 3 * 12) // 3
inches = foots % 3
print(str(miles) + ' miles '+ str(yards) + ' yards ' + str(foots) + ' foots ' + str(inches) + ' inches ')