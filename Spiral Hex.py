import turtle

colors = ["red", "yellow", "green", "purple", "blue", "orange"]

turtle.speed(10)
turtle.bgcolor("black")

for x in range(300):
	turtle.pencolor(colors[x % 6])
	turtle.width(x / 100 + 1)
	turtle.forward(x)
	turtle.left(59)

turtle.done()