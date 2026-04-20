from turtle import Turtle, Screen

jin = Turtle()

def move_forward():
    jin.forward(10)
def move_backward():
    jin.backward(10)
def turn_left():
    jin.left(10)
def turn_right():
    jin.right(10)
def clear():
    jin.clear()
    jin.penup()
    jin.home()

screen = Screen()
screen.listen()
screen.onkey(key = "w" , fun = move_forward)
screen.onkey(key = "s" , fun = move_backward)
screen.onkey(key = "a" , fun = turn_left)
screen.onkey(key = "d" , fun = turn_right)
screen.onkey(key = "c" , fun = clear)

screen.exitonclick()
