import random

list_names = ['Spiderman','Ironman','hulk','Thor','Thanos','Venom']
name = random.choice(list_names)
print(name,len(name))
symbols = ['*' for i in range(len(name))]
print(symbols,len(symbols))
user = input('type a letter - ')
if user in name:
    index = name.index(user)
    print(index)
    symbols.pop(index)
    symbols.insert(index,user)
print(''.join(symbols))

'''import random
numbers = [x for x in range(1,11)]
random.shuffle(numbers)
print(numbers)
numbers.sort()
print(numbers)
print(numbers[-1],numbers.index(numbers[-1]))'''

'''
#tuple and set - izbe izlik ham koplik

#tuple - izbe izlik - кортеж
# max()-maximum , min()-minimum , sum()
numbers = (1,2,3,4,5,1,33,4,) # - en' u'lken sandi shig'arip beredi
print(max(numbers))
numbers = [1,2,4,5,6,7,3]
print(sum(numbers))

#set() - koplik
numbers = [1,1,2,3,4,2,2,4,6,5,]
print(list(set(numbers)))
a = {1,2,4,5,7,3}
b = {3,7,9,8,5,10,11}
print(a.intersection(b)) -# ekewinde bar elementlerdi ekranga shigaradi
print(a.add(b)) 
print(a.union(b))
print(a.difference(b))
print(b.difference(a))'''