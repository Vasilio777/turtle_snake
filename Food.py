import turtle
import random
import math

class Food(turtle.Turtle):
    def __init__(self, screensize, cell_size):
        super().__init__()
        self.up()
        self.ht()
        self.speed(0)
        max_x = screensize[0] / 2 - cell_size
        max_y = screensize[1] / 2 - cell_size
        self.setpos(random.randrange(-max_x, max_x, cell_size), random.randrange(-max_y, max_y, cell_size))
        self.color(random.choice(['blue', 'red', 'green', 'purple']))
        self.shape(name = random.choice(['circle', 'square', 'triangle']))
        self.st()
        self.collected = False

    def try_collect(self, snake_head_pos):
        if self.distance(snake_head_pos) < 1:
            self.collected = True
            self.ht()
    
    def render(self, snake_head_pos):
        if self.isvisible():
            self.try_collect(snake_head_pos)

    def on_restart(self):
        self.ht()
