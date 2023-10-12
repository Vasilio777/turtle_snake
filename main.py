import turtle 
from Snake import Snake 
from Scoreboard import Scoreboard
from Food import Food
import math

t = turtle.Turtle()
t.screen.tracer(0)
screensize = (1280, 720)
cell_size = 20
field_size = ((int(screensize[0] / cell_size) - 2) * cell_size / 2, (int(screensize[1] / cell_size) - 2) * cell_size / 2)
paused = True
is_game_over = False
speed = 1

def toggle_pause(x, y):
    global paused
    paused = not paused

def init_game(snake, scoreboard):
    global t
    t.screen.setup(screensize[0], screensize[1])
    t.screen.onscreenclick(toggle_pause)
    
    spawn_food()

    render_tick()

    t.screen.onkeypress(snake.up, 'w')
    t.screen.onkeypress(snake.down, 's')
    t.screen.onkeypress(snake.left, 'a')
    t.screen.onkeypress(snake.right, 'd')
    
    t.pen(speed=0, shown=False)

def render_tick():
    global t, speed, paused, is_game_over, field_size

    if not paused and not is_game_over:
        snake.render()

        if snake.head.xcor() < -field_size[0] \
            or snake.head.xcor() > field_size[0] \
            or snake.head.ycor() < -field_size[1] \
            or snake.head.ycor() > field_size[1] \
            or snake.is_body_collision():
            paused = True
            is_game_over = True
            scoreboard.game_over()

        if len(food_collection) > 0:         
            for food in food_collection:
                food.render(snake.head.pos())
                if food.collected:
                    food_collection.remove(food)
                    snake.extend()
                    scoreboard.add_score()
        
        scoreboard.print_score()


    t.screen.update()
    s_multi = math.floor(scoreboard.score / 5) * 0.5
    turtle.ontimer(render_tick, max(10, int(100 / multiply_speed(s_multi))))

def multiply_speed(multi):
    global speed
    cache = speed
    return cache * 1 + multi

def spawn_food():
    if not paused:
        if len(food_collection) < 10:
            new_food = Food(screensize, cell_size)
            food_collection.append(new_food)

    t.screen.update()
    turtle.ontimer(spawn_food, 100)

snake = Snake(cell_size)
scoreboard = Scoreboard(screensize)
food_collection = []

init_game(snake, scoreboard)

t.screen.listen()
t.screen.mainloop()
