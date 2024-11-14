
import turtle

def draw_heart(turtle, message):
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(113)
    turtle.circle(-90, 180)
    turtle.setheading(60)
    turtle.circle(-90, 180)
    turtle.forward(112)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.color("red")
    turtle.write(message, font=("Arial", 24, "bold"), align="center")

window = turtle.Screen()
window.bgcolor("black")

my_turtle = turtle.Turtle()
my_turtle.speed(2)

message = "I Love You, tere bandi ka name!"
draw_heart(my_turtle, message)

window.mainloop()