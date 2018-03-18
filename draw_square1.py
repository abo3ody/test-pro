import turtle
my_turtle=turtle.Turtle()
my_turtle.speed(0)
window=turtle.Screen()
window.bgcolor("gray")


def square(length,angle):
    for i in range(4):
        my_turtle.shape("turtle")
        my_turtle.color("red")
        my_turtle.forward(length)
        my_turtle.right(angle)
for i in range(36):
    square(100,90)
    my_turtle.right(10)
window.exitonclick()
