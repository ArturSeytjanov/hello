#SHART APERATORLARI
#if , elif , else
#syntax -
#if (shart):

'''a = 7
b = 9
if a>b:
    print('a>b')
else:
    print('b>a')

name_1 = input('name_1 -')
name_2 = input('name_2 -')
print(len(name_1),len(name_2))
if len(name_1)>len(name_2):
    print(f'{name_1}>{name_2}')
elif len(name_1)==len(name_2):
    print(f'{name_1}={name_2}')
else:
    print(f'{name_2}>{name_1}')
###################################
num_1=int(input('first number - '))
symbol=input('*,+,-,/ ? - ')
num_2=int(input('second number - '))

if symbol =='+':
    print(num_1+num_2)
elif symbol =='*':
    print(num_1*num_2)
elif symbol =='-':
    print(num_1-num_2)
elif symbol =='/':
    print(num_1/num_2)
else:
    print('error')
###################################
from turtle import*
bgcolor('blue')
pensize(2)
speed(100)
pencolor('green')
penup()
goto(70,100)
pendown()
for i in range(200):
    forward(i*2)
    right(i)
done()

a = int(input('a='))

if a>0 and a%2 == 1:
    print(a)

elif a<10 and a % 2 ==0:
    print(a)
#1
a = int(input("a= "))
if a>0 :
    print('bul + san')
elif a<0 :
    print('bul - san')'''

a = int(input('a='))
if a%2==0 :
    print(a)

