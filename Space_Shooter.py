
# ! Using Python 3.8.6
# ! Changes may be required if using older python versions.

# TODO: Making a Space Shooter Game using Pygame.

# Importing required modules
import pygame
import numpy # ? Numpy needs to be installed using pip, type `pip install pygame` in command prompt to install it.
# * import random 
# ? Use it if numpy not available, replace every numpy.random... by random...
from threading import Timer
import sys
from tkinter import *
import tkinter.messagebox as Alert

# Assigning variables for set the game running or exit it
Game_Running = False
Game_Quit = True

# Creating start window
Window = Tk()
Window.title("Space_Shooter")
Window.geometry("1000x750+270+45")
Window.maxsize(1000, 750)
Window.minsize(1000, 750)
Window.configure(background = "Black")

# Try to load the images if the are at the given location
try:
    # Loading all the pictures
    Frame_Icon = PhotoImage(file = "Images\\Space_Shooter_Icon.png")
    Icon = pygame.image.load("Images\\Space_Shooter_Icon.jpg")
    Player_Ship_Image = pygame.image.load("Images\\Player_Space_Ship.jpg")
    Enemy_Ship_Image = pygame.image.load("Images\\Enemy_Space_Ship.jpg")
    Player_Missile_Image = pygame.image.load("Images\\Player_Missile_Image.png")
    Enemy_Missile_Image = pygame.image.load("Images\\Enemy_Missile_Image.png")

# If files are not at given location...
except Exception as Error:
    
    # Give an error box and exit the program
    Alert.showerror("Files not Found", "Error: " + str(Error) + "\nRequired Files not found at destination.")
    sys.exit()

# Setting the icon and Canvas for showing the objects
Window.iconphoto(False, Frame_Icon)
Can = Canvas(Window, width = 1000, height = 750, background = "Black")
Can.pack()

# Creating an empty list for objects and their speed, and a colour list and setting number of objects
Objects = []
Object_Speed_X = []
Object_Speed_Y = []
Colour_List = ["White", "Red", "Aqua", "Blue", "Deep pink", "Green", "Yellow", "Purple", "Orangered"]
Number_OF_Objects = 540

# Setting text to show up on screen
Can.create_text(495, 27, font = ("Times New Roman", 45), text = "Space Shooter", fill = "White")
Can.create_text(495, 630, font = ("Times New Roman", 18), text = "Press 'Enter' to start the game!", fill = "White")
Can.create_text(495, 690, font = ("Times New Roman", 18), text = "Press 'F1' for Help!", fill = "White")

# Creating Information variables to show when the user clicks for help
Info_Information = [
    "Welcome to the Space Shooter Game!",
    "Press 'F2' for About.",
    "Press 'F3' for Game Controls",
    "Press 'F4' for Other Informations"
]

About_Information = [
    "Project-Name:   Space_Shooter",
    "Developer:          Ansh Malviya",
    "Mode:                 Multi Player",
    "Version:               1.0",
    "Language:          Python",
    "(c) 2021 - Ansh", 
    "All rights reserved."
]

Game_Controls_Information = [
    "Controls before starrting the Game:",
    "   'Enter':                 Start the Game.",
    "   'F1, F2, F3, F4':    Help.",
    "Controls after the Game Starts:",
    "   'Right-Key':         Move the Player Ship right.",
    "   'Left-Key':            Move the Player Ship left.",
    "   'Up-Key':              Fire the Missile."
]

Play_Information = [
    "After starting the game, 5 enemies ships and a player ship will appear.",
    "The Enemies will continously burst fire on you.",
    "Save your ship from these missiles by moving your ship.",
    "Keep firing missiles to bring down the Enemy ships.",
    "Your Missiles would be limited to 5 and will recharge after every 3 seconds.",
    "Each Enemy is worth 10 points!",
    "Your highscore will be saved at a local destination. \n",
    "Objective: To kill as many enemies as possible before they gets below your screen or their missile hits your ship.",
    "\n",
    "Best of Luck!"
]

