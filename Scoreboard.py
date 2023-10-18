from constants import screensize
from SessionController import SessionController
import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.ht()
        self.speed_level = 1 
        self.highscore = SessionController.read_highscore()
        self.on_restart()
        
    def draw_score(self): 
        self.setpos(screensize[0] / 2.5, screensize[1] / 2.5)
        self.color('black')
        self.write(f'{self.score}', align="right", font=('Arial', 40, 'normal'))

        self.setpos(screensize[0] / 2.5, screensize[1] / 2.7)
        self.write(f'level: {self.speed_level + 1}', align="right", font=('Arial', 12, 'normal')) # +1 because of floor value 

        self.setpos(screensize[0] / 2.35, screensize[1] / 2.5)
        self.color('red')
        self.write(f'/{self.highscore}', align="center", font=('Arial', 20, 'normal'))

    def draw(self):
        if self.game_is_on:
            self.clear()
            
            self.draw_score()
            self.draw_legend()
        else:
            self.on_game_over()

    def draw_legend(self):
        self.color('black')
        self.setpos(-screensize[0] / 2.2, screensize[1] / 2.4)
        self.write('LMB: pause toggle', align="left", font=('Arial', 12, 'normal'))
     
    def draw_game_over(self):
        self.setpos(0, screensize[1] / 3)
        self.color('black')
        self.write('Game over!', align="center", font=('Arial', 50, 'normal'))
        self.setpos(0, screensize[1] / 5.5)
        self.write(f'Score: {self.score}', align="center", font=('Arial', 40, 'normal'))

        self.setpos(-screensize[0] / 2.2, screensize[1] / 2.65)
        self.write(f'RMB: restart', align="left", font=('Arial', 12, 'normal'))

    def add_score(self):
        self.score += 1

    def set_speed_level(self, speed_level):
        self.speed_level = speed_level

    def get_score(self):
        return self.score

    def game_over(self):
        self.game_is_on = False

    def on_game_over(self):
        self.clear()
        self.write_session()
        self.draw_game_over()

    def on_restart(self):
        self.score = 0
        self.game_is_on = True
        self.highscore = SessionController.read_highscore()
        self.draw()

    def write_session(self):
        SessionController.write_session(self.score)
