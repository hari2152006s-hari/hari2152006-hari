#dice roling game

class dice_roling_game:
    def __init__(self):
        self.roll = ""

    def roll_dice(self):
        import random
        runing = True

        while runing:
            self.roll =input("roll your dice(y/n)")

            if self.roll == "y":
                roll1 = random.randint(10,60)
                print(roll1)
            elif self.roll == "n":
                print("thank you bye")
                break
            else:
                print("please enter y or n")


roll2=dice_roling_game()
roll2.roll_dice()