# Starting the game when the user hits enter
def Start_Game(event):
    
    global Game_Running
    global Game_Quit
    
    Window.unbind("<Return>")
    Window.destroy()
    Game_Running = True
    Game_Quit = False

Window.bind("<Return>", Start_Game)

# Creating 'Number_Of_Object' times Objects to show up on screen
for i in range(Number_OF_Objects):
    x = numpy.random.randint(0, 990)
    y = numpy.random.randint(0, 735)
    Colour = numpy.random.choice(Colour_List)
    Speed = numpy.random.randint(1, 6)
    random_x = numpy.random.randint(1, 3)
    random_y = numpy.random.randint(1, 3)
    Random_size = numpy.random.randint(1, 6)
    
    if random_x == 1:
        Object_Speed_X.append(Speed)
    else:
        Object_Speed_X.append(-Speed)
    if random_y == 1:
        Object_Speed_Y.append(Speed)
    else:
        Object_Speed_Y.append(-Speed)
    
    Object = Can.create_oval(x, y, x + Random_size, y + Random_size, outline = Colour, fill = Colour)
    Objects.append(Object)

# Moving the Objects
def Move_Objects(Objects):
    for Object in Objects:
        
        x = Object_Speed_X[Objects.index(Object)]
        y = Object_Speed_Y[Objects.index(Object)]
        
        x1, y1, x2, y2 = Can.coords(Object)
        
        if x1 <= 0 or x2 >= 1000:
            x = -x
        if y1 <= 0 or y2 >= 750:
            y = -y
        
        Can.move(Object, x, y)
        
        Object_Speed_X[Objects.index(Object)] = x
        Object_Speed_Y[Objects.index(Object)] = y
        
        Colour = numpy.random.choice(Colour_List)
        
        Can.itemconfig(Object, fill = Colour, outline = Colour)
        
    Window.after(27, lambda: Move_Objects(Objects))

# Call Move_Objects function
Move_Objects(Objects)

# Showing Info, opening a tkinter.messagebox.showinfo() box
def Show_Info(Title, Information):
    
    Alert.showinfo(Title, "\n".join(Information))

# Binding the keys to show info
Window.bind("<F1>", lambda event: Show_Info("Help", Info_Information))
Window.bind("<F2>", lambda event: Show_Info("About", About_Information))
Window.bind("<F3>", lambda event: Show_Info("Game Controls", Game_Controls_Information))
Window.bind("<F4>", lambda event: Show_Info("How to Play", Play_Information))

# Putting the start screen in a mainloop
Window.mainloop()

if Game_Quit == True:
    sys.exit()

# Try to create an external file to save the Highscore setting default highscore as 0
try:
    Highscore_File = open("Space_Shooter_Highscore.txt", "x")
    Highscore_File = open("Space_Shooter_Highscore.txt", "w")
    Highscore_File.write("0")

# Ignore if file already exists
except Exception as Error:
    pass

# Taking the Highscore from the file
Highscore_File = open("Space_Shooter_Highscore.txt", "r")
Highscore = int(Highscore_File.read())

pygame.init()
Window = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Space_Shooter")
pygame.display.set_icon(Icon)

# Defining Score Variable
Score = 0

# Rescaling all the pictures to smaller size
Player_Ship_Image = pygame.transform.scale(Player_Ship_Image, (30, 30))
Enemy_Ship_Image = pygame.transform.scale(Enemy_Ship_Image, (30, 30))
Player_Missile_Image = pygame.transform.scale(Player_Missile_Image, (10, 10))
Enemy_Missile_Image = pygame.transform.scale(Enemy_Missile_Image, (10, 10))

pygame.display.set_icon(Icon)

# Setting a variable to control frame rate
Frame_Rate = pygame.time.Clock()

# Setting Initial Position of Player Ship
Player_x = 485
Player_y = 690

# Creating lists for storing enemies, its speed and missiles for both Player and Enemies and Number of missiles available as an int
Enemies = []
Enemy_Speed = []
Player_Missiles = []
Enemy_Missiles = []
Missiles_Available = 5

