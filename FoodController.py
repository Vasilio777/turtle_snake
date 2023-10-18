from Food import Food
from constants import screensize, cell_size
import turtle 

class FoodController():
    def __init__(self, food_amount_max):
        self.food_collection = []
        self.food_amount_max = food_amount_max

    def spawn_food(self):
        if len(self.food_collection) < self.food_amount_max:
            new_food = Food(screensize, cell_size)
            self.food_collection.append(new_food)

    def render_tick(self, snake, scoreboard):
        if len(self.food_collection) > 0:         
            for food in self.food_collection:
                food.render(snake.head.pos())
                if food.collected:
                    self.food_collection.remove(food)
                    snake.extend()
                    scoreboard.add_score()

    def on_restart(self):
        [i.on_restart() for i in self.food_collection]
        self.food_collection.clear()
