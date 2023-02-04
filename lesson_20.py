'''#dictionary - so'zlik
#get()
#syntax {key:value,key2:value2}'''
#information = {'Kaxarman':'+998909599090','Nurlibay':'+998909999999'}
#user = input('type name - ')
#print(information[user])
#print(information.get(user))
#keys()

#print(information.keys()) # spiskide barlardi shigaradi
#print(information.values()) # nomerdi shigaradi
#print(information.items())

#information = {'Kaxarman':'+998905909090','Nurlibay':'+998999900909'}
'''numbers = {x:x**2 for x in range(1,11)}
print(numbers[5]) # sanlardin kvadratin shigaradi'''
#########################################
'''stop = int(input('stop = '))
key = input('key = ')
value = input('value = ')
information = {}
for x in range(stop):
    key = input('key = ')
    value = input('value = ')
    information[key] = value
print(information)'''
##################################################
'''countries = {
    'USA':{'Was there':['New York','Los Angeles'],'Was not there':['Chicago','Detroid','Boston','Harizona']},
    'Russian':{'Was there':['Moskva','Peterburg'],'Was not there':['Ekaterinburg','Volgograd']},
}
country = input('type a country name - ')
there = input('type what you wanna see - ')

print(countries[country][there])'''

###############################################

information = {'Kaxarman':'+998905909090','Nurlibay':'+998999997777','Artur':'+11111111','Hakimbek':'+22222'}
for x,j in zip(information.keys(),information.values()):
    print(f'name : {x},phone_number : {j}')
for x in information.items():
    print(x)