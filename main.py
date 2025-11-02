#Alexander Mejia 
#QCC ID:24588520

 
import random

class Die:
    def __init__(self, sides=6):
        self.s = sides
        
        def roll(self):
            return random.randint(1, self.s)
       

Class DiceGame:
    def__init_(self):
self.die1 = Die()
self.die2 = Die()

    def play_round(self):
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()
        