# Creating Score panel
Score_Font = pygame.font.SysFont("Times New Roman", 36)
Score_Text = Score_Font.render("Score: " + str(Score), True, "White")
Score_Rectangle = Score_Text.get_rect()
Score_Rectangle.center = (66, 30)

# Creating Highscore panel
Highscore_Font = pygame.font.SysFont("Times New Roman", 36)
Highscore_Text = Highscore_Font.render("Highscore: " + str(Highscore), True, "White")
Highscore_Rectangle = Highscore_Text.get_rect()
Highscore_Rectangle.center = (882, 30)

# Updating window
pygame.display.flip()

# Creating text to display on the initial screen
Font = pygame.font.SysFont("Times New Roman", 54, italic = True)
Text = Font.render("Space Shooter", True, "White")
Text_Rectangle = Text.get_rect()
Text_Rectangle.center = (500, 50)

# Function to create enemies for a number of times and put them and their speeds in lists, it will also be used to recreate the Enemies
def Create_Enemies(Number):
    for i in range(Number):
        x = numpy.random.randint(780)
        y = numpy.random.randint(20, 270)
        Enemy = pygame.draw.rect(Window, "RED", pygame.Rect(x, y, 30, 30))
        Enemies.append(Enemy)
        Window.blit(Enemy_Ship_Image, Enemy)
        
        Enemy_Speed.append(numpy.random.choice([3, -3]))

# Moving Enemies 
def Move_Enemies(Enemy):
    x1 = Enemy.left
    x2 = Enemy.right
    y = Enemy.top
    
    # Checking if Enemies hit frame edges
    if x1 <= 0 or x2 > 999:
        
        # Changing their direction
        Enemy_Speed[Enemies.index(Enemy)] = -Enemy_Speed[Enemies.index(Enemy)]
        
    # Creating New Enemy with new position
    New_Enemy = pygame.draw.rect(Window, "RED", pygame.Rect(x1 + Enemy_Speed[Enemies.index(Enemy)], y, 30, 30))
    
    # Putting image on the Enemy Surface
    Window.blit(Enemy_Ship_Image, New_Enemy)
    
    # Replacing the Enemy with new Enemy
    Enemies[Enemies.index(Enemy)] = New_Enemy

def Move_Enemies_Down():
    
    global Game_Running
    
    # To check for Each Enemy
    for Enemy in Enemies:
        
        x1 = Enemy.left
        y1 = Enemy.top
        
        # Recreating enemy with new (vertical) position
        New_Enemy = pygame.draw.rect(Window, "RED", pygame.Rect(x1 + Enemy_Speed[Enemies.index(Enemy)], y1 + 15, 30, 30))

        # Replacing Enemy with new enemy
        Enemies[Enemies.index(Enemy)] = New_Enemy
        
    # Recalling the function after 3 seconds if game is STILL RUNNING
    if Game_Running == True:
        Gravity = Timer(3, Move_Enemies_Down)
        Gravity.start()

def Fire_Missile_Player():
    
    global Missiles_Available
    
    # Reducing available missiles by 1
    Missiles_Available -= 1
    
    x1 = Player_Ship.left
    
    # Creating new missile rectangle
    Missile = pygame.draw.rect(Window, "YELLOW", pygame.Rect(x1 + 10, 675, 10, 10))
    
    # Putting image on the Missile Surface
    Window.blit(Enemy_Ship_Image, Missile)
    
    Player_Missiles.append(Missile)
    
# Moving Missile fired by player
def Move_Missiles_Player(Missile):
    
    x1 = Missile.left
    y1 = Missile.top
    Previous_Missile = Player_Missiles.index(Missile)
    
    # Recreacting Missile with new position
    Missile = pygame.draw.rect(Window, "YELLOW", pygame.Rect(x1, y1 - 3, 10, 10))
    
    # Putting image on the Missile Surface
    Window.blit(Player_Missile_Image, Missile)
    
    Player_Missiles[Previous_Missile] = Missile
    
    x1 = Missile.left
    y1 = Missile.top
    
    # Checking if Missile hit top edge of frame or the enemy
    if y1 <= 0 or Collision_Occurs_Enemy_Missiles(Missile):
        
        # Removing missile from list
        Player_Missiles.pop(Previous_Missile)

