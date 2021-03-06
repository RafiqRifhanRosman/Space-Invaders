# Space-Invaders

This code allows you to create a basic version of the classic game Space Invaders, I'm currently working to improve the game further to make it as close as possible to the actual game, but with this code it would give you an idea how the game can be created. Please note that the code was written on a Mac, so maybe the format to input audio files may not work on Windows. Before we begin with anything, if you are running python 3.6 and above, please include this in your code (at the end), so that the game screen will not just appear for a short time and will continue to appear until the user presses enter:

    wn.mainloop() #using the delay might crash python 3.6 and above 

The code starts off by importing the modules that we are going to need: 
                    
    import turtle 
    import os 
    import math 
    import random 
    
Importing 'turtle' allows us to create objects in the game. Importing 'os' allows us to access the audio files that we are going to use for the game effects later on. 

Here is the step by step, and the breakdown of the entire space invaders code:

1)After importing the modules, we need to set up the screen of the game:
    
    #set up the screen 
    wn = turtle.Screen ()
    wn.bgcolor ("black")
    wn.title("Space Invaders")
    wn.bgpic("space.gif")

Here, wn = turtle.Screen () would create the basic screen for the game. wn.bgcolor("black") will set up the colour of the game background, and you can change to any color that you want, yellow, teal etc and make sure to put them in parenthesis. wn.title ("space invaders") creates the game title. wn.bgpic ("space.gif") actually allows you to access images from the same folder to be used as your game background. In this game, the format is set to 600 x 600 pixels and the image to be used must be in gif format. Make sure that the image that you want to use is in the same folder as the code. 

2)After creating the screen, it is time for us to create the players and objects in the game:

    #Register the shapes
    turtle.register_shape("invader.gif")
    turtle.register_shape("player.gif")
    
Python only has basic shapes like circles and triangles, so you have to import images of your own, and here, we will use actual invaders and cannon shapes to be used as the 'enemies' and 'player' in the game. But, to be able to use them, you have to register them as above, to be used later.

3)Once we have set up the screen and creating the shapes for our players, we need to create the border for the game, so that the objects in the game will not go elsewhere in the screen. 

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
 
The pen starts from the center, moves from the centre to the left to -300, and then moves
downwards again to -300 , turns left again forward by 600, and then continues to do it 4 times
until a square is created 
    
 4) Creating the score: 
     
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
        
5) Creating the player turtle:
  
        #Create  the player turtle 
        player = turtle.Turtle ()
        player.color("blue")
        player.shape("player.gif")
        player.penup()
        player.speed(0)#because we want the speed to be the fastest as possible for the game 
        player.setposition (0, -250) #down to the bottom of the border 
when we run the code at this point, the player will be facing to the right by default it can rotated in an anticlockwise manner, where rotating it to face up from facing right is to turn it by 90 degrees player.setheading (90)

6) Moving the player turtle:

        #Moving the player turtle 
        playerspeed = 15 #setting the playerspeed variable 

7) Creating the enemies: 

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
        
 8) Creating the laser bullet: 
 
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
        #fire - bullet is firing 
        bulletstate = "ready" #when we start firing bulletstate = ready 
        
 9) Moving the player left and right, also known as boundary checking 
 
        def move_left():
        x = player.xcor() #getting the x coordinate of the player 
        x -= playerspeed 
        if x < -280:
            x = -280 
        player.setx(x) #changing the players location from x to a new x 

        def move_right():
            x= player.xcor()
            x += playerspeed
            if x > 280:
                x = 280
            player.setx(x)
           
At the first part of the code, it takes the current value of x, subtracts player speed and assigns that to x,eg: we start with  x=0. so we then subtract the playerspeed, and now x is -15. Then, we want to make sure that x moves within the border and thus when x is going to go outside the border , whatever the value of x is, it will be set to -280 at most 

10) Firing the bullet: 

        def fire_bullet():
            #Declare bulletstate as a global if it needs changed 
            global bulletstate 
            if bulletstate == "ready" :#we push the space bar, and check the state, if its ready, it will fire 
                os.system ("afplay laser.mp3&")
                bulletstate = "fire"
                #Move the bullet to the just above the player 
                x = player.xcor()
                y = player.ycor() + 15 #because we want to put the bullet above the player 
                bullet.setposition (x, y)
                bullet.showturtle ()
                
 We want to change the global bulletstate, so we have to make the one in the function global so that the global(outside the function) will also be changed 
 

