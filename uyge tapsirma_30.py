#1
"""class Telephone:
    def __init__(self,marka,cena,camera,storage):
        self.marka = marka
        self.cena = cena
        self.camera = camera
        self.storage = storage
    def show_info(self):
        return f'''
marka = {self.marka},
cena = {self.cena},
camera = {self.camera},
storage = {self.storage}.
'''
Iphone = Telephone(marka = 'iphone 14 pro max ',cena = '2000$',camera = '60mp',storage = '1tb')
print(Iphone.show_info())"""
#2
#3
#4
"""class Laptop:
    def __init__(self,marka,cena,storage,Full_HD):
        self.marka = marka
        self.cena = cena
        self.storage = storage
        self.Full_HD = Full_HD
    def show_info(self):
        return f'''
marka = {self.marka},
cena = {self.cena},
storage = {self.storage},
Full_HD = {self.Full_HD}.
'''
Macbook = Laptop(marka = 'Macbook Pro', cena = '2444$', storage = '512gb or 1Tb', Full_HD = '1920x1080')
print(Macbook.show_info())"""

#car-brend
class Car:
    def __init__(self,brend,year,cena):
        self.brend = brend
        self.year = year
        self.cena = cena
    def show_info(self):
        return f'''
    brend = {self.brend},
    year = {self.year},
    cena = {self.cena}.
    '''
Mercedes_Benz = Car(brend = 'Mercedes-Benz Vision EQXX', year = '2022', cena = '')