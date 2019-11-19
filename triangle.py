import turtle
nofsides=20
turtle.color("red")
for i in range(nofsides):
    turtle.forward(100)
    turtle.right(360/nofsides)
    for j in range(nofsides):
        turtle.forward(50)
        turtle.right(360 / nofsides)
