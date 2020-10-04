import turtle

#Creation of screen
win=turtle.Screen()
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)# it stops updating our window 


#Paddle _a
paddle_a=turtle.Turtle()
paddle_a.speed(0)#its speed of animation (Kind of maintaining FPS)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(5,1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b=turtle.Turtle()
paddle_b.speed(0)#its speed of animation (Kind of maintaining FPS)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(5,1)
paddle_b.penup()
paddle_b.goto(350,0)
# Main loop

#ball
ball=turtle.Turtle()
ball.speed(0)#its speed of animation (Kind of maintaining FPS)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx =0.5
ball.dy =0.5

#score
score_a=0
score_b=0
score=turtle.Turtle() #turtle-module name Turtle - class name (which is gonna run in background)
score.speed(0)
score.penup()
score.hideturtle()
score.color("white")
score.goto(0,270)

score.write("Player A:{} Player B:{}".format(score_a,score_b),align="center", font=("courier",24,"normal"))


# Function to move paddle A
def paddle_a_up():
    y =paddle_a.ycor()
    y =y+20
    paddle_a.sety(y)
    
def paddle_a_down():
    y=paddle_a.ycor()
    y=y-20
    paddle_a.sety(y)

# Function to move paddle B
def paddle_b_up():
    y =paddle_b.ycor()
    y =y+20
    paddle_b.sety(y)
    
def paddle_b_down():
    y=paddle_b.ycor()
    y=y-20
    paddle_b.sety(y)
#Keyboard Binding
win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")


while True:
    win.update()
    
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy=ball.dy * -1
    
    if ball.xcor() > 390:
        #ball.setx(390)
        #ball.dy, ball.dx=ball.dy * 1, ball.dx * -1
        ball.goto(0,0)
        ball.dx*= -1
        score_a +=1
        score.clear()
        score.write("Player A:{} Player B:{}".format(score_a,score_b),align="center", font=("courier",24,"normal"))
        if score_a >= 10:
            score.clear()
            score.write("....Player A WINS.....",align="center", font=("courier",24,"bold"))
            break
        if score_b >= 10:
            score.clear()
            score.write("....Player B WINS.....",align="center", font=("courier",24,"bold"))

    if ball.ycor() < -290:
        ball.dy=ball.dy * -1
        
        
       
    if ball.xcor() < -390:
        #ball.dy, ball.dx=ball.dy * 1, ball.dx * -1
        ball.goto(0,0)
        ball.dx*= -1
        score_b +=1
        score.clear()
        score.write("Player A:{} Player B:{}".format(score_a,score_b),align="center", font=("courier",24,"normal"))
        if score_a >= 10:
            score.clear()
            score.write("....Player A WINS.....",align="center", font=("courier",24,"bold"))
            break
        if score_b >= 10:
            score.clear()
            score.write("....Player B WINS.....",align="center", font=("courier",24,"bold"))
                
        #paddle with ball
    if (ball.xcor()>340 and ball.xcor()<350)and (ball.ycor()< paddle_b.ycor()+50 and ball.ycor()> paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor()< -340 and ball.xcor()> -350)and (ball.ycor()< paddle_a.ycor()+50 and ball.ycor()> paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1

        
