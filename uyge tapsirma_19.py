#19
#1
'''a = set() # iterator
for x in range(1,101):
    if x % 2==0:
        a.add(x)
print(a)'''
'''b = {x for x in range(2,101,2)}
print(b)'''
#2
'''set_a = {1,2,3,4,5,6}
set_b = {4,5,6,7,8,9,10}
print(set_a.difference(set_b))
print(set_a - set_b) #difference
print('-----------------------------')
print(set_a.intersection(set_b))
print(set_a & set_b) #intersection
print('-----------------------------')
print(set_a ^ set_b) #ekewinde jog'in shigarip beredi
print('-----------------------------')
print(set_a.union(set_b))
print(set_a | set_b) #union'''
#3
'''a = (1,2,3,3,6,7)
b = (7,8,9,4,3,2)
print(set(a+b))'''
#4
'''names = ['maftuna','aydin','artur','hakimbek','hakimbek','artur']
new_names = list(set(names))
result = []
for x in new_names:
    result.append(x.capitalize()) # title - capitalize ulken haripte shigaradi
print(result)'''
#5
'''numbers = [1,1,1,1,2,2,2,3,3,3,3,3,5,5,4,4,4]
numbers.sort()
new_numbers = (list(set(numbers)))
new_numbers.reverse()
print()'''
#6
'''numbers_1 = [1,2,4,5,7,3]
numbers_2 = [3,7,9,8,5,10]
print(tuple(numbers_1+numbers_2))'''

'''a = [1,2,3,4,5,5,5,5,6,6,6,7]
b = [4,4,4,4,5,5,5,5,6,6,6,6,7,8,9,10]
print(list(set(a + b)))'''
#6
'''a = [1,2,3,4,5,5,5,5,6,6,6,7]
b = [4,4,4,4,5,5,5,5,6,6,6,6,7,8,9,10]
a.extend(b)
c = list(set(a))
print(c)'''