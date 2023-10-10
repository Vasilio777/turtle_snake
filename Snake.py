import turtle
import random

class Snake():
    def __init__(self, step_size):
        super().__init__()
        self.step_size = step_size
        self.curr_h = 0
        # self.speed = 1
        
        self.body = []
        self.body_init_pos = [(i * step_size, 0) for i in range(4)]

        for x, y in self.body_init_pos:
            body_part = self.create_cell(pos=(x, y), shape='square', color='black')
            self.body.append(body_part)

        # TODO: customize body_part (head, tail)
        self.head = self.body[-1]

    def create_cell(self, shape, color, pos=(0,0)):
        new_cell = turtle.Turtle()
        new_cell.speed(0)
        new_cell.up()
        new_cell.setpos(pos)
        new_cell.shapesize(.9,.9)
        new_cell.color(color)
        new_cell.shape(name=shape)

        return new_cell

    def up(self):
        if self.head.heading() != 270:
            self.curr_h = 90

    def down(self):
        if self.head.heading() != 90:
            self.curr_h = 270

    def left(self):
        if self.head.heading() != 0:
            self.curr_h = 180

    def right(self):
        if self.head.heading() != 180:
            self.curr_h = 0

    def move(self):
        self.head.seth(self.curr_h)
        self.head.forward(self.step_size)

    # TODO: implement
    def extend(self):
        pass

    def render(self):
        for i in range(len(self.body) - 1):
            curr = self.body[i]
            _next = self.body[i + 1]
            curr.goto(_next.pos())

        self.move()
