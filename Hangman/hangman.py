import string
import random
import re


class Game:

    def __init__(self):
        # Sets word chosen by players as word to guess
        word = input("Choose word to guess please: ")
        self.word = word

        # Shows how many letters have to be guessed by players and are already guessed
        self.progress = "."*len(self.word)

        # Generates a random code so other players can actually join the game to try and guess the word
        self.code = ''.join(random.choice(string.ascii_letters) for _ in range(8))

        # Initializes how many mistakes can be made and will diminish every time someone guesses wrong
        self.mistakes_left = 10

        # Initializes the collection of already guessed letters, right and wrong
        self.selected = []

        # Obviously creates an empty winner slot
        self.winner = None

        self.running = True
        self.run_game()

    # Enables the players to guess a letter
    def guess(self):
        letter = input("Please guess a letter: ")
        if letter in self.selected:
            print("This letter was already chosen before, please try another one")
            return False
        self.selected.append(letter)
        if letter not in self.word:
            self.mistakes_left -= 1
            print("This letter is not in the word. You have ({}) wrong tries left.".format(self.mistakes_left))
        else:
            matches = []
            for match in re.finditer(letter, self.word):
                matches.append(match.start())
            for match in matches:
                self.progress = self.progress[:match] + letter + self.progress[match + 1:]
        self.check_win()
        self.show_progress()

    # Checks if the game is done and if so who won, the hanger or the guessers
    def check_win(self):
        if self.mistakes_left == 0:
            self.winner = "Hanger"
            print("Congratulations hanger, you won")
            self.running = False
        if self.progress == self.word:
            self.winner = "Guesser"
            print("Congratulations guesser, you won")
            self.running = False

    def show_progress(self):
        print(self.progress)

    def show_selected(self):
        print("You've already guessed these letters: ({})".format(self.selected))

    def play_again(self):
        answer = input("Would you like to play again? y/n: ")
        if answer == "y" or answer == "":
            self.__init__()

    def run_game(self):
        self.show_progress()
        # While the game is not over
        while self.running:
            self.show_selected()
            self.guess()
        self.play_again()