# continue
# def - definition - aniqlastiriw
'''def names(*args):
    for x in args:
        print(x)
names('Artur','Azamat','Rasul')
user = input('user = ')
names(user)'''
###########################
'''def summa(*args):
    summa = 0
    for x in args:
        summa+=x
    return summa 
print(summa(1,2,3,4,5,6,7,8,9))
print(summa(1,2))''' '''*args - tuple qilip beredi'''
#############################
'''def nums(*args):
    return args
print(nums(1,2,3,4,4,6,3,2,1,4,2,45,3))'''
##############################
''' ** - kwargs - key qilip beredi'''
'''def names(**kwargs):
    return kwargs
print(names(a=1,b=2,c=3))'''

'''dict = {}
def names(*kwargs):
    stop = int(input('stop = '))
    key = input('key = ')
    value = input('value = ')
    information = {}
    for x in range(stop):
        key = input('key = ')
        value = input('value = ')
        information[key] = value
        print(information)'''

'''sozlik = {'Artur':1202838,'Azamat':1932049309,'Mirzabek':839175489}
for x in dict.sozlik():
    print(x)'''
########################
'''def names(a,b,c=5):
    return a,b,c
print(names(a=3,b=2,c=3))'''
#######################
#lambda functions
'''def name(a):
    return a*2
namme = lambda a:a*2
print(name('Mirzabek'))
print(namme('Rasul'))'''
###############################
#1
'''sanlar = lambda a : True if a%2==0 else False
print(sanlar(6))'''
#2
'''def artur(a):
    if a%2==0:
        return Jup san
    else:
        return Taq san
a = int(input('a = '))
print(artur(a))'''
##################
'''qosindi = lambda a,b: a+b
print(qosindi(1,2))'''
###################
'''ulken = lambda a,b: a if a>b else b
print(ulken(6,5))'''
###################
ulken = lambda a,b,c: a if a>b>c else b and a if a>c>b else c and b if b>c>a else c and b if b>a>c else a and c if c>a>b else a and c if c>b>a else b
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print(ulken(a,b,c))