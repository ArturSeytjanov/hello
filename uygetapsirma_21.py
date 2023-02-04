'''Tovarlar = {
    'Bazar':{'satip alingan':['Produkti','kiyimler'],'Satip aliw kerek':['Игружки','Ochkiy','Kepka',"Sag'at"]},
    'Magazin':{'Satip alingan':['Moloko','Tort'],'Satip aliw kerek ':['Kola','Pepsi','Shokolad']},
}
tovar= input('Bazar yamasa Magazin - ')
there = input("Satip aling'an zatlar yamasa satip aliw kerek zatlar - ")

print(Tovarlar[tovar][there])'''
#2
'''list = []
numbers = {x:x for x in list}
print(numbers[list])'''

'''a = ['111222000355222244']
dict = []'''
#3
'''num = '111222000355222244'

dict = {x:num.count(x)for x in num}
print(dict)'''

#4
'''a = ['A','E','I','O','U','L','N','S','T','R']#1ball
b = ['D','G']#2ball
c = ['B', 'C', 'M', 'P']#3ball
d = ['F', 'H', 'V', 'W', 'Y' ]#4ball
e = ['K']#5ball
f = ['J','X']#8ball
g = ['Q','Z']#10ball
ball = 0
user = input('type a word - ').upper()
for x in user:
    if x in a:
        ball+=1
    if x in b:
        ball+=2
    if x in c:
        ball+=3
    if x in d:
        ball+=4
    if x in e:
        ball+=5
    if x in f:
        ball+=8
    if x in g:
        ball+=10
print(ball)'''