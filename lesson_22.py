'''TEMA - definition'''
''' def - aniqlastiriw'''
############################
'''b = 'Hello world'
schetchik = 0
for x in b:
    schetchik+=1
print(schetchik)'''
#############################
'''b = 'Hello world'
def dlina(b):
    schetchik = 0
    for x in b:
        schetchik+=1
    print(schetchik)
dlina(b)
c = 'qwerty'
dlina(c)

d = 'awa'
dlina(d)'''
#############################
'''def sayhello():
    return 'hello world'
def sayhi():
    print('hi')
sayhi()
print(sayhello())'''
#############################
'''def primougolnik(a,b):
    s = a*b
    p = (a+b)*2
    return s,p
print(primougolnik(7,5))
'''
#############################
a =[1,2,3,4,5,100,6,7,8]
def maximum(a):
    number = 0
    for x in a:
        if number<x:
            number=x
    return 'maximal number is ' , number
print(max(a))
    