# Checking if missile fired by player hit the enemy
def Collision_Occurs_Enemy_Missiles(Missile):
    
    global Score
    Mx1, My1, Mx2, My2 = Missile.left, Missile.top, Missile.right, Missile.bottom
    
    for Enemy in Enemies:
        
        Ex1, Ey1, Ex2, Ey2 = Enemy.left, Enemy.top, Enemy.right, Enemy.bottom
        
        # Checking collision
        if Mx1 > Ex1 and Mx1 < Ex2 or Mx2 > Ex1 and Mx2 < Ex2:
            if My1 > Ey1 and My1 < Ey2 or My2 > Ey1 and My2 < Ey2:
                # ? If Collision happens...
                
                # Adding 10 to score
                Score += 10
                
                # Removing Enemy and its speed from list
                Enemy_Speed.pop(Enemies.index(Enemy))
                Enemies.pop(Enemies.index(Enemy))

                # Recreating 0, 1 or 2 (chosen as random) enemies
                Create_Enemies(numpy.random.randint(0, 3))
                
                # Returing True
                return True
            
    # Returning False, if collision occurs
    return False

# Adding Missile to available number of missiles, it its less than 5
def Add_Missiles():
    
    global Missiles_Available
    
    if Missiles_Available < 5:
        Missiles_Available += 1
        
    # Recalling the function after 3 seconds
    if Game_Running == True:
        Add_Missile = Timer(3, Add_Missiles)
        Add_Missile.start()

# Displaying Number of Missiles available as rectangles
def Display_Number_Of_Missiles(Number_Of_Missiles):
    
    # Creating rectangles as many available missiles
    for i in range(Number_Of_Missiles):
        
        y = 654
        
        Missile = pygame.draw.rect(Window, "RED", pygame.Rect(975, y + 20*i, 10, 10))

# Firing Missiles by Enemy (automatically every after 1 second)
def Enemy_Fire_Missile():

    # Selecting a random enemy to fire a missile
    Enemy = Enemies[numpy.random.choice(len(Enemies))]
    
    x = Enemy.left
    y = Enemy.top
    
    Missile = pygame.draw.rect(Window, "Yellow", pygame.Rect(x + 10, y + 10, 10, 10))
    
    Enemy_Missiles.append(Missile)
    
    # Recalling the function after a second if game is STILL RUNNING
    if Game_Running == True:
        Enemy_Fire = Timer(1, Enemy_Fire_Missile)
        Enemy_Fire.start()

# Move Missile fired by the enemy
def Move_Enemy_Missile(Missile):
    
    global Game_Running
    global Highscore
    global Score
    
    x1 = Missile.left
    y1 = Missile.top
    Previous_Missile = Enemy_Missiles.index(Missile)
    
    # Recreating missile with new position of missile
    Missile = pygame.draw.rect(Window, "YELLOW", pygame.Rect(x1, y1 + 3, 10, 10))
    Window.blit(Enemy_Missile_Image, Missile)
    
    Enemy_Missiles[Previous_Missile] = Missile
    
    x1 = Missile.left
    y1 = Missile.bottom
    
    # Removing the missile if it reaches the bottom of the frame
    if y1 >= 747:
        Enemy_Missiles.pop(Previous_Missile)
        
    # Checking collition of missile with player
    if Collision_Occurs_Player_Missiles(Missile):
        
        # If true, quit the game
        Game_Running = False
        
        if Highscore < Score:
            
            try:
                Highscore_File = open("Space_Shooter_Highscore.txt", "w")
                Highscore_File.write(str(Score))
            
            except Exception as Error:
                print(Error)

