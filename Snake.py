from constants import screensize, cell_size
import turtle
import random

class Snake():
    def __init__(self):
        super().__init__()
        self.step_size = cell_size
        self.curr_h = 0
        self.body = []
        self.init_snake_size = 3
        self.body_init_pos = [(i * self.step_size, 0) for i in range(self.init_snake_size + 1)]

        for x, y in self.body_init_pos:
            body_part = self.create_cell(pos=(x, y), shape='square', color='black')
            self.body.append(body_part)

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

    def is_field_collision(self) -> bool:
        field_size = ((int(screensize[0] / cell_size) - 2) * cell_size / 2, (int(screensize[1] / cell_size) - 2) * cell_size / 2)
        return self.head.xcor() < -field_size[0] \
            or self.head.xcor() > field_size[0] \
            or self.head.ycor() < -field_size[1] \
            or self.head.ycor() > field_size[1]

    def is_body_collision(self) -> bool:
        for body_i in range(len(self.body) - 1):
            if self.head.distance(self.body[body_i]) < 1:
                return True
        return False

    def is_collision(self):
        return self.is_field_collision() or self.is_body_collision()

    def extend(self):
        body_part = self.create_cell(pos=self.body[0].pos(), shape='square', color='black')
        self.body.insert(0, body_part)

    def render_tick(self):
        for i in range(len(self.body) - 1):
            curr = self.body[i]
            _next = self.body[i + 1]
            curr.goto(_next.pos())

        self.move()

    def on_restart(self):
        tail_pointer = -self.init_snake_size-1

        [i.ht() for i in self.body[:tail_pointer]]
        self.body = self.body[tail_pointer:]
        for i in range(len(self.body)):
                self.body[i].setpos(self.body_init_pos[i])
        self.curr_h = 0
