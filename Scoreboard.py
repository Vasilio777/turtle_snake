import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self, screensize):
        super().__init__()
        self.up()
        self.ht()
        self.screensize = screensize
        self.setpos(0, self.screensize[1] / 2.5)
        self.game_is_on = True
        self.score = 0

    def print_score(self):
        if self.game_is_on:
            self.clear()
            self.write(f'{self.score}', align="center", font=('Arial', 40, 'normal'))
        else:
            self.game_over()

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.game_is_on = False
        self.clear()
        self.setpos(0, self.screensize[1] / 3)
        self.write('Game over!', align="center", font=('Arial', 50, 'normal'))
        self.setpos(0, self.screensize[1] / 5.5)
        self.write(f'Score: {self.score}', align="center", font=('Arial', 40, 'normal'))
