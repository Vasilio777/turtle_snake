import turtle 
from Snake import Snake 
from Scoreboard import Scoreboard

t = turtle.Turtle()
screensize = (1280, 720)
cell_size = 20
paused = True
speed = 1

def toggle_pause(x, y):
    global paused
    paused = not paused

def init_game(snake, scoreboard):
    global t
    t.screen.setup(screensize[0], screensize[1])
    t.screen.onscreenclick(toggle_pause)
    render_tick()

    t.screen.onkeypress(snake.up, 'w')
    t.screen.onkeypress(snake.down, 's')
    t.screen.onkeypress(snake.left, 'a')
    t.screen.onkeypress(snake.right, 'd')
    
    t.pen(speed=0, shown=False)

def render_tick():
    global t, speed, paused

    if not paused:
        snake.render()

        field_size = ((int(screensize[0] / cell_size) - 3) * cell_size / 2, (int(screensize[1] / cell_size) - 3) * cell_size / 2)

        if snake.head.xcor() < -field_size[0] \
            or snake.head.xcor() > field_size[0] \
            or snake.head.ycor() < -field_size[1] \
            or snake.head.ycor() > field_size[1]:
            paused = True
            scoreboard.game_over()

    
    # speed *= 1.1
    # turtle.ontimer(render_tick, max(100, int(1000 / speed)))
    turtle.ontimer(render_tick, 100)

snake = Snake(cell_size)
scoreboard = Scoreboard()
init_game(snake, scoreboard)

t.screen.listen()
t.screen.mainloop()
