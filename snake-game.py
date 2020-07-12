import os
import turtle
import time
import random
import ctypes


delay = 0.1
# Scoring
score = 0
high_score = 0
# making the Screen ....
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor('green')
wn.setup(width=600,height=600)
wn.tracer(0) # turns of the screen update

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color('black')
head.penup()
head.goto(0,0)
head.direction='stop'

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color('red')
food.shapesize(0.75,0.75)
food.penup()
food.goto(0,100)

segments = []
 # pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0 High Score: 0",align="center",font=("courier",24,"normal"))


# functions
def go_up():
    if head.direction != "down":
        head.direction ="up"
def go_down():
    if head.direction != "up":
        head.direction ="down"
def go_left():
    if head.direction != "right":
        head.direction ="left"
def go_right():
    if head.direction != "left":
        head.direction ="right"
def stop():
    head.direction="stop"

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction =="down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction =="left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction =="right":
        x = head.xcor()
        head.setx(x+20)

# keyboard binding
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
wn.onkeypress(stop,"0")


# main  game loop
while True:
    wn.update()
    # check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() >290 or head.ycor()<-290:
        val = ctypes.windll.user32.MessageBoxW(0, "Play again or not", "Game Says", 5+64)
        if val == 4:
            time.sleep(1)
            score = 0
            head.goto(0,0)
            head.direction="stop"
            pen.clear()
            pen.write("Score : {} High Score: {}".format(score,high_score),align="center",font=("courier",24,"normal"))
        else:
            pass # .clear() ,. reset() ,.clearscreen(), .resetscreen() ,.bye()


        # Hide the segments :
        for segment in segments:
            segment.goto(1000,1000)
        # Clear the segments
        segments.clear() # or segments = []

    # check food collision
    if head.distance(food)<20:
        # move food at random place
        x = random.randint(-290,290)
        y = random.randint(-290,250)
        food.goto(x,y)
        # add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        # Increase the score
        score +=1
        if score > high_score and high_score !=0:
            score = high_score

        pen.clear()
        pen.write("Score : {} High Score: {}".format(score,high_score),align="center",font=("courier",24,"normal"))

    # move the end segmennt
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()

    # check for body collision
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            # Hide the segments :
            for segment in segments:
                segment.goto(1000,1000)
            # Clear the segments
            segments.clear()
    time.sleep(delay)
wn.mainloop()