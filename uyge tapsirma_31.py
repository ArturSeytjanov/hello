#1
"""class Home:
    def __init__(self,street,floor,rooms,cena):
        self.street = street
        self.floor = floor
        self.rooms = rooms
        self.cena = cena
    def show_info(self):
        return f'''
street = {self.street},
floor = {self.floor},
rooms = {self.rooms},
cena = {self.cena}.
'''
House = Home(street = 'Located on Peterson Street',floor = '2 floor',rooms = '10 rooms',cena = '10,000$')
print(House.show_info())"""
#2
"""class Car:
    def __init__(self,marka,year,cena,brend):
        self.marka = marka
        self.year = year
        self.cena = cena
        self.brend = brend
    def show_info(self):
        return f'''
    marka = {self.marka},
    year = {self.year},
    cena = {self.cena},
    brend = {self.brend}
    '''
Mercedes_Benz = Car(marka = 'Mercedes-Benz Vision EQXX', year = '2022', cena = ' 140 000$',brend = 'Mersedes-benz')
print(Mercedes_Benz.show_info())

class Motorbike(Car):
    def __init__(self,marka,year,cena,brend):
        
        super().__init__(marka,year,cena,brend)
        def show_info(self):
            return '''
marka= {0},
year = {1},
cena = {2},
brend = {3},

'''.format(self.marka,self.year,self.cena,self.brend)

MV_Augusta_F3_800= Motorbike(
	marka='MV Augusta F3 800',
	year = '2020',
    cena = '32158,88$',
    brend = 'Mersedes-benz'

	)
print( MV_Augusta_F3_800.show_info())"""
