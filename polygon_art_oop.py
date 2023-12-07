import turtle
import random


class Polygon:

    def __init__(self):
        self.num_sides = random.randint(3, 5)  # triangle, square, or pentagon
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = 0.618
        # self.draw_polygon()

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        # turtle.end_fill()

    def get_new_color(self):
        return self.color

    def move_polygon(self):
        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location = turtle.pos()
        self.location = turtle.pos()
        self.size *= self.reduction_ratio


class Polygon_stimulate:

    def __init__(self, num_polygon):
        self.polygon = [Polygon() for _ in range(num_polygon)]

    def move(self):
        for polygon in self.polygon:
            polygon.move_polygon()

    def draw(self):
        for ball in self.polygon:
            ball.draw_polygon()


num_polygon = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive:  "))

turtle.hideturtle()
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
ploy = Polygon()
ploy.draw_polygon()

simulator = Polygon_stimulate(num_polygon)

while True:
    turtle.clear()
    simulator.move()
    simulator.draw()
    turtle.update()
