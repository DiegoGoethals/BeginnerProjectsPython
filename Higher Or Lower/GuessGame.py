import random


class Game:

    def __init__(self):

        range_of_numbers = input("Between what numbers would you like to guess? ")
        self.low_border, self.high_border = range_of_numbers.split(" ")
        numbers_to_choose = []
        for i in range(int(self.low_border), int(self.high_border) + 1):
            numbers_to_choose.append(i)
        self.number = random.choice(numbers_to_choose)
        self.guesses = 0
        self.running = True
        self.run()

    def guess(self):
        number = int(input("What number would you like to guess? "))
        if number < int(self.low_border) or number > int(self.high_border):
            print("Your number must be between " + self.low_border + " and " + self.high_border)
            return False
        self.guesses += 1
        if number == self.number:
            print("Congratulations, you win")
            self.running = False
        if number < self.number:
            print("Your number is too low, guess a higher one")
        if number > self.number:
            print("Your number is too high, guess another one")
        print("You've already guessed ({}) times".format(self.guesses))

    def play_again(self):
        answer = input("Would you like to play again? y/n: ")
        if answer == "y" or answer == "":
            self.__init__()

    def run(self):
        while self.running:
            self.guess()
        self.play_again()


game = Game()
