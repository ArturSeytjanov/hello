#classes - klaslar
'''class Telephone:
    name = 'Samsung'
print(Telephone.name)'''# - attirirbute

class Telephone:
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
redmi = Telephone(marka = 'Redmi 12 ultra',cena = '1500$',camera = '120mp',storage = '512')
print(redmi.show_info())

Iphone = Telephone(marka = 'iphone 14 pro max ',cena = '2000$',camera = '60mp',storage = '1tb')
