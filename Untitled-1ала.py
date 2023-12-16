class players:
    def __init__(self, age, height, weight, speed):
        #аргументи
        self.age = age
        self.height = height
        self.weight = weight
        self.speed = speed
        
    def setings(self):#setings звертається до аргументів
        print(f'його вік {self.age} років, його ріст {self.height} см, його вага {self.weight} кг, його швидкість {self.speed} км/год')
#init ініціалізація
class players_1(players):
    def __init__(self, age, height, weight, speed, defence):
        super().__init__(age, height, weight, speed)
        self.defence = defence
    
    def setings(self):
        print(f'його вік {self.age} років, його ріст {self.height} см, його вага {self.weight} кг, його швидкість {self.speed} км/год, його захист {self.defence} гравців')
class players_2(players):
    pass
#pass нічого

class players_gp(players):  
    def __init__(self, age, height, weight, speed, gp_rating):
        super().__init__(age, height, weight, speed)
        self.gp_rating = gp_rating
    
    def setings(self):
        print(f'його вік {self.age} років, його ріст {self.height} см, його вага {self.weight} кг, його швидкість {self.speed} км/год, його рейтинг gp {self.gp_rating}')


p1 = players_1('20', '180', '75', '33', '8/10')
p1.setings()

p2 = players_2('19', '174', '60', '34')
p2.setings()

gp_player = players_gp('22', '185', '80', '30', '9/10')
gp_player.setings()
# наслідування

