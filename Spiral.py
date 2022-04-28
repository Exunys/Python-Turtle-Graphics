import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(10)

for i in range(6):
	for color in ("red", "magenta", "blue", "cyan", "green", "white", "yellow"):
		turtle.color(color)
		turtle.circle(100)
		turtle.left(10)

	turtle.hideturtle()