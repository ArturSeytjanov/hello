'''#1
tovarlar = {
    'Bazar':{'satip alingan':['Produkti','kiyimler'],'Satip aliw kerek':['Игружки','Ochkiy','Kepka',"Sag'at"]},
    'Magazin':{'Satip alingan':['Moloko','Tort'],'Satip aliw kerek ':['Kola','Pepsi','Shokolad']},
}
tovar= input('Bazar yamasa Magazin - ')
there = input("Satip aling'an zatlar yamasa satip aliw kerek zatlar - ")

print(tovarlar[tovar][there]) '''

#2
'''a = int(input('a = '))
numbers={x:x for x in range(a)}
print(list[numbers])'''

tovarlar = {
    'Bazar':{'tovari':['Kartoshka , bahasi':'1000'],'tovari':['Piyaz,bahasi':'2000']}
}
tovar= input('Bazar di jaz - ')

print(tovarlar[tovar])

