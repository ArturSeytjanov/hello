
#1
'''fruits = ['alma','almurt','banan','baklajan','pomidor','qiyar']
vegetables = []
fruits.remove('baklajan')
fruits.remove('pomidor')
fruits.remove('qiyar')
vegetables.append('baklajan')
vegetables.append('pomidor')
vegetables.append('qiyar')
print(fruits , vegetables)'''
#2
'''numbers = []
for x in range(1,51):
    numbers.append(x)
print(numbers)
numbers.append('Artur')
print(numbers)
numbers.insert(0,'Dastan')
print(numbers)'''
#3
'''num = [x for x in range(1,11)]
print(num)
num.pop(-1)
print(num)
'''
#4
'''names = ['McGregor','Muhammed Ali','Tyson']
names.pop(0)
names.insert(0,'Khabib')
print(names)'''
#5
'''
tovar_1 = ['alma','banan','qiyar','grechka']
tovar_2 = ['kartoshka','pomidor','ananas','kivi']
all_tovar = tovar_1+tovar_2
print(all_tovar)'''
#6
'''nums_3 = []
for x in range(1,101):
    if x % 2 == 0:
        nums_3.append(x)
print(nums_3)'''
#7
'''numbers = [1,1,1,2,2,3,3,3,4,4]
nums = []
for x in numbers:
    if x not in nums:
        nums.append(x)
print(nums)'''
#17
'''nums = []
for x in range(101):
    nums.append(0)
print(nums)
nums.insert(0,1)
nums.append(1)
print(nums)'''

'''user = input('type... - ')
user_list = user.split(' ')
hashtag = '#'
for word in user_list:
    hashtag+=word.capitalize()
print(hashtag)'''

'''magazin = ['nan','kartoshka','alma']
satip_alindi = ['shokalad','kola','alma']
for x , j in zip(magazin,satip_alindi):
    if x == j:
        satip_alindi.remove(x)
        magazin.remove(j)
print(satip_alindi,magazin)'''

'''numbers = [[1,2,3],[4,5,6],[7,8,9]]
for x  in numbers:
    for j in x:
        print(j,end='')
        print()
print(numbers)'''

nums=[]
nums.append('Alma')
nums.append('Banan')
nums.append('Almurt')
print(nums)