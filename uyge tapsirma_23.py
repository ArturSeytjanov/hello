'''def Artur(start,stop):
    summa=0
    for x in range(start,stop+1):
        summa+=x
    return summa
print(Artur(1,10))
print(Artur(5,10))

def artur_2():
    start = int(input('start = '))
    stop = int(input('stop = '))
    summa = 0
    for x in range(start,stop+1):
        summa+=x
    return summa
print(artur_2())'''

#1

'''def sum_range(start,end):
    summa = 0
    if start > end:
        for x in range(end,start+1):
            summa+=x
    else:
        for x in range(start,end+1):
            summa+=x
    return summa
a = int(input('start = '))
b = int(input('end = '))
print(sum_range(a,b))'''

#1
'''def sum_range_2(start,end):
    if start>end:
        start,end=end,start
    summa = 0
    for x in range(start,end+1):
        summa += x
    return summa
a = int(input('start = '))
b = int(input('end = '))
print(sum_range_2(a,b))'''

#2
'''def fact(a):
    factorial = 1
    for x in range(1,a+1):
        factorial*=1
    return factorial
user = input('user = ')
print(fact(user))'''
#3
'''def square(a):
    for x in range(a):
        return square
a = int(input('a = '))
print(a**2)'''
#4
'''def perimetr(a,b):
    for x in range(a,b):
        return perimetr
a = int(input('a = '))
b = int(input('b = '))
print(a*b)'''

#5
'''def isEven(a):
        if a % 2 == 0:
            print('True')
        elif a % 2 == 1:
            print('False')
a = int(input('a = '))
isEven(a)'''
#6
'''numbers = [1,2,3,4,5,9,10,1]
summa = 0
for x in numbers:
    summa+=1
print(summa)'''
#7
'''def artur(a):
    if a % 3 == 0 and a % 2 == 1:
        print('True')
a = int(input('a = '))
artur(a)'''
#8
'''a =[1,2,3,4,5,15,6,7,8]
def maximum(a):
    number = 0
    for x in a:
        if number<x:
            number=x
    return number
print(max(a))'''
#9
'''a = [4,5,3,5,6,7,8,9,4,2,4,8]
def artur_2(a):
    schetchik = 0
    if a % 2 == 0:
        print(a)
print(artur_2)'''