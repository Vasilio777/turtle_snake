import turtle 
from Snake import Snake 
from Scoreboard import Scoreboard
from FoodController import FoodController
from constants import screensize, cell_size
import math
import random

t = turtle.Turtle()
t.screen.tracer(0)

paused = True
is_game_over = False

def toggle_pause(x, y):
    global paused
    paused = not paused

def restart(x, y):
    global is_game_over, paused
    if is_game_over:
        is_game_over = False
        paused = False

        snake.on_restart()
        food_controller.on_restart()
        scoreboard.on_restart()
    
def init_game(snake, scoreboard):
    global t
    t.screen.setup(screensize[0], screensize[1])
    t.screen.onscreenclick(toggle_pause, 1)
    t.screen.onscreenclick(restart, 3)

    spawn_food()

    render_tick()

    t.screen.onkeypress(snake.up, 'w')
    t.screen.onkeypress(snake.down, 's')
    t.screen.onkeypress(snake.left, 'a')
    t.screen.onkeypress(snake.right, 'd')
    
    t.pen(speed=0, shown=False)

def render_tick():
    global t, paused, is_game_over

    level = math.floor(scoreboard.get_score() / 5)
    scoreboard.set_speed_level(level)

    if not paused and not is_game_over:
        snake.render_tick()
        if snake.is_collision():
            paused = True
            is_game_over = True
            scoreboard.game_over()

        food_controller.render_tick(snake, scoreboard)
        scoreboard.draw()

    t.screen.update()
    
    curr_speed = 1 + level * 0.5
    turtle.ontimer(render_tick, max(10, int(100 / curr_speed)))

def spawn_food():
    if not paused:
        food_controller.spawn_food()
    
    tick_within = random.randrange(300, 2000)
    turtle.ontimer(spawn_food, tick_within)

snake = Snake()
scoreboard = Scoreboard()
food_controller = FoodController(10)

init_game(snake, scoreboard)

t.screen.listen()
t.screen.mainloop()
