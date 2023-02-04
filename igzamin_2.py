#1
'''names = ['Artur']
print(names)
'''
#2
'''a = []
a.append('Jony')
print(a)'''
#3
'''names = ['Artur','Mirzabek','Azamat']
names.insert(3,'Dastan')
print(names)'''
#4
'''names = ['Artur','Mirzabek','Azamat','Hakimbek','Dilshod']
names.remove('Hakimbek')
print(names)
names.pop(-1)
print(names)'''
#5
'''num = [x for x in range(1,12)] #genarator
print(num)
num.pop(-1)
print(num)'''
#5
'''numbers = []
for x in range(1,11): #iterator
    numbers.append(x)
print(numbers)'''
#6 nin birinshisi variant
'''nums = []
for x in range(1,31):
    if x % 2 == 0:
        nums.append(x)

for x in range(1,31):
    if x % 2 == 1:
        nums.append(x)
print(nums)'''
#6 nin ekinshisi variant
'''nums = []
for x in range(1,31):
    if x % 2 == 0:
        nums.append(x)
print(nums)'''
#6 nin ekinshisi variant
'''nums_2 = []
for x in range(1,31):
    if x % 2 == 1:
        nums_2.append(x)
print(nums_2)
'''
#7
'''numbers = [1,2,3,4,5]
summa = 0
for x in numbers:
    summa+=x
print(summa)'''
#8
'''a = (1,1,1,1,2,2,2,2,3,3,3,4,4,4,4,5,5,5,5,6,7,7,8,9,9)
b = tuple(set(a))
print(b)
summa = 0
for x in b:
    if x % 2 == 1:
        summa+=x
print(summa)'''
#9
'''a = ('hello, world!')
print(tuple(a))'''
#10
'''num = '1, 3, 5, 3, 7'

dict = {x:num.count(x)for x in num}
print(dict)'''
#11
'''dict = ['Artur','Mirzabek','Azamat']
dict.append('Dilshod')
print(dict)'''
#12
'''empty_dict = {}
empty_dict['Azamat'] = '+998911010101'
empty_dict['Aza'] = '+998911010101'
empty_dict['Azat'] = '+998911010101'
keys = empty_dict.keys()
for x in keys:
    print(x)'''
#13
'''set = []
set.append('Artur')
print(set)'''
#14
'''a = {1,2,4,5,7,3}
b = {3,7,9,8,5,10,11}
print(a.intersection(b))'''
#15
'''a = {1,2,4,5,7,3}
b = {3,7,9,8,5,10,11}
c = {5,6,3,5,9,7}
print(a.intersection(b,c))'''
#15
'''a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = {5,6,7,8,9,10}
result = (a - b - c) | (c - b - a)
print(result)'''
#16
'''a = {1,2,3,4}
b = (4,5,6,7)
c = [6,7,8,9]
result = list(a) + list(b) + c
print(set(result))'''
#17
'''qaharmanlar = {
    'Xalk':{'qaharman':['Ol kushli ham jasil']},
    'Thor':{'qaharman':['Ol kushli ham Odennin balasi']},
}
qaharman_2 = input("Ati :  ")

print(qaharmanlar[qaharman_2]) '''
#18
'''mektepler = {
    'I.Yusupov':{'mektep':['Ol mektepte bilim ham jaqsi tarbiya bar, ol en kushli mektepler reytinginde turadi']},
    'Prezident':{'mektep':['Ol jerde bilim ham jaqsi tarbiya bar rawajlangan mektep , ol en kushli mektepler reytinginde turadi']},
}
mektep_1 = input("Ati :  ")

print(mektepler[mektep_1]) '''
#19
'''list_1 = [5,2,3,1,6,8,7,[[0,2,[21,'hello',12],3]]]
print(list_1)
print(list_1[3])
print(list_1[3][-1])
print(list_1[3][-1][3])
print(list_1[3][-1][3][3])

print(list_1[-1][-1][-1][-1])'''
#20
'''numbers = [x for x in range(1,11)]
numbers.sort()
print(numbers)'''
'''a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = {5,6,7,8,9,10}
result = (a - b - c) | (c - b - a)
print(result)'''

#17 
'''a = {'Hulk':'very strong and green','Thor':'Son of Oden'}
for x,j in zip(a.keys(),a.values()):
    print('names:',x,'(s)')'''