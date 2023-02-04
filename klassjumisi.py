ulken = lambda a,b,c,d: a if a>b>c>d else b and a if a>c>b>d else c and a if a>c>d>b else c and a if a>d>b>c else d and b if b>c>d>a else c and b if b>d>c>a else d and b if b>a>c>d else a and  c if c>d>a>b else d and c if c>a>b>d else a and c if c>b>a>d else c if c>b>d>a else b and d if d>a>b>c else a and d if d>c>b>a else c and d if d>c>a>b else c and d if d>b>a>c else b and d if d>b>c>a else b and d if d>c>a>b else c and d if d>c>b>a else c
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
print(ulken(a,b,c,d))