#1
'''numbers_2 = [1,2,3,4,5,6,7,8,9]
summa = 0
for x in numbers_2:
    summa+=x
print(summa)'''
#2
'''a = [4,5,6,7,8,9]
def multiply(a):
    total = 1
    for x in a:
        total *= x
    return total
print(multiply(a))'''
#3
'''def factorial(a):
    fact = 1
    if a == 0:
        return 1
    else:
        return a * factorial (a-1)
n = int(input('san kiritin : '))
print(factorial(n))'''
#4
'''start = int(input('Startti kiritin = '))
stop = int(input('Stopti kiritin = '))
number = int(input('arasindagi sandi kiritin = '))
def artur(start,stop,number):
    if start and stop and number >= 1 and start and stop and number < 10:
        print('Duris')
    else:
        print('Qate')'''
'''   numbers = {x:x**2 for x in range(1,31)}
    print(list[numbers])'''
     
#8
start = 1
stop = 30
def artur_1(start,stop):
    for x in range(start,stop):
        if x**start:
            print(x)

artur_1