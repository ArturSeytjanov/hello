#magliwmatlar turleri
#int()-integer-целые число-1,2,3,4,-1,-5....
#float()-float-utir sanlar-1.2,21.4,3.14,3
#bool()-boolean-logikaliqmagliwmatlar turi - True , False
#str() - string - qatar(jaziw) - '1','Hello world',"it's me",'''Hello world'''
'''
a='Maykl'
b=' Jekson '
print(a+b)

num_1='5'
num_2='5'
print(num_1)
print(type(num_1))
print(a+b)

print(int(num_1)+int(num_2)) #int()-
a=5.5 #float-utir sanlar
print(type(a))

1-masele
#
type_1=1             #integer
type_2='Hello world' #string
type_3=True          #boolean
type_4=3.14          #float

print(type(type_1),type(type_2),type(type_3),type(type_4))
#
#float-float()
#integer-int()
#boolean-bool()
#string-str()

#boolean - логически тип данных
a=10
b=10

#

print(a>b)
print('------------')
print(a<b)


# == - tenlikti tekseriw ushin.
# != - ten emesligin tekseredi
# >= - ulken yamasa ten
# <= - kishi yamasa ten
print(a != b)
print(a == b)
print(d == c)
print(d != c)
print('--------------')

name = input("Atin'izd kiritin' : ")
print(name.capitalize()) #capitalize-birinshi haripti ulkeytedi
print(name.upper()) # upper-hamme haripti ulkeytip beredi
print(name.lower()) # lower-hamme haripti kishireytedi
print(name.title()) #title-haripti tuwrilap birinshi sozdin haribin ulkeytedi
print(name.count('a')) #count-a degen hariptin neshew ekenin tawip beredi

a = 'Ra$ul'
print(a.replace('$' , 's'))

name=input('atindi jaz : ')
print(name.strip('_-,.=+')) # strip - eki qaptaldagi zattin alip taslaydi

text = 'Hello World'
print(text[0])

text = 'Hello World'
print(text[-3])
'''
user = input('напишите что нибудь - ').lower()
print(user)
print(user[::-1] == user)

