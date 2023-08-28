class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printinfo(self):
        print(self.name)
        print(self.age)
        
        if self.age >= 20:
            print("大人である")
        else:
            print("大人でない")
        
human1 = Human("椎野",25)
human2 = Human("沢田",19)
human3 = Human("石井",36)
human4 = Human("中本",15)

menber = [human1,human2,human3,human4]

for i in menber:
    i.printinfo()