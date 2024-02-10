import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

#snake body
body=[]

#creating a screen
screen= turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

#creating snake head
head=turtle.Turtle()
head.shape("circle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "Stop"

# creating food
food=turtle.Turtle()
food.shape("square")
food.color("#70e000")
food.speed(0)
food.penup()
food.goto(0,150)

# creating scoreboard
sb=turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(0,250)
sb.write("Score : 0 High Score : 0", align="center",font=("candara", 24, "bold"))

# assigning key direction
def moveup():
    if head.direction !="down":
        head.direction ="up"
def movedown():
    if head.direction !="up":
        head.direction ="down"
def moveleft():
    if head.direction !="right":
        head.direction ="left"
def moveright():
    if head.direction !="left":
        head.direction ="right"
def move():
    if head.direction =="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction =="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction =="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction =="right":
        x=head.xcor()
        head.setx(x+20)

#key mapping
screen.listen()
screen.onkeypress(moveup ,"Up")
screen.onkeypress(movedown,"Down")
screen.onkeypress(moveleft,"Left")
screen.onkeypress(moveright,"Right")

#main loop
while True:
    screen.update()
    #checking collision with borders
    x=head.xcor()
    y=head.ycor()
    if x > 290 or x < -290 or y>290 or y < -290 :
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        for j in body:
            j.goto(1000, 1000)
        body.clear()
        score=0
        delay=0.1
        sb.clear()
        sb.write("SCORE : {}  HIGH SCORE : {}" .format(score, high_score), align="center" , font=("candara", 24 ,"bold"))
    #new food generation
    if head.distance(food)<20:
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        food.goto(x,y)
        #increasing snake body length
        body_part=turtle.Turtle()
        body_part.speed(0)
        body_part.shape("circle")
        body_part.color("#70E000")
        body_part.penup()
        body.append(body_part)
        #increasing snake speed
        delay-=0.001
        #increasing score and updating
        score+=10
        if score > high_score:
            high_score = score
        sb.clear()
        sb.write("SCORE : {}  HIGH SCORE : {}" .format(score, high_score), align="center" , font=("candara", 24 ,"bold"))
    #moving snake body
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body) > 0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    move()
    #checking collision with body
    for j in body:
        if j.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for j in body:
                j.goto(1000, 1000)
            body.clear()
            score=0
            delay=0.1
            sb.clear()
            sb.write("SCORE : {}  HIGH SCORE : {}" .format(score, high_score), align="center" , font=("candara", 24 ,"bold"))
    time.sleep(delay)
screen.mainloop()