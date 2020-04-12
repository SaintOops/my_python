class Player:
    def __init__(self, name = "Unknown"):
        self._name = name
        self.__x = 0 
        self.__y = 0
        self.__rigth_hand = "fist" 
        self.__left_hand = "fist" 
        self.__boost_coeff = 1 
        print(f"Player {self._name} connected to the game")
        
    def move(self, x = 0, y = 0): # x,y - то на сколько игрок хочет переместить своего персонажа
        self.__x += x*self.__boost_coeff # следует учитывать текущий boost-коэфицент(иначе можно перескочить/недойти)
        self.__y += y*self.__boost_coeff
        print(f"{self._name} relocated to the point ({self.__x},{self.__y})")
        
    def pick(self, item):
        if item == "gun": 
            self.__rigth_hand = item # в правую руку всегда бертся оружие("gun" - тип предмета)
            print(f"{self._name} took {self.__rigth_hand} in the right hand")
        else:
            self.__left_hand = item # в левую руку всегда бертся все осальное("boost" - тип предмета)
            print(f"{self._name} took a {self.__left_hand} in the left hand")
            
    def shoot(self):
        print(f"{self._name} shot a {self.__rigth_hand}") # если в правой руке ничего нет, то по умолчанию персонаж бьет кулаком
    
    def use(self): 
        
        if self.__left_hand == "speed boost up": # от типа буста(всего 2) зависит boost-коэфицент
            self.__boost_coeff = 2
            self.__left_hand = "fist" # после использования boost'а предмет(boost) обнуляется
            print(f"{self._name} used a {boost} and became faster")
            
        if self.__left_hand == "speed boost down": #
            self.__boost_coeff = 1/2
            self.__left_hand = "fist"
            print(f"{self._name} used a {boost} and became slower")

class IronMan(Player):
    def __init__(self, name = "Unknown IronMan"):
        Player.__init__(self, name = name)
        self.__fly_boost_coeff = 10 # для летающих персонажей boost-коэфицент всегда - 10
        self.__x = 0 
        self.__y = 0
        
    def fly(self, x = 0, y = 0):
        self.__x += x*self.__fly_boost_coeff
        self.__y += y*self.__fly_boost_coeff
        print(f"{self._name} relocated to the point ({self.__x},{self.__y})")


pl1 = Player('Rembo')
pl1.pick("gun")
pl1.move(5,10)
pl1.pick("speed boost up")
pl1.move(5,10)
pl1.shoot()
pl2 = IronMan('Tony')
pl2.move(5,10)
pl2.fly(5,10)
