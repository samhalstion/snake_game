#import packages
import turtle
import random
import time


#creating screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=700,height=700)
screen.tracer(0)
screen.bgcolor("black")



#creating border

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()


#score
score = 0
delay = 0.1

#snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#food
mouse = turtle.Turtle()
mouse.speed(0)
mouse.shape("square")
mouse.color("white")
mouse.penup()
mouse.goto(30,30)

old_mouse = []

#scoring system
scoring=turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score: ", align="center",font=("Courier",24,"bold"))

#define movement

def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)

#Keyboard binding
screen.listen()
screen.onkeypress(snake_go_up,"Up")
screen.onkeypress(snake_go_down,"Down")
screen.onkeypress(snake_go_left,"Left")
screen.onkeypress(snake_go_right,"Right")

#Main Loop

while True:
    screen.update()

    #snake & mouse colision 
    if snake.distance(mouse) < 20:
        x = random.randint(-290,270)
        y = random.randint(-240,240)
        mouse.goto(x,y)
        scoring.clear()
        score +=1
        scoring.write("Score:{}".format(score), align="center",font=("Courier",24,"bold"))
        delay -= 0.001

        #creating new mouse
        new_mouse = turtle.Turtle()
        new_mouse.speed(0)
        new_mouse.shape("square")
        new_mouse.color("red")
        new_mouse.penup()
        old_mouse.append(new_mouse)

    #adding ball to snake

    for index in range(len(old_mouse)-1,0,-1):
        a = old_mouse[index -1].xcor()
        b = old_mouse[index -1].ycor()

        old_mouse[index].goto(a,b)

    if len(old_mouse) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_mouse[0].goto(a,b)
    snake_move()


    # Snake and Border colision 
    if snake.xcor() >280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() <-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor("blue")
        scoring.goto(0,0)
        scoring.write("Game Over: \n Your Score is {}".format(score), align="center",font=("Courier",30,"bold"))

        #snake colision
    for food in old_mouse:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("blue")
            scoring.goto(0,0)
            scoring.write("Game Over: \n Your Score is {}".format(score), align="center",font=("Courier",30,"bold"))

    time.sleep(delay)

turtle.turtle.Terminator()
            