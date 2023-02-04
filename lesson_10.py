#CIKL

#for-aperator #while-aperator
#1
'''while True:
    print('hello world')
#2
start = 0
stop = 20

while start <= stop:
    print('hello world')
    stop += 1
#2
start = 1
stop = 10
while start <= stop:
    print(start)
    start += 1
#3
start = int(input('start = '))
stop = int(input('stop = '))
while start <= stop:
    if start %2 == 1:
        print(start)
    start += 1
#4
start = 0
while True:
    print(start)
    if start == 30:
        break
    start += 1
#5
words = 'Rasul,Jurabek,Maman,Almat,Artur,'
start = 0
stop = len(words)
user = input('username = ').capitalize()
print(stop)
while start < stop:
    if user == words[start]:
        print(user)
        break
    start += 1
#6
start = 0
stop = 20

while start <= stop:
    start+=1
    if start == 10 or start == 15:
        continue
    print(start)
    print(start)
#7

word = input('type a word - ')
start = 0
stop = len(word)
print(stop)
print()

while start < stop:
    if word[start] == 'b':
        break
    print(word[start])
    start += 1
#8
start = 0
stop = int(input('n = '))
k = 5
while start < stop:
    print(k)
    start+=1
#9
start = int(input('a = '))
stop = int(input('b = '))
schetchik = 0

while start <= stop:
    print(start)
    schetchik+=1
    start+=1
print('-----------------')
print(schetchik)
    

