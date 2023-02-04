#for
#17
'''start = 0
stop = int(input('n = '))
a = float(input('a = '))
summa = 0
for x in range(start,stop+1):
    summa += a**x
print(summa)'''
#19
'''start = 1
stop = int(input('n = '))
a = float(input('a = '))
fact = 1
for x in range(start, stop+1):
    fact *= x
print(fact)'''
#20
'''start = 1
stop = int(input('n = '))
summa = 0
fact = 1
for x in range(start,stop+1):
    fact *= x
    summa += fact
print(summa)'''
#21
'''start = 1
stop = int(input('n = '))
summa = 0
fact = 1
for x in range(start,stop+1):
    fact *= x
    summa += x/(fact)
print(summa)'''
#36
'''start = 1
stop = int(input('n = '))
summa = 0
for x in range(start,stop+1):
    summa +=x**((stop+1)-x)
print(summa)'''
#37
import random
N = random.randint(1,11)	