class Hero:
    __jumlah = 0

    def _init_(self, name, health, attPower, armor):
    
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0
        self._healthMax = self.healthStandar * self._level
        self._attPower = self.attPowerStandar * self._level
        self._armor = self.armorStandar * self._level
        self._health = self._healthMax

        Hero.__jumlah += 1  

    @property
    def gainEXP(self):
     pass

    gainEXP.setter
    def gainEXP(self, addEXP):
        self.__exp += addEXP
       
        while self.__exp >= 100:
            print(f"{self.__name} level up")
            self.__level += 1
            self.__exp -= 100

            self._healthMax = self.healthStandar * self._level
            self._attPower = self.attPowerStandar * self._level
            self._armor = self.armorStandar * self._level
            self._health = self._healthMax

    def attack(self, musuh):
        self.gainEXP = 50

    @property
    def info(self):
        return f"{self._name} level {self._level}: \n" \
               f"\thealth = {self._health}/{self._healthMax} \n" \
               f"\tattack = {self.__attPower} \n" \
               f"\tarmor = {self.__armor}"
    
    slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)

print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print(slardar.info)