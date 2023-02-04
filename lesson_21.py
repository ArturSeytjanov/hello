#1
stop = int(input('stop = '))
key = input('key = ')
value = input('value = ')
information = {}
for x in range(stop):
    key = input('key = ')
    value = input('value = ')
    information[key] = value
print(information)
#2
'''stop = 0
key = input('key = ')
value_1= 'Steve Jobs'
value_2 = 'Mark Sukerberg'
information_1= {'Steve Jobs 24-fevral 1955-jil https://www.apple.com/'}
information_2= { 'Mark Sukerberg 14-may 1984-jil https://www.facebook.com/'}
for x in range(stop):
    information_1,[key] = value_1
    information_2,[key] = value_2
print(information_1 , information_2) '''
#3
'''empty_dict = {}
empty_dict['Azamat'] = '+998911010101'
empty_dict['Aza'] = '+998911010101'
empty_dict['Azat'] = '+998911010101'
keys = empty_dict.keys()
for x in keys:
    print(x)'''
#4
''''''
#5
'''stop = 0
key = 'Mektep mugallimleri'
value = ()
information = {"Mektep mug'allimleri jaqsi , mektepte ko'binshe hayal-qizlar mug'allim boladi"}
for x in range(stop):
    information[key] = value
print(information)'''
#6
'''number = int(input('numbers = '))
dict = {x:x**2 for x in range(1,100)}
print(dict[number])'''
#7
'''dict = ['Artur','Mirzabek','Azamat']
print(dict.clear)'''
#8
'''tovarlar = {
    'Bazar':{'satip alingan':['Produkti','kiyimler'],'Satip aliw kerek':['Игружки','Ochkiy','Kepka',"Sag'at"]},
    'Magazin':{'Satip alingan':['Moloko','Tort'],'Satip aliw kerek ':['Kola','Pepsi','Shokolad']},
}
tovar= input('Bazar yamasa Magazin - ')
there = input("Satip aling'an zatlar yamasa satip aliw kerek zatlar - ")

print(tovarlar[tovar][there])'''

#11111111111111111111111111
'''numbers = [0,1,0,0,3,4,5,0,7,0]
new_numbers = []
schetchik = 0
for x in numbers:
    if x != 0:
        new_numbers.append(x)
    else:
        schetchik+=1
print(new_numbers)
for x in range(schetchik):
    new_numbers.append(0)
print(new_numbers)'''