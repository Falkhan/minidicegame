import random
import sys
class Game:
    def __init__(self,money):
        self.money = money
        print("Welcome to Falkhan's Gambling Emporium! Here you can play dice", "Bet a number and if it appears on a dice, you win two times the bet!")
        print("At the beginning you'll get %s$! Enjoy" % self.money)
        self.initialize_game()
    def initialize_game(self):
        if(self.money == 0):
            print("Sorry, but you've lost everything! Come back soon!")
            sys.exit(0)
        will = input('You have %s$. Do you want to play? (Y/N)' % self.money)
        if will.lower() == "y":
            self.game()
        elif will.lower() =="n":
            print("That's fine. Thank you for coming. Bye!")
            sys.exit(0)
        else:
            self.initialize_game()
    def game(self):
            bet = int(input("Brilliant. How much do you want to bet?"))
            # Checking if the bet is larger than
            while bet > self.money or bet < 0:
                bet = int(input("Please type in a correct amount of money."))
            number = int(input("Great, what number are you betting on?"))
            # Checking if number is in the 1-6 range
            while number not in list(range(1,6)):
                number = int(input("You can't bet on a number that is not on a 6-sided die!"))
            print("Wonderful! LET'S ROLL!")
            if self.roll(bet, number):
                print("Congratulations! You've won %s$!!!", bet*2)
                self.money += bet * 2
            else:
                print("Sorry, you've lost your bet!")
                self.money -= bet if self.money - bet >= 0 else self.money == 0
            self.initialize_game()
    def roll(self, bet, betnum):
        die = random.randrange(1,6)
        print("You betted %s on number %s. And the dice shows the number... %s!!" % (bet, betnum, die))
        return betnum == die

new_game = Game(20)
