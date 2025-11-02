#Alexander Mejia 
#QCC ID:24588520

 
import random

class Die:
    def __init__(self, sides=6):
        self.s = sides
        
        def roll(self):
            return random.randint(1, self.s)
       

class DiceGame:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

def play_round(self):
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()
        total = roll1 + roll2
        result = self.evaluate_roll(total)
        return {
            "die1": roll1,
            "die2": roll2,
            "total": total,
            "result": result
        }
    def evaluate_roll(self, total):
        if total in [7, 11]:
            return "Win"
        elif total in [2,3,12]