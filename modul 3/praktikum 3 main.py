# Parent class
class Hero:
    def __init__(self,name,health):
        # Constructor parent menangani penyimpanan health
        self.name = name          # <-- seharusnya ada ini agar tidak error
        self.health = health

    def showInfo(self):
        # Method untuk menampilkan info hero dari parent
        print("showInfo di class Hero")
        print("{} health: {}".format(
            self.name,
            self.health
        ))


# Subclass Intelligent
class Hero_intelligent(Hero):
    def __init__(self,name):
        # Panggil constructor parent dengan health = 100
        super().__init__(name,100)

    # Override method showInfo()
    def showInfo(self):
        print("showInfo di subclass Hero_intelligent")
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(
            self.name,
            self.health
        ))


# Subclass Strength
class Hero_strength(Hero):
    def __init__(self,name):
        # Panggil parent constructor dengan health = 200
        super().__init__(name,200)


# Membuat objek
lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

# Memanggil method override
lina.showInfo()
