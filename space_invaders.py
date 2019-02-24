#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 18:47:06 2019

@author: mdrafiqrifhanrosman
"""

#Space invaders = Part 1 
#Set up the screen 
#Python 3.7 on Mac 

import turtle 
import os 
import math 
import random 


#set up the screen 

wn = turtle.Screen () #wn is the object
wn.bgcolor ("black")
wn.title("Space Invaders")
wn.bgpic ("space.gif")
#wn.bgpic ("invader_enemy.gif")

#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#Draw border 
border_pen = turtle.Turtle() #this is how you create a turtle 
border_pen.speed (0) # where zero is the fastest speed to draw 
border_pen.color("white")
border_pen.penup() #penup is going to help it draw a line 
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize (3) #thicknes of the pen 
for side in range (4): #drawing the square 
    border_pen.fd (600) #where fd is forward 
    border_pen.lt(90) #where lt is going to the left where 90 is the degrees of turn of the pen 
border_pen.hideturtle() #hide the pen that is drawing 

#Set the score to 0
score = 0

#Draw the score 
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("yellow")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: " + str(score)
score_pen.write (scorestring, False, align = "left", font=("Arial",25, "normal"))
score_pen.hideturtle()



#the pen starts from the center, moves from the centre to the left to -300, and then moves
#downwards again to -300 , turns left again forward by 600, and then continues to do it 4 times
#until a square is created 

#Create  the player turtle 
player = turtle.Turtle ()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)#because we want the speed to be the fastest as possible for the game 
player.setposition (0, -250) #down to the bottom of the border 
#when we run the code at this point, the triangle will be facing to the right by default 
#it can rotated in an anticlockwise manner, where rotating it to face up from facing right
#is to turn it by 90 degrees 
player.setheading (90)

#Moving the player turtle 
playerspeed = 15 #setting the playerspeed vriable 


#Choose a number if enemeies 
number_of_enemies = 5
#Create an empty list of enemies 
enemies = [] # we start out with an empty list 

#Add enemies to the list 
for i in range (number_of_enemies):
    #Create the enemy 
    enemies.append (turtle.Turtle()) #apeending a turtle to our list
    
    
for enemy in enemies: #for each pf the enemy in turtles, we are gonna change the colours etc 
    enemy.color ("red")
    enemy.shape("invader.gif")
    enemy.penup() #because we dont want the enemy to draw any line on the screen 
    enemy.speed(0)
    x = random.randint (-200,200)# will start it from a random spot from -200 to 200 
    y = random.randint (100,250)
    enemy.setposition(x , y)

enemyspeed = 2 # making the enemy slower 

    

#Create the player's bullet 
bullet = turtle.Turtle()
bullet.color("Yellow")
bullet.shape ("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.1,1.0)
bullet.hideturtle() # hide the bullet at first

bulletspeed = 20 

#Define bullet state 
#ready - ready to fire 
#@fire - bullet is firing 
bulletstate = "ready" #when we start firing bulletstate = ready 

#from here we need to create functions, one to move it to the right, and the other to the left.
#afterwards, we want to bind it into  a key 

#Moving the player left and right aka boundary checking 
def move_left():
    x = player.xcor() #getting the x coordinate of the player 
    x -= playerspeed #here it takes the current value of x, subtracts player speed and assigns that to x 
    #eg: we start with  x=0. so we then subtract the playerspeed, and now x is -15
    if x < -280:
        x = -280 #here, we want to make sure that x moves within the border and thus when x is going to go outside the border , whatever the value of x is, it will be set to -280 at most 
    player.setx(x) #changing the players location from x to a new x 

def move_right():
    x= player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    
def fire_bullet():
    #Declare bulletstate as a global if it needs changed 
    global bulletstate #if a variable is defined inside a function, it is a local variable only to the function, outside of the function, variables are globals 
    #in this case we want to change the global bulletstate, so we have to make the one in the function global so that the global(outside the function) will also be changed 
    if bulletstate == "ready" :#we push the space bar, and check the state, if its ready, it will fire 
        os.system ("afplay laser.mp3&")
        bulletstate = "fire"
        #Move the bullet to the just above the player 
        x = player.xcor()
        y = player.ycor() + 15 #because we want to put the bullet above the player 
        bullet.setposition (x, y)
        bullet.showturtle ()
        
        
def isCollision(t1, t2): #we usually put is is at the front of the function name to show that we are actually checkking whether or not 
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor() , 2)+ math.pow(t1.ycor()- t2.ycor(),2))
    if distance < 15:
        return True 
    else:
        return False 
    
    
    
    
    
    
    
#Create keyboard bindings 
turtle.listen() #asking the turtle to listen to the keyboard actions 
turtle.onkey(move_left, "Left") #when push the left arrow key, the function move left is called 
turtle.onkey(move_right, "Right")
turtle.onkey (fire_bullet, "space")

#Main Game Looop
while True: #we want the game to run forever, once this loop is ran, the wn.mainloop at the bottom will not run anymore 
   
    for enemy in enemies : 
        #Move the enemy 
        x = enemy.xcor()
        x+= enemyspeed
        enemy.setx(x)
        
        #Moving the enemy back and down
        
        if enemy.xcor() > 280 :
            #Move all the enemies down together 
            for e in enemies:
                y = e.ycor()
                y -= 40  #every time the enemy hits the border, it will go down by 40 pixels, and thus gets closer and closer to user 
                e.sety(y)
            #Changes the direction 
            enemyspeed *= -1 #because we want to multply this to the speed 2 we set earlier, 
#            2* -1 = -2 so the enemy will reverse direction ie will minus its coordinates hance gg back 
            
            
        if enemy.xcor () < -280:
            #Move all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40 
                e.sety(y)
            #Changes the enemy direction 
            enemyspeed *= -1 # will become positive  and thus will move forward
            
         #Check for a collison fr a collison between the bullet anf the enemy 
        if isCollision (bullet, enemy) :
            #Reset the bullet 
            bullet.hideturtle()
            bulletstate = "ready" 
            bullet.setposition (0, -400) #moves the bullet down the screen so that we dont have anty positive collisions later 
            #so even if the bullet is hidden, the collision code will still be running and it we leave it there, even if its 
            #its invisible, enemies can still run into it 
            os.system ("afplay explosion.mp3&") #without & the program will pause 
            #Reset the enemy:
            enemy.setposition (-200, 250)
            x = random.randint (-200,200)# will start it from a random spot from -200 to 200 
            y = random.randint (100,250)
            enemy.setposition(x , y)
            #update the score
            #Draw the score 
            os.system ("afplay score.mp3&")
            score += 10
            scorestring = "Score: " + str(score)
            score_pen.clear()
            score_pen.write (scorestring, False, align = "left", font=("Arial",25, "normal"))
        
            
            

            
        if isCollision (player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game over")
            break #will break us out of the main loop 
            
        
    #Move the bullet
    if bulletstate == "fire": #trying not to waste the clock cycle, so if its ready we dont it to fire 
        y = bullet.ycor()
        y += bulletspeed 
        bullet.sety(y)
        #if we run this at this point the bullet will continue firing when press enter and seems to like coming back to the user instead, and thats not what we want 
        
        
    #Check if the bullet has gone to the top 
    if bullet.ycor() > 275 :
        bullet.hideturtle ()
        bulletstate = "ready" 
    
   
        






    
    




















#delay = input ("Press enter to finish") #you need this, if not the screen will flash for a short time and be gone 

wn.mainloop() #using the delay might crash python 3.6 and above 


