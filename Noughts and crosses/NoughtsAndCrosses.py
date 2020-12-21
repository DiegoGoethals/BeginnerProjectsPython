import random


# class which represents the game
class Game:

    # initializes everything needed to start a game
    def __init__(self, player_one="X", player_two="O"):
        self.player_one = player_one
        self.player_two = player_two

        # initializes the board so the game can be played
        self.board = [
            [".", ".", "."],
            [".", ".", "."],
            [".", ".", "."]
        ]

        # sets active player for the game
        self.active_player = random.choice([self.player_one, self.player_two])

        # sets winner of the game
        self.winner = ""

        self.countmove = 0

        # starts running the game
        self.running = True
        self.run_game()

    # shows the board
    def show_board(self):
        for row in self.board:
            row_string = ""
            for cell in row:
                row_string = "{} {} ".format(row_string, cell)
            print(row_string)

    def move(self):
        input_data = input("Player ({}) please choose a Column and a Row: ".format(self.active_player))

        row, column = input_data.split(" ")
        if self.board[int(row) - 1][int(column) - 1] == ".":
            self.board[int(row) - 1][int(column) - 1] = self.active_player

            # Did they win?
            self.check_win()

            # change players if there is no winner yet
            if self.active_player == self.player_one:
                self.active_player = self.player_two
            else:
                self.active_player = self.player_one

            self.countmove += 1
        else:
            print("This cell is already selected, please choose a valid one")

    def check_win(self):
        combinations = [
            # horizontal
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # vertical
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # crossed
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)]
        ]

        for coordinates in combinations:
            letters = [self.board[x][y] for x, y in coordinates]

            # If all the letters match
            if "." not in letters:
                if len(set(letters)) <= 1:
                    # returns corresponding letter for winner (X/O)
                    print("Well done {}!  You won the game!".format(self.active_player))
                    self.winner = self.active_player
                    self.running = False
                    return True
        return False

    def board_full(self):
        if self.countmove == 9 and self.winner == "":
            print("The game is a draw :( ")

            # Stop the game
            self.running = False

    def run_game(self):
        # While the game is not over
        while self.running:

            # Show the player the board
            self.show_board()

            self.move()

            self.board_full()

        # Print the winning game board
        self.show_board()


game = Game()