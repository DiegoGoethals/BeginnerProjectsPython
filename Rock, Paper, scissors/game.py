import random


class Game():

    def __init__(self, moves=3):

        self.moves = moves
        self.score = (0, 0)
        self.winner = None
        self.running = True
        self.run()

    def move(self):

        player_move = input("Rock, paper, scissors: ")
        cpu_move = random.choice(["rock", "paper", "scissor"])
        if (player_move == "rock" and cpu_move == "scissor") or (player_move == "paper" and cpu_move == "rock")\
                or (player_move == "scissor" and cpu_move == "paper"):
            print("cpu chose " + cpu_move)
            self.score = (self.score[0] + 1, self.score[1])
            print("player wins this one")
        if (player_move == "rock" and cpu_move == "paper") or (player_move == "paper" and cpu_move == "scissor")\
                or (player_move == "scissor" and cpu_move == "rock"):
            print("cpu chose " + cpu_move)
            self.score = (self.score[0], self.score[1] + 1)
            print("cpu wins this one")
        if player_move == cpu_move:
            print("cpu chose " + cpu_move)
            print("You both chose the same, play again")
        self.check_win()

    def show_score(self):
        print("Player score: ({})".format(self.score[0]))
        print("Cpu score: ({})".format(self.score[1]))

    def check_win(self):
        if self.score[0] >= self.moves // 2 + 1:
            self.winner = "Player"
            self.running = False
            print("Congratulations you win")
        if self.score[1] >= self.moves // 2 + 1:
            self.winner = "cpu"
            self.running = False
            print("Too bad, you lost")

    def play_again(self):
        answer = input("Would you like to play again? y/n: ")
        if answer == "y" or answer == "":
            self.__init__()

    def run(self):

        while self.running:
            self.move()
            self.show_score()
        self.play_again()


game = Game()
