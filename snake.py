import turtle
import time
import random


delay = 0.05
body_segments = []
score = 0
high_score = 0

wn = turtle.Screen()

#Title
wn.title("juego culebrita")

#Size
wn.setup(width=600, height=600)

#Color
wn.bgcolor('cyan4')

#Head settings 

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color('gold')
head.penup()
head.goto(0,0) 
head.direction = "stop"

#foodSetings

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Red")
food.penup()
food.goto(0,100)
food.direction = "stop"

#score

text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write(f'score 0        High Score: 0',align="center",font=("roboto",24))


def mov():
     if  head.direction == "up":
        y = head.ycor()
        head.sety(y+15)

     if head.direction == "down":
        y = head.ycor()
        head.sety(y-15)

     if head.direction == "right":
        x = head.xcor()
        head.setx(x+15)

     if head.direction == "left":
        x = head.xcor()
        head.setx(x-15)

def dirUp():
    head.direction = "up"

def dirDown():
    head.direction = "down"

def dirRight():
    head.direction = "right"

def dirLeft():
    head.direction = "left"




wn.listen()
wn.onkeypress(dirUp, "Up" )
wn.onkeypress(dirDown, "Down" )
wn.onkeypress(dirLeft, "Left" )
wn.onkeypress(dirRight, "Right" )



while True:
    wn.update()
        #colision paredes
    
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
    

        #esconder segmentos
        for segment in body_segments:
            segment.goto(1000,1000)

        body_segments.clear()
        score = 0
        text.clear()
        text.write(f'score 0 {score}     High Score: {high_score}',align="center",font=("roboto",24))


       

        #colision vs food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)

        #new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("yellow")
        new_segment.penup()
        body_segments.append(new_segment)

        score += 10
        if score > high_score:
                high_score = score
        
        text.clear()
        text.write(f'score 0 {score}     High Score: {high_score}',align="center",font=("roboto",24))

    
    totalSeg = len(body_segments)

    for i in range (totalSeg - 1, 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)



    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x, y)



    mov() 

    #colisiones con los segmentos
    
    for segment in body_segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in body_segments:
                segment.goto(1000,1000)

            body_segments.clear()

            score = 0
            text.clear()
            text.write(f'score 0 {score}     High Score: {high_score}',align="center",font=("roboto",24))



    
    time.sleep(delay)

turtle.done()