11) Checking for collision, setting the conditions as to what is considered as a collision

        def isCollision(t1, t2): #we usually put is is at the front of the function name to show that we are actually checkking whether or not 
            distance = math.sqrt(math.pow(t1.xcor()-t2.xcor() , 2)+ math.pow(t1.ycor()- t2.ycor(),2))
            if distance < 15:
                return True 
            else:
                return False 
                
 To check whether or not the player or bullet collides with the enemy, or the invader, we have to use pythagoras theorem to calculate the distance between the centres of the objects. Since the objects that we use are about the size of 15 pixels, if the objects are passing towards each other and their centres are less than 15 pixels from each other, the code will register this as a collision. 
 
 12) We need to create the keyboard bindings so that python can 'listen' to our keyboard inputs and execute the right instructions :
 
    #Create keyboard bindings 
    turtle.listen() #asking the turtle to listen to the keyboard actions 
    turtle.onkey(move_left, "Left") #when push the left arrow key, the function move left is called 
    turtle.onkey(move_right, "Right")
    turtle.onkey (fire_bullet, "space")
    
 13) Main Game loop :
 
 
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
                y -= 40  #every time the enemy hits the border, it will go down by 40 pixels, 
                #and thus gets closer and closer to user 
                e.sety(y)
            #Changes the direction 
            enemyspeed *= -1 #because we want to multply this to the speed 2 we set earlier, 
            # 2* -1 = -2 so the enemy will reverse direction ie will minus its coordinates hance gg back 
            
            
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
        
        
        
Up till here, the game is good to go, but it will not be as exciting yet. So from here, I'm adding features such as invaders firing at the player, mothership or the mystery ship appearing and updating the number of lives when the player gets hit.

14) Creating the enemy's bullet: 

        #Createthe enemy's bullet

        enemy_bullet = turtle.Turtle()
        enemy_bullet.color("Red")
        enemy_bullet.shape ("square")
        enemy_bullet.penup()
        enemy_bullet.speed(0)
        enemy_bullet.setheading(-90)
        enemy_bullet.shapesize(0.1,1.0)
        enemy_bullet.hideturtle() # hide the bullet at first
        enemy_bulletspeed = 8
        
        #Define enemy_bulletstate
        enemy_bulletstate = "ready"
Just like creating the bullet for the player, the same idea applies, in this case you can change the colour of the bullet to differentiate the bullets.

15) Defining the enemy_bullet():

        def fire_enemybullet():
            global enemy_bulletstate 
            if enemy_bulletstate == "ready":
                enemy_bulletstate = "fire"
                x = enemy.xcor()
                y = enemy.ycor() -15  #because we want to put the bullet below the enemy 
                enemy_bullet.setposition (x, y)
                enemy_bullet.showturtle ()
            
We also need to define a function for the enemy_bullet so that it can be placed below the invader when it is ready. Note that in this function, instead of +15, we are going to put it at -15 because we want the bullet to be ready and placed at the bottom of the invader. The function fire_enemybullet() is called at the beginning of the for loop: for enemy in enemies.


16) For the bullet to travel downwards, we need to add the following statements to the the main game loop. Under, the while loop, under for enemy in enemies loop: 

        if enemy_bulletstate == "fire":
                    y = enemy_bullet.ycor()
                    y -= enemy_bulletspeed 
                    enemy_bullet.sety(y)
        
        if enemy_bullet.ycor() < -275:
            enemy_bullet.hideturtle ()
            enemy_bulletstate = "ready"

The idea works exactly the same as the the player bullet but we need to make some adjustments such as instead of incrementing y, we need to decrement it so that it travels downwards. And instead of setting the condition to +275 we change it to  "if enemy_bullet.ycor() < -275" because the bullet is going downwards to negative y coordinate and we need to reset it at y coordinate = -275

16) Creating lives: 

        #Set the number of lives
        number_lives = 5

        #Making lives 

        lives = []

        for i in range (number_lives):
            lives.append(turtle.Turtle)

        xpos = -280

        for live in lives:

            live = turtle.Turtle()
            live.speed(0)
            live.shape("lives.gif")
            live.shapesize(100,100)
            live.penup()
            y = -280
            live.setposition(xpos, y)
            xpos += 40
            
Same idea as creating enemies applies when creating the lives where lives is made into a list and in the list are a bunch of live. The initial xpos (x coordinate position) is set to -280 because we want to the lives to appear at the bottom-left section of the game screen. So as it creates each of the live, xpos is incremented so that the live that is created will not overlap with the previous live created. 

17) Changing the red hearts/ lives when the enemy bullet hits the player: 
We are going to use a new shape for this, and I'm using a black version of the lives that we have created. So, we have to once again register this new shape or the code will not be able to use it.
                
    turtle.register_shape ("lives2.gif")