# Checking collision of Player and Missile fired by enemy
def Collision_Occurs_Player_Missiles(Missile):
    
    Mx1, My1, Mx2, My2 = Missile.left, Missile.top, Missile.right, Missile.bottom

    Px1, Py1, Px2, Py2 = Player_Ship.left, Player_Ship.top, Player_Ship.right, Player_Ship.bottom
    
    # Checking collision
    if Mx1 > Px1 and Mx1 < Px2 or Mx2 > Px1 and Mx2 < Px2:
        if My1 > Py1 and My1 < Py2 or My2 > Py1 and My2 < Py2:
            # ? If Collision happens...
            
            # Remove the missile from list
            Enemy_Missiles.pop(Enemy_Missiles.index(Missile))

            # Return True
            return True
        
    # Return False, if collision do not occur
    return False

# Creating 5 enemies, initially
Create_Enemies(5)

# Staring times for moving enemies down
Gravity = Timer(3, Move_Enemies_Down)
Gravity.start()

# Starting times to add missiles to available missiles
Add_Missile = Timer(3, Add_Missiles)
Add_Missile.start()

# Starting times to start enemy firing
Enemy_Fire = Timer(1, Enemy_Fire_Missile)
Enemy_Fire.start()

# Running main game loop
while Game_Running == True:
    
    # Setting game frame rate
    Frame_Rate.tick(90)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exiting game
            Game_Running = False
            Game_Quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player_x -= 15
            if event.key == pygame.K_RIGHT:    
                Player_x += 15
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                if Missiles_Available:
                    Fire_Missile_Player()
                
    # Filling black on the game window
    Window.fill("BLACK")
    
    # Moving the Player ship, vertically
    Event = pygame.key.get_pressed()
    Player_x += Event[pygame.K_RIGHT]*2 - Event[pygame.K_LEFT]*2
    
    # Preventing Player ship to move out of game window
    if Player_x < 0:
        Player_x = 0
    if Player_x > 970:
        Player_x = 970
    
    # Moving each Enemy
    for Enemy in Enemies:
        Move_Enemies(Enemy)
        
        # Stopping the game if an enemy reaches the bottom edge of the screen
        if Enemy.bottom >= 747:
            Game_Running = False
        
    # Moving each missile fired by player
    for Missile in Player_Missiles:
        Move_Missiles_Player(Missile)
        
    # Moving Each missile fired by enemy
    for Missile in Enemy_Missiles:
        Move_Enemy_Missile(Missile)
        
    # Checking there are less than 3 enemies left, if so, recreate 3 more enemies
    if len(Enemies) < 3:
        Create_Enemies(3)
        # This prevents terminating the gtame without player's mistake by getting 0 enemies
        
    # Displaying number of missiles available
    Display_Number_Of_Missiles(Missiles_Available)
    
    # Creating and moving the Player ship and putting image on it
    Player_Ship = pygame.draw.rect(Window, "BLUE", pygame.Rect(Player_x, Player_y, 30, 30))
    Window.blit(Player_Ship_Image, Player_Ship)
    
    # Putting Score panel on surface of the window
    Score_Text = Score_Font.render("Score: " + str(Score), True, "White")
    Window.blit(Score_Text, Score_Rectangle)
    
    # Putting Highscore panel on surface of the window
    Highscore_Text = Highscore_Font.render("Highscore: " + str(Highscore), True, "White")
    Window.blit(Highscore_Text, Highscore_Rectangle)
    
    # Updating game window
    pygame.display.flip()

Window.fill("BLACK")

while Game_Quit == False:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Quit = True
    
    Window.blit(Text, Text_Rectangle)

    Game_Over_Font = pygame.font.SysFont("Times New Roman", 36)
    Game_Over_Text = Game_Over_Font.render("Game Over", True, "RED")
    Game_Over_Text_Rectangle = Game_Over_Text.get_rect()
    Game_Over_Text_Rectangle.center = (500, 450)
    Window.blit(Game_Over_Text, Game_Over_Text_Rectangle)
    
    # Creating Score panel
    Score_Font = pygame.font.SysFont("Times New Roman", 36)
    Score_Text = Score_Font.render("Score: " + str(Score), True, "BLUE")
    Score_Rectangle = Score_Text.get_rect()
    Score_Rectangle.center = (500, 480)
    Window.blit(Score_Text, Score_Rectangle)
    
    pygame.display.flip()
    
    Window.fill("BLACK")