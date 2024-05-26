from turtle import Turtle
from random import choice, randint

COLORS = ["white", "black", "red", "green", "blue", "cyan", "magenta",
          "yellow", "orange", "purple", "brown", "pink", "gold",
          "silver", "gray", "navy", "turquoise", "olive", "maroon", "lime"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5
CAR_LENGTH_RATIOS = (1, 2, 3, 4)
CAR_WIDTH_RATIOS = (0.5, 1)
OUTLINE = 5


class CarManager:
    """Manages the creation and movement of cars on the screen."""

    def __init__(self):
        self.all_cars = []
        self.car_positions = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawning = 15
        self.safe_distance = 50

    def create_car(self):
        """Creates a new car at a random y-position and adds it to the list."""
        random_y = randint(-240, 250)
        if randint(1, self.spawning) == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.setheading(180)
            color = choice(COLORS)
            new_car.color(color)
            new_car.shapesize(stretch_wid=choice(CAR_WIDTH_RATIOS), stretch_len=choice(CAR_LENGTH_RATIOS),
                              outline=OUTLINE)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
            self.car_positions.append(new_car.ycor())

    def move_cars(self):
        """Moves all cars forward by the current car_speed."""
        for car in self.all_cars:
            car.forward(self.car_speed)

    def car_move_increment(self):
        """Increases the car_speed by MOVE_INCREMENT."""
        self.spawning -= 1
        self.car_speed += MOVE_INCREMENT
