#Alexander Mejia 
#QCC ID:24588520

import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


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
        elif total in [2, 3, 12]:
            return "Lose"
        else:
            return


def main():
    game = DiceGame()

    while True:
        print("\nDice Roll And find out Simulator")
        print("1. Bet on a round")
        print("2. Quit before winning")

        choice = input("Choose an option: ")

        if choice == "1":
            result = game.play_round()
            print(f"\nYou rolled: {result['die1']} and {result['die2']}")
            print(f"Total: {result['total']}")
            print(f"Result: {result['result']}")
        elif choice == "2":
            print("Thank you for playing! Come back soon.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()