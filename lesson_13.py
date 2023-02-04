#while
'''start = 0
stop = 10
while start <= stop:
    print(start)
    start+=1'''
#for

'''for x in range(0,11):
    pritn(x)'''

#1 for
'''word = 'hello world'
for letter in word:
    print(letter)'''

'''#2 while
word = 'hello world'
start = 0
stop = len(word)
while start<=stop:
    print(word[start])
    start+=1'''

#range() - araliq

'''for x in range(1,11,2):
    print(x)'''

'''start = int(input('start = '))
stop = int(input('stop = '))
for x in range(start,stop):
    print(x)'''

#2
'''for x in range(1,31):
    if x % 2==0:
        print(x)'''
#3
'''for x in range(1,31):
    if x == 10 or x == 20 or x == 30:
        print(x)'''
#4
'''for x in range(50):
    print(x)'''
#5
'''start = int(input('start = '))
stop = int(input('start = '))
step = int(input('step = '))
for x in range(start,stop-1,step):
    print(x)'''

#6
'''names = 'Azamat,Artur,Mirzabek,diana,Maman,Jurabek,Rufat,Muxammedali,Hakimbek'.split(',')
user = input('type your friends name for searching -  ')
for x in names:
    if user == x:
        print('We get this contact !'x)'''

# oyin islew
'''import cowsay
stop = int(input('stop = '))
for x in range(stop):
    user = input('type animals name - ')
    if user == 'daemon':
        print(cowsay.daemon(hi))
    elif user == 'pig':
        print(cowsay.pig('hi'))'''