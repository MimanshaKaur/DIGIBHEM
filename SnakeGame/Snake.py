import turtle
import random
import time

delay = 0.1
score = 0
highestscore ="0"

#snake body
body=[]

#creating a screen
screen= turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("SNAKE GAME")

#creating snake head
head=turtle.Turtle()
head.shape("square")
head.color("white")
head.fillcolor("white")
head.penup()
head.goto(0,0)

# creating food
food=turtle.Turtle()
food.shape("circle")
food.color("#386641")
food.fillcolor("#A7C957")
food.speed(0)
food.penup()
food.ht()
food.goto(0,150)
food.st()

# creating scoreboard
sb=turtle.Turtle()
sb.shape("square")
sb.color("#fb6f92")
sb.fillcolor("#fb6f92")
sb.penup()
sb.ht()
sb.goto(-450,-450)
sb.write(" SCORE : 0      | HIGHEST SCORE : 0 ")

def moveup():
    if head.heading()!= 90:
        head.right(270)
def movedown():
    if head.heading()!=270:
        head.right(90)
def moveleft():
    if head.heading()!=0:
        head.right(180)
def moveright():
    if head.heading()!=180:
        head.right(0)
def move():
    if head.heading()==270:
        y=head.ycor()
        head.sety(y+20)
    if head.heading()==90:
        y=head.ycor()
        head.sety(y-20)
    if head.heading()==180:
        x=head.xcor()
        head.setx(x-20)
    if head.heading()==0:
        x=head.xcor()
        head.setx(x+20)

#key mapping
screen.listen()
screen.onkey(moveup ,"Up")
screen.onkey(movedown,"Down")
screen.onkey(moveleft,"Left")
screen.onkey(moveright,"Right")

#main loop
while True:
    screen.update()

    #new food generation
    if head.distance(food)<20:
        x=random.randint(-450,450)
        y=random.randint(-450,450)
        food.goto(x,y)

    #increasing snake body length
    body_part=turtle.Turtle()
    body_part.speed(0)
    body_part.penup()
    body_part.shape("square")
    body_part.color("#D90429")
    body_part.fillcolor("#D90429")
    body.append(body_part)

    #increasing score
    score+=1
    #increasing snake speed
    delay-=0.001
    #score update
    if score>int(highestscore):
        highestscore=score
    sb.clear()
    sb.write("SCORE:{} HIGHESTSCORE: {}",format(score,str(highestscore)))
    #moving snake body
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    move()
    time.sleep(0)

    #checking collision with body
    for j in body:
        if j.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            j.ht()
            body.clear()
            score=0
            delay=0
            sb.clear()
            sb.write("SCORE:{} HIGHESTSCORE: {}",format(score,highestscore))

    #checking collision with borders
    x=head.xcor()
    y=head.ycor()
screen.mainloop()