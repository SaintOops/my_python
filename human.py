class Human:
    def __init__(self, name = "Nemo"):
        self._name = name
        print(f"{self._name} was born!")
        self.__age = 0
    
    def eating(self):
        print(f"{self._name} is eating")   

    def sleeping(self):
        print(f"{self._name} is sleeping")

    def working(self):
        if 18 <= self.__age < 65:
            print(f"{self._name} is working")
        if self.__age >= 65:
            print(f"{self._name} is on retirement")
    
    def relaxing(self):
        print(f"{self._name} is relaxing")

    def growing(self):
        print(f"{self._name} is growing")
        self.__age += 1

class Life:
    def life(self, human, years=70):
        while years:            
            human.growing()
            human.eating()
            human.sleeping()
            human.working()
            human.relaxing()
            years -= 1

arny = Human('Arnold')
life_arny = Life()
life_arny.life(arny)
