import subprocess
import turtle
import time
import random
import os
delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("The Snake King Game by Sabrina")
wn.bgpic("snake1.gif")
wn.setup(width=600, height=700)
wn.tracer(0) # Turns off the screen updates
wn.register_shape("apple apple.gif")
wn.register_shape("snake-head-.gif")
wn.register_shape("melon2.gif")
wn.register_shape("grapes.gif")
wn.register_shape("watermelon.gif")
wn.register_shape("mango.gif")
wn.register_shape("strawberry.gif")

# Snake head
head = turtle.Turtle()
head.shape("snake-head-.gif")
# head.color()
head.penup()
head.goto(160,-200)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("apple apple.gif")
#food.color("red")
food.penup()
food.goto(0,100)

#Snake food 2
grape=turtle.Turtle()
grape.speed(1)
grape.shape("grapes.gif")
#grapes.color
grape.penup()
grape.goto(100,100)

#Snake food 3
watermelon=turtle.Turtle()
watermelon.speed(1)
watermelon.shape("watermelon.gif")
#watermelon.color
watermelon.penup()
watermelon.goto(-100,100)

#Snake food 4
mango=turtle.Turtle()
mango.speed(1)
mango.shape("mango.gif")
#mango.color
mango.penup()
mango.goto(-100,0)

#Snake food 5
fruit=turtle.Turtle()
fruit.speed(1)
fruit.shape("melon2.gif")
#fruit.color
fruit.penup()
fruit.goto(0,0)

#Snake food 6
strawberry=turtle.Turtle()
strawberry.speed(1)
strawberry.shape("strawberry.gif")
#straberry.color
strawberry.penup()
strawberry.goto(100,0)


segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "bold"))

         
# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()
    #subprocess.call(["afplay","bgmusic.mp3"])#this is the music background
        # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        subprocess.call(["afplay","hitthewall.mp3"])
        head.goto(0,0)
        head.direction = "stop"
        

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "bold")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)
        subprocess.call(["afplay","eatfood.mp3"])#eat food sounds
        # Increase the score
        score +=30

    if head.distance(grape) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        grape.goto(x,y)
        subprocess.call(["afplay","eatfood.mp3"])
         # Increase the score
        score -= 10

        if score > high_score:
            high_score = score
        
        # Shorten the delay
        delay -= 0.001

        #add the music in 
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        
        pen.clear()
        pen.color("blue")
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "bold")) 


   
    if head.distance(mango) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        mango.goto(x,y)
        subprocess.call(["afplay","eatfood.mp3"])#eat food sounds
         # Increase the score
        score += 20

        if score > high_score:
            high_score = score
        
        # Shorten the delay
        delay -= 0.001

    
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)

        
        pen.clear()
        pen.color("Red")
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "bold")) 

    if head.distance(watermelon) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        watermelon.goto(x,y)
        subprocess.call(["afplay","eatfood.mp3"])#eat food sounds
         # Increase the score
        score += 20

        if score > high_score:
            high_score = score
        
        # Shorten the delay
        delay -= 0.001

    
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

        
        pen.clear()
        pen.color("turquoise")
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "normal")) 

    if head.distance(strawberry) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        strawberry.goto(x,y)
        subprocess.call(["afplay","eatfood.mp3"])#eat food sounds
         # Increase the score
        score += 50

        if score > high_score:
            high_score = score
        
        # Shorten the delay
        delay -= 0.001

    
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        
        pen.clear()
        pen.color("Green")
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "bold")) 



    if head.distance(fruit) < 20:
        # Move the food to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        fruit.goto(x,y)
        
         # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        # Shorten the delay
        delay -= 0.001
        subprocess.call(["afplay","eatfood.mp3"])#eat food sounds
         # Increase the score
        score += 30

        if score > high_score:
            high_score = score
    
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        
        pen.clear()
        pen.color("purple")
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "bold")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()
            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.color("orange")
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 18, "bold"))

    time.sleep(delay)

wn.mainloop()