We are going to create the black hearts when the enemy_bullet collides with the player. So we have to check for collision between the enemy_bullet and the player beforehand. And to this, we have to call the isCollision function. 

    if isCollision (enemy_bullet, player) :
                #Reset the bullet 
                enemy_bullet.hideturtle()
                enemy_bulletstate = "ready" 
                enemy_bullet.setposition (0, -400) #moves the bullet down so that we dont have any positive collisions 
                os.system ("afplay explosion.mp3&") #without & the program will pause 
               
               #Reset the player:
                player.setposition (0, -250) #resets the player at the middle section of the bottom part of the screen 

                lives.clear() #because we don't want to keep adding turtles 
                for i in range (number_lives):
                    lives.append(turtle.Turtle)

                xlives = -280

                for live in lives:

                    live = turtle.Turtle()
                    live.penup()
                    live.speed(0)
                    live.shape("lives2.gif")
                    live.shapesize(100,100)
                    y = -280
                    live.setposition(xlives,y)
                    xlives += 40
                    live.hideturtle() #The turtles are actually overlapping
                    #on top of one another but we won't see it because they are hidden


                number_lives -= 1 #the number of turtles we want to create gets smaller in number 
                live.showturtle() #of all the black hearts overlapping, the last one in the list of lives will be shown each time 

We can see that when the enemy_bullet hits the player, the player is reset to the bottom-middle section of the game screen. We then use the same lives list and number_lives variable to create the black hearts/lives. Since the lives list was initially occupied by the live turtles, we need to clear it for the black hearts to be appended. The black hearts are created in a similar manner as the lives. The only difference is that each time the enemy_bullet collides with the player, the black hearts are created but hidden and only the last black heart in the lives list will be shown. The black heart is actually overlapping the previous live turtle, and for each collision, each of the live turtles created earlier in the program will be overlapped by a black heart. This effect is to show that the player has lost a life when the enemy_bullet hits the player. 

18) Adding the mystery ship or the mothership. Just like in the actual space invaders, the mystery ship will appear at some point of time. Since this the game is at its developing stage, I am only going to make the mystery ship appear when the player achieve a certain score. So, similar to the other turtles we have created, we have to register the shape that we want to use. 

        turtle.register_shape ("mothership.gif")
 
19) Creating the mothership: 

        #Creating the mothership
        
        mothership = turtle.Turtle()
        mothership.color("red")
        mothership.shape("mothership.gif")
        mothership.penup()
        mothership.speed(0)
        mothership.setposition(-260, 260)
        mothership.hideturtle()

        mothershipspeed = 10
        
20) Moving the mothership at a certain score:

        #Move the mothership
        if score == 10:
            mothership.showturtle()
            x = mothership.xcor()
            x+= mothershipspeed
            mothership.setx(x)
            
21) Checking if the mothership has reached the border and making sure that disappears at the border: 


         #Check if mothership has left the game(reached the other side of the border)
            if mothership.xcor() > 250:
                mothership.hideturtle() 
            
22) Check for collision between the player bullet and the mothership: 


        if isCollision (bullet, mothership) :
                    #Reset the bullet 
                    bullet.hideturtle()
                    bulletstate = "ready" 
                    bullet.setposition (0, -400) 
                    os.system ("afplay explosion.mp3&") #without & the program will pause 
                    mothership.hideturtle()
                    #Draw the score 
                    os.system ("afplay score.mp3&")
                    score += 50
                    scorestring = "Score: " + str(score)
                    score_pen.clear()
                    score_pen.write (scorestring, False, align = "left", font=("Arial",25, "normal"))

Definitely, when we hit the mothership, we would want to make the player earn more points than hitting the normal invaders 

23) Now that we have created the lives, mothership, enemy bullets, have a game over sign would be an interesting addition to the game to show that the user has lost. Similar to creating other turtles in the game, we need to register the shape of our "Game Over" sign of we are using a gif file from our folder:

        turtle.register_shape ("gameover.gif")
        
We also have to create a condition where the "game over" sign will be shown:


        
    if isCollision (player, enemy) or number_lives == 0:
        player.hideturtle()
        enemy.hideturtle()
        print ("Game over")
        gameover = turtle.Turtle()
        gameover.shape("gameover.gif")
        gameover.speed(0)
        gameover.setposition (0,0)
        gameover.penup()
        player.setposition (-400, 0)
        break #will break us out of the main loop 




    






    

    
        
        
 

