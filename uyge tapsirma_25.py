#1
'''list = [1,2,3,4,5,6,7,8,9,10]
list.reverse()
print(list)'''
#2
'''a =[45,86,17]
def maximum(a):
    number = 0
    for x in a:
        if number<x:
            number=x:
    return number
print(max(a))'''
#2
'''def maxim(a,b,c):
    if a>b>c:
        return a
    elif a>c>b:
        return a
    elif b>c>a:
        return b
    elif b>a>c:
        return b    
    elif c>a>b:
        return c
    elif c>b>a:
        return c
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
print(maxim(a,b,c))'''
#3
'''def satr(soz):
	schetchik = 0
	alfabit = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,y,x,z'.split(',')
	for harip in alfabit:
		if harip in soz:
			schetchik+=1
	if schetchik>=26:
		return True
	else:
		return False,schetchik
a = input('a = ').lower()
print(satr(a))'''
#4
'''def numebers(a,b,c):
    return max(a,b,c) , a+b+c ,a*b*c
print(numebers(1,2,3)) '''
#5

#8
'''a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
s = a+b+c
print(s)'''

#10
'''def artur(a,b):
    s = a**2
    p = b**2
    return s , p
print(artur(7,5))'''
