import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.game_is_on = True

    def print_score(self):
        if self.game_is_on:
            self.write('olala')
        else:
            self.write('Game Over!')

    def game_over(self):
        self.game_is_on = False
