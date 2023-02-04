#2
'''start = 0
stop = int(input('stop = '))

while start <= stop:
    print(stop)
    start+=1
#3
k = int(input('k = '))
n = int(input('n = '))
while k<=n:
    print(k)
    k+=1
#4
start = int(input('start = '))
stop = int(input('stop = '))
summa = 0
while start <= stop:
    summa += start
    print(start)
    start+=1
print('----------------------')
print(summa)

#5
start = 0
n = int(input('n = '))
if n>10:
    while n>=start:
        start+=1
        if start==5:
            continue
        print(start)
else:
    print('error')
#6
start = int(input('start = '))
stop = int(input('stop = '))
while start<=stop:
    print(start)
    if start==5:
        break
    start+=1
#7
while True:
    print("it's an  infinite loop")
#8
word = 'hello world'
start = 0
stop = 4
while start<=stop:
    print(word)
    start+=1
########
#1
start = 1
stop = 31
while start<=stop:
    if start%5==0 and start!=5:
        print(start)
    start+=1
#2
start = 5
stop = 15
while start<=stop:
    if start%8==0 and start!=8:
        if start%10==0 and start!=10:
            print(start)
            start+=1
#3
start = 0
stop = 5
while start<=stop:
    print(f'{start})0')
    start+=1
#5
start = 1
stop = 14
summa = 0
while start <= stop:
     summa += start
     print(f'{start}+1')
     start+=1
print('=')

#7
start = 1
stop = 9
while start <= stop:
    print('9 x',start,'=',9*start,)
    start+=1'''

