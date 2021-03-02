
# ! Using Python 3.8.6
# ! Changes may be required if using older python versions.

# TODO: Making a Space Shooter Game using Pygame.

# Importing required modules
import json
import sys
import tkinter.messagebox as Alert
from threading import Timer
from tkinter import (Button, Canvas, Frame, Label, PhotoImage, Scrollbar, Tk,Toplevel, ttk)
import numpy  # ? Numpy needs to be installed using pip, type `pip install pygame` in command prompt to install it.
# * import random 
# ? Use it if numpy not available, replace every numpy.random... by random...
import pygame
from PIL import Image, ImageTk

# Checking if this file is running as the main file, else terminationg the program
# These two lines can be skipped
if __name__ != "__main__":
    sys.exit()

# Assigning variables for set the game running or exit it
Game_Running = False
Game_Quit = True

# Trying to create an external JSON file for storing configurations
try:
    # Creating Default Configurations (For the program to run for the first time)
    Configurations = {
        "Appearence": {
            "Start": {
                "Change_Object_Colours": True,
                "Background_Colour": "#000014"
            },
            "Game": {
                "Player_Ship_Image": "Images\\Player_Space_Ship(1).png",
                "Enemy_Ship_Image": "Images\\Enemy_Space_Ship(3).png",
                "Boss_Ship_Image": "Images\\Boss_Space_Ship(1).png",
                "Star_Appearence": "Stars with Movement",
                "Background_Colour": "#000014"
            }
        },
    "Game_Functionings":
        {
            "Player_Ship_Speed": 4
        }
    }
    
    # Converting Python statements (Dict) to JSON statements (String)
    Configurations = json.dumps(Configurations)
    
    # Creating a new JSON file and storing the default configurations in it
    Configuration_File = open("Space_Shooter_Configurations.json", "x")
    Configuration_File = open("Space_Shooter_Configurations.json", "w")
    Configuration_File.write(Configurations)

# Ignore if file already exists
except:
    pass

# Reading the JSON file and converting JSON statements (String) to python statements (Dict)
Configuration_File = open("Space_Shooter_Configurations.json", "r")
Configurations = json.loads(Configuration_File.read()) # Storing value in the variable

# Creating start window
Window = Tk()
Window.title("Space_Shooter")
Window.geometry("1000x750+270+45")
Window.maxsize(1000, 750)
Window.minsize(1000, 750)
Window.configure(background = Configurations["Appearence"]["Start"]["Background_Colour"]) # Setting background as defined in the dict

# Try to load the images if the are at the given location
try:
    # Loading all the pictures
    Frame_Icon = PhotoImage(file = "Images\\Space_Shooter_Icon(1).png")
    Icon = pygame.image.load("Images\\Space_Shooter_Icon(1).png")
    Player_Ship_Image = pygame.image.load(Configurations["Appearence"]["Game"]["Player_Ship_Image"])
    Enemy_Ship_Image = pygame.image.load(Configurations["Appearence"]["Game"]["Enemy_Ship_Image"])
    Player_Missile_Image = pygame.image.load("Images\\Player_Missile_Image.png")
    Enemy_Missile_Image = pygame.image.load("Images\\Enemy_Missile_Image.png")
    Boss_Ship_Image = pygame.image.load(Configurations["Appearence"]["Game"]["Boss_Ship_Image"])
    Settings_Icon = Image.open("Images\\Settings_Icon.jpg")
    Settings_Icon_Inverted = Image.open("Images\\Settings_Icon_Inverted.jpg")

# If files are not at given location...
except Exception as Error:
    
    # ...Give an error box and exit the program
    Alert.showerror("Files not Found", "Error: " + str(Error) + "\nRequired Files not found at destination.")
    sys.exit()

# Converting Image to PhotoImage and resizing it for the settings window
Settings_Window_Icon = ImageTk.PhotoImage(Settings_Icon)
Settings_Icon = Settings_Icon.resize((45, 45), Image.ANTIALIAS) 
Settings_Icon_Inverted = Settings_Icon_Inverted.resize((45, 45), Image.ANTIALIAS)
Settings_Icon = ImageTk.PhotoImage(Settings_Icon)
Settings_Icon_Inverted = ImageTk.PhotoImage(Settings_Icon_Inverted)

# Function to open Settings Window
def Open_Settings():
    # Declaring Configurations as global variable
    global Configurations
    
    # Creating Settings Window
    Settings_Window = Toplevel()
    Settings_Window.focus_set()
    Settings_Window.config(background = "#000014")
    Settings_Window.title("Space Shooter: Settings")
    Settings_Window.geometry("810x846+360+18")
    Settings_Window.minsize(810, 846)
    Settings_Window.iconphoto(False, Settings_Window_Icon)
    
    # Creating a Frame to insert other widgets
    # You may skip these two lines and replace 'Setting_Frame' to 'Settings_Window'
    Setting_Frame = Frame(Settings_Window, height = 846, width = 810, background = "#000014")
    Setting_Frame.pack()
    
    # Trying to create PhotoImage for all skins... if available at given location
    try:
        Player_1 = Image.open("Images\\Player_Space_Ship(1).png")
        Player_1 = Player_1.resize((60, 60), Image.ANTIALIAS)
        Player_1 = ImageTk.PhotoImage(Player_1)
        Player_2 = Image.open("Images\\Player_Space_Ship(2).png")
        Player_2 = Player_2.resize((60, 60), Image.ANTIALIAS)
        Player_2 = ImageTk.PhotoImage(Player_2)
        Player_3 = Image.open("Images\\Player_Space_Ship(3).png")
        Player_3 = Player_3.resize((60, 60), Image.ANTIALIAS)
        Player_3 = ImageTk.PhotoImage(Player_3)
        Enemy_1 = Image.open("Images\\Enemy_Space_Ship(1).png")
        Enemy_1 = Enemy_1.resize((60, 60), Image.ANTIALIAS)
        Enemy_1 = ImageTk.PhotoImage(Enemy_1)
        Enemy_2 = Image.open("Images\\Enemy_Space_Ship(2).png")
        Enemy_2 = Enemy_2.resize((60, 60), Image.ANTIALIAS)
        Enemy_2 = ImageTk.PhotoImage(Enemy_2)
        Enemy_3 = Image.open("Images\\Enemy_Space_Ship(3).png")
        Enemy_3 = Enemy_3.resize((60, 60), Image.ANTIALIAS)
        Enemy_3 = ImageTk.PhotoImage(Enemy_3)
        Boss_1 = Image.open("Images\\Boss_Space_Ship(1).png")
        Boss_1 = Boss_1.resize((120, 60), Image.ANTIALIAS)
        Boss_1 = ImageTk.PhotoImage(Boss_1)
        Boss_2 = Image.open("Images\\Boss_Space_Ship(2).png")
        Boss_2 = Boss_2.resize((120, 60), Image.ANTIALIAS)
        Boss_2 = ImageTk.PhotoImage(Boss_2)
    
    # If the files are not at Given Location...
    except Exception as Error:
        
        # Show an error, destroy the Settings window and get out of the function
        Alert.showerror("Files not Found", "Error: " + str(Error) + "\nRequired files not found at destination.")
        Settings_Window.destroy()
        return
        # ? Even if some of the images were already opened before, we are again opening all so that if any of these images is missing but not selected by the user, it won't affect the main program
        
    # Creating a local variable to store the changes made be the user before saving and overwriting the previous settings
    Settings_Config = Configurations
    
    # Creating widgets for settings window
    Title = Label(Setting_Frame, text = "Settings", background = "#000014", foreground = "#FFFFFF", font = ("Times New Roman", 36))
    Title.place(x = 333, y = 3)
    Appear_Title = Label(Setting_Frame, text = "Appearence", background = "#000014", foreground = "#FFFFFF", font = ("Times New Roman", 30, "bold", "italic", "underline"))
    Appear_Title.place(x = 3, y = 54)
    Start_Appear_Title = Label(Setting_Frame, text = "Start Window", background = "#000014", foreground = "#FFFFFF", font = ("Times New Roman", 24, "bold", "italic"))
    Start_Appear_Title.place(x = 27, y = 108)
    Change_Obj_Col_Label = Label(Setting_Frame, text = "Change Object Colour with every Movement:", foreground = "#FFFFFF", background = "#000014", font = ("Times New Roman", 18))
    Change_Obj_Col_Label.place(x = 54, y = 153)
    Change_Obj_Col_Box = ttk.Combobox(Setting_Frame, values = ("Yes", "No"), font = ("Times New Roman", 12, "italic"), state = "readonly")
    Change_Obj_Col_Box.place(x = 567, y = 150)
    Start_Win_Bg_Label = Label(Setting_Frame, text = "Start Window Background Colour:", foreground = "#FFFFFF", background = "#000014", font = ("Times New Roman", 18))
    Start_Win_Bg_Label.place(x = 54, y = 189)
    Start_Win_Bg_Box = ttk.Combobox(Setting_Frame, values = ("Space_Blue", "Black"), font = ("Times New Roman", 12, "italic"), state = "readonly")
    Start_Win_Bg_Box.place(x = 567, y = 186)
    Game_Appear_Title = Label(Setting_Frame, text = "After Game Starts", background = "#000014", foreground = "#FFFFFF", font = ("Times New Roman", 24, "bold", "italic"))
    Game_Appear_Title.place(x = 27, y = 234)
    Player_Label = Label(Setting_Frame, text = "Player Ship Skin:", background = "#000014", foreground = "#FFFFFF", font = ("Times New Roman", 18)).place(x = 54, y = 288)
    Player_Label = Label(Setting_Frame, text = "Enemy Ship Skin:", background = "#000014", foreground = "#FFFFFF", font = ("Times New Roman", 18)).place(x = 54, y = 378)
    Player_Label = Label(Setting_Frame, text = "Boss Ship Skin:", background = "#000014", foreground = "#FFFFFF", font = ("Times New Roman", 18)).place(x = 54, y = 468)
    Player_1_Button = Button(Setting_Frame, image = Player_1)
    Player_1_Button.place(x = 261, y = 279)
    Player_2_Button = Button(Setting_Frame, image = Player_2)
    Player_2_Button.place(x = 360, y = 279)
    Player_3_Button = Button(Setting_Frame, image = Player_3)
    Player_3_Button.place(x = 459, y = 279)    
    Enemy_1_Button = Button(Setting_Frame, image = Enemy_1)
    Enemy_1_Button.place(x = 261, y = 369)
    Enemy_2_Button = Button(Setting_Frame, image = Enemy_2)
    Enemy_2_Button.place(x = 360, y = 369)
    Enemy_3_Button = Button(Setting_Frame, image = Enemy_3)
    Enemy_3_Button.place(x = 459, y = 369)
    Boss_1_Button = Button(Setting_Frame, image = Boss_1)
    Boss_1_Button.place(x = 261, y = 459)
    Boss_2_Button = Button(Setting_Frame, image = Boss_2)
    Boss_2_Button.place(x = 399.6, y = 459)
    Star_Appearence_Label = Label(Setting_Frame, text = "Star Appearence:", foreground = "#FFFFFF", background = "#000014", font = ("Times New Roman", 18))
    Star_Appearence_Label.place(x = 54, y = 540)
    Star_Appearence_Box = ttk.Combobox(Setting_Frame, values = ("No Stars", "Stars but no Movement", "Stars with Movement"), state = "readonly", font = ("Times New Roman", 12, "italic"))
    Star_Appearence_Box.place(x = 567, y = 537)
    Game_Win_Bg_Label = Label(Setting_Frame, text = "Game Window Background Colour:", foreground = "#FFFFFF", background = "#000014", font = ("Times New Roman", 18))
    Game_Win_Bg_Label.place(x = 54, y = 576)
    Game_Win_Bg_Box = ttk.Combobox(Setting_Frame, values = ("Space_Blue", "Black"), font = ("Times New Roman", 12, "italic"), state = "readonly")
    Game_Win_Bg_Box.place(x = 567, y = 576)
    Game_Func_Title = Label(Setting_Frame, text = "Game Functionings", background = "#000014", foreground = "#FFFFFF", font = ("Times New Roman", 30, "bold", "italic", "underline"))
    Game_Func_Title.place(x = 3, y = 630)
    Player_Speed_Label = Label(Setting_Frame, text = "Player Ship Speed:", foreground = "#FFFFFF", background = "#000014", font = ("Times New Roman", 18))
    Player_Speed_Label.place(x = 54, y = 690)
    Player_Speed_Box = ttk.Combobox(Setting_Frame, values = ("Low", "Medium (Recommanded)", "High"), state = "readonly", font = ("Times New Roman", 12, "italic"))
    Player_Speed_Box.place(x = 270, y = 687)
    
    # A function to return background or current value for widgets wose value is present in the Configurations variable (or the JSON file)
    # For example, if Player_Space_Ship(3).png is defined as the Player skin in the JSON file, it will return 'RED' colour for it
    def Show_Curen_Config(Widget, Character, Image_Path = None):
        # Only for Buttons
        if Widget == "Button":
            if Character == "Player":
                if Configurations["Appearence"]["Game"]["Player_Ship_Image"] == Image_Path:
                    return "Red"
                else: 
                    return "White"
            if Character == "Enemy":
                if Configurations["Appearence"]["Game"]["Enemy_Ship_Image"] == Image_Path:
                    return "Red"
                else: 
                    return "White"
            if Character == "Boss":
                if Configurations["Appearence"]["Game"]["Boss_Ship_Image"] == Image_Path:
                    return "Red"
                else: 
                    return "White"
                
        # Only for Comboboxes
        if Widget == "Combobox":
            if Character == "#000000" or Character == False or Character == "Stars but no Movement" or Character == 4:
                return 1
            elif Character == "#000014" or Character == True or Character == "No Stars" or Character == 2:
                return 0
            else: 
                return 2
    
    # Function to update Settings_Config variable and the appearence of the button clicked
    def Change_Settings(Character, Name, Number = 1):
        
        if Character == "Player":
            Player_1_Button.configure(background = "White")
            Player_2_Button.configure(background = "White")
            Player_3_Button.configure(background = "White")
            Name.configure(background = "Red")
            Settings_Config["Appearence"]["Game"]["Player_Ship_Image"] = "Images\\Player_Space_Ship(" + str(Number) + ").png"
        if Character == "Enemy":
            Enemy_1_Button.configure(background = "White")
            Enemy_2_Button.configure(background = "White")
            Enemy_3_Button.configure(background = "White")
            Name.configure(background = "Red")
            Settings_Config["Appearence"]["Game"]["Enemy_Ship_Image"] = "Images\\Enemy_Space_Ship(" + str(Number) + ").png"
        if Character == "Boss":
            Boss_1_Button.configure(background = "White")
            Boss_2_Button.configure(background = "White")
            Name.configure(background = "Red")
            Settings_Config["Appearence"]["Game"]["Boss_Ship_Image"] = "Images\\Boss_Space_Ship(" + str(Number) + ").png"
    
    # Function to save changes made to Settings_Config and overwriting it on previous settings in JSON file
    # Most changes will take place the next time game starts
    def Save_Configures():
        
        # Asking confirmation to save files
        Confirmation = Alert.askquestion("Save changes?", "Saving changes will overwrite the previous configurations. \nDo you wish to continue?", icon = "warning")
        
        # If confirmed, proceed, else, exit the fuction
        if Confirmation == "yes":
            pass
        else:
            return
        
        # Overwriting the Settings_Config variable according to the current values of the Comboboxes
        if Change_Obj_Col_Box.get() == "Yes":
            Settings_Config["Appearence"]["Start"]["Change_Object_Colours"] = True
        else:
            Settings_Config["Appearence"]["Start"]["Change_Object_Colours"] = False
        if Start_Win_Bg_Box.get() == "Black":
            Settings_Config["Appearence"]["Start"]["Background_Colour"] = "#000000"
        else:
            Settings_Config["Appearence"]["Start"]["Background_Colour"] = "#000014"
        Settings_Config["Appearence"]["Game"]["Star_Appearence"] = Star_Appearence_Box.get()
        if Player_Speed_Box.get() == "High":
            Settings_Config["Game_Functionings"]["Player_Ship_Speed"] = 8
        elif Player_Speed_Box.get() == "Low":
            Settings_Config["Game_Functionings"]["Player_Ship_Speed"] = 2
        else:
            Settings_Config["Game_Functionings"]["Player_Ship_Speed"] = 4
        if Game_Win_Bg_Box.get() == "Black":
                Settings_Config["Appearence"]["Game"]["Background_Colour"] = "#000000"
        else:
            Settings_Config["Appearence"]["Game"]["Background_Colour"] = "#000014"
        # Overwriting global Configurations variable
        Configurations = Settings_Config
        # Converting Python statements (Dict) to JSON statements (String)
        Configurations = json.dumps(Configurations)
        # Overwriting the JSON files and showing a messege box that the process was completed successfully
        Configuration_File = open("Space_Shooter_Configurations.json", "w")
        Configuration_File.write(Configurations)
        Alert.showinfo("Settings", "Your configurations are saved and will take effect the next time you start the game.")
        # Destroying Settings_Window, after saving the settings
        Settings_Window.destroy()
        
    # Function to overwrite default settings on previous settings
    def Set_Defaults():
        
        # Asking confirmation to save files
        Confirmation = Alert.askquestion("Restore Defaults?", "Restoring to defaults will delete the changes you made in the settings. \nExcept your settings, no other changes will be made. \nDo you wish to continue?", icon = "warning")
        # If confirmed, proceed, else, exit the fuction
        if Confirmation == "yes":
            pass
        else:
            return
        
        # Assinging new value to Configurations variable, the default configurations
        Configurations = {
            "Appearence": 
                {
                "Start": 
                    {
                    "Change_Object_Colours": True,
                    "Background_Colour": "#000014"
                },
                "Game": 
                    {
                    "Player_Ship_Image": "Images\\Player_Space_Ship(1).png",
                    "Enemy_Ship_Image": "Images\\Enemy_Space_Ship(1).png",
                    "Boss_Ship_Image": "Images\\Boss_Space_Ship(1).png",
                    "Star_Appearence": "Stars with Movement",
                    "Background_Colour": "#000014"
                }
            },
        "Game_Functionings":
            {
                "Player_Ship_Speed": 4
            }
        }
        # Converting Python Statements (Dict) to JSON Statemets (String) and overwriting the default settings
        Configurations = json.dumps(Configurations)
        Configuration_File = open("Space_Shooter_Configurations.json", "w")
        Configuration_File.write(Configurations)
        # Showing that process was completed successfully and destroying the Settings_Window
        Alert.showinfo("Settings", "The game settings are restored to default. \nMost changes will take place the next time you start the game.")
        Settings_Window.destroy()
    
    # Function to configure the widgets to have values as defined in the JSON file
    def Show_Configs():
        Configuration_File = open("Space_Shooter_Configurations.json", "r")
        Configurations = Configuration_File.read()
        Configurations = json.loads(Configurations)
        
        Player_1_Button.configure(command = lambda: Change_Settings("Player", Player_1_Button, 1), background = Show_Curen_Config("Button", "Player", "Images\\Player_Space_Ship(1).png"))
        Player_2_Button.configure(command = lambda: Change_Settings("Player", Player_2_Button, 2), background = Show_Curen_Config("Button", "Player", "Images\\Player_Space_Ship(2).png"))
        Player_3_Button.configure(command = lambda: Change_Settings("Player", Player_3_Button, 3), background = Show_Curen_Config("Button", "Player", "Images\\Player_Space_Ship(3).png"))
        Enemy_1_Button.configure(command = lambda: Change_Settings("Enemy", Enemy_1_Button, 1), background = Show_Curen_Config("Button", "Enemy", "Images\\Enemy_Space_Ship(1).png"))
        Enemy_2_Button.configure(command = lambda: Change_Settings("Enemy", Enemy_2_Button, 2), background = Show_Curen_Config("Button", "Enemy", "Images\\Enemy_Space_Ship(2).png"))
        Enemy_3_Button.configure(command = lambda: Change_Settings("Enemy", Enemy_3_Button, 3), background = Show_Curen_Config("Button", "Enemy", "Images\\Enemy_Space_Ship(3).png"))
        Boss_1_Button.configure(command = lambda: Change_Settings("Boss", Boss_1_Button, 1), background = Show_Curen_Config("Button", "Boss", "Images\\Boss_Space_Ship(1).png"))
        Boss_2_Button.configure(command = lambda: Change_Settings("Boss", Boss_2_Button, 2), background = Show_Curen_Config("Button", "Boss", "Images\\Boss_Space_Ship(2).png"))
        Start_Win_Bg_Box.current(Show_Curen_Config("Combobox", Configurations["Appearence"]["Start"]["Background_Colour"]))
        Star_Appearence_Box.current(Show_Curen_Config("Combobox", Configurations["Appearence"]["Game"]["Star_Appearence"]))
        Game_Win_Bg_Box.current(Show_Curen_Config("Combobox", Configurations["Appearence"]["Game"]["Background_Colour"]))
        Player_Speed_Box.current(Show_Curen_Config("Combobox", Configurations["Game_Functionings"]["Player_Ship_Speed"]))
        Change_Obj_Col_Box.current(Show_Curen_Config("Combobox", Configurations["Appearence"]["Start"]["Change_Object_Colours"]))
        
    Show_Configs()
    
    # Creating a Frame and a Button for saving files
    Save_Frame = Frame(Setting_Frame, highlightthickness = 9, highlightbackground = "Cyan", highlightcolor = "Cyan")
    Save_Frame.place(x = 180, y = 738)
    Save_Button = Button(Save_Frame, text = "Save", borderwidth = 0, font = ("Times New Roman", 18, "bold"), foreground = "Cyan", background = "#000014", command = Save_Configures, width = 6)
    Save_Button.pack()
    
    # Creating a Frame and a Button to restore defaults
    Res_Def_Frame = Frame(Setting_Frame, highlightthickness = 9, highlightbackground = "Cyan", highlightcolor = "Cyan")
    Res_Def_Frame.place(x = 360, y = 738)
    Res_Def_Button = Button(Res_Def_Frame, text = "Restore Defaults", borderwidth = 0, font = ("Times New Roman", 18, "bold"), foreground = "Cyan", background = "#000014", command = Set_Defaults, width = 12)
    Res_Def_Button.pack()
    
    # Binding combination keys for saving and restoring defaults
    Settings_Window.bind("<Control-s>", lambda event: Save_Configures())
    Settings_Window.bind("<Control-d>", lambda event: Set_Defaults())
    
    Settings_Window.mainloop()
    
# Setting the icon and Canvas for showing the objects and a button for settings
Window.iconphoto(False, Frame_Icon)
Can = Canvas(Window, width = 1000, height = 750, background = Configurations["Appearence"]["Start"]["Background_Colour"])
Can.pack()
Set_But = Button(Window, image = Settings_Icon, background = "Cyan", command = lambda: Open_Settings())
Set_But.place(x = 900, y = 30)

# Creating an empty list for objects and their speed, and a colour list and setting number of objects
Objects = []
Object_Colours = []
Object_Speed_X = []
Object_Speed_Y = []
Colour_List = ["White", "Red", "Aqua", "Blue", "Deep pink", "Green", "Yellow", "Purple", "Orangered"]
Number_OF_Objects = 540

# Setting text to show up on screen
Can.create_text(495, 27, font = ("Times New Roman", 45), text = "Space Shooter", fill = "White")
Can.create_text(495, 630, font = ("Times New Roman", 18), text = "Press 'Enter' to start the game!", fill = "White")
Can.create_text(495, 690, font = ("Times New Roman", 18), text = "Press 'F1' for Help!", fill = "White")

# Creating Information variables to show when the user presses 'Fx' key for help
Info_Information = [
    "Welcome to the Space Shooter Game!",
    "Press 'F2' for About.",
    "Press 'F3' for Game Controls",
    "Press 'F4' for Other Informations",
    "Press 'F5' for Update Notes"
]

About_Information = [
    "Project-Name:            Space_Shooter",
    "Developer:                   Ansh Malviya",
    "GitHub Username:     AnonymousTechDeveloper",
    "Mode:                          Single Player",
    "Version:                       2.0.0",
    "Language:                   Python & JScript(JSON)",
    "Special Thanks:          All my dear Friends.",
    "(c) 2021 - Ansh", 
    "All rights reserved."
]

Game_Controls_Information = [
    "Keyboard Controls before starting the Game:",
    "   'Enter':                            Start the Game.",
    "   'F1, F2, F3, F4':               Help.",
    "   'Ctrl-Shift-S':                 Open Settings Window.",
    "Keyboard Controls before Settings Window:",
    "   'Ctrl-s':                           Save Configurations.",
    "   'Ctrl-d':                          Restore Defaults.",
    "Keyboard Controls after the Game Starts:",
    "   'Right-Key/d':               Move the Player Ship right.",
    "   'Left-Key/a':                  Move the Player Ship left.",
    "   'Up/Down-Key/w/s:    Fire the Missile."
]

Play_Information = [
    "After starting the game, 5 enemies ships and a player ship will appear.",
    "The Enemies will continously burst fire on you.",
    "Save your ship from these missiles by moving your ship.",
    "Keep firing missiles to bring down the Enemy ships.",
    "Your Missiles would be limited to 5 and will recharge after every 3 seconds.",
    "The Red Squares at the bottom right of the window indicates the number of missiles available.",
    "Each Enemy is worth 10 points!",
    "Your highscore will be saved at a local destination. \n",
    "Boss Ships:",
    "   ->Appear after unfrequent intervals.",
    "   ->Hitpoints- x10 of hitpoints of general enemies (Look at the purple bar above it).",
    "   ->Firing types-",
    "       >Missiles: Fires 2 missiles at a time at the set of 3.",
    "       >Normal Missiles: Shoots a laser till the bottom is the screen, lasts 3 sec, refreshes after 9 sec.",
    "       >Target Miisiles: Spawns a Target Ring at the current position of Player Ship, after 3 sec, it shoots, refreshes after 3 sec.",
    "   ->Award: Adds 100 points as you gets it down.\n",
    "Objective: To kill as many enemies as possible before they gets below your screen or their missile/laser hits your ship.",
    "For any query, bug, problem etc. please do not hesitate to ask it on the GitHub, the same repository from where you downloaded this file.",
    "\n",
    "Best of Luck! \n",
    "IMPORTANT: Closing the game may takes a few moments and may freeze as you do it (Especially when the Boss exists when you close the game), give it the time of almost 9 sec and it will close."
]

Update_Note_Information = [
    "Welcome to the Major Update of Space_Shooter!",
    "Version: 2.0.0",
    "Added Features and Changes:",
    "   ->Added New Background Colour- Space Blue.",
    "   ->Added Animated Background- Moving Star Animation.",
    "   ->Added All new Boss Ships (Refer to Gameplay for more info- F4).",
    "   ->Added Settings Window: For Personalisation.",
    "   ->Introducing New Player & Enemy Skins.",
    "   ->Enabled WSAD controls.",
    "\n",
    "More Updates with new features coming soon, Stay Tuned!"
]

# Starting the game when the user hits enter
def Start_Game(event):
    
    global Game_Running
    global Game_Quit
    
    Window.unbind("<Return>")
    Window.destroy()
    Game_Running = True
    Game_Quit = False

# Function to change background and image when user hovers mouse over the settings button
def Change_Appearence(Colour, Image):
    
    Set_But.configure(background = Colour, image = Image)

# Key bindings and hover bindings for the Window and Setting Button
Window.bind("<Return>", Start_Game)
Window.bind("<Control-Shift-S>", lambda event: Open_Settings())
Set_But.bind("<Enter>", lambda event: Change_Appearence("Purple", Settings_Icon_Inverted))
Set_But.bind("<Leave>", lambda event: Change_Appearence("Cyan", Settings_Icon))

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
    Object_Colours.append(Colour)
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
        
        if Configurations["Appearence"]["Start"]["Change_Object_Colours"]:
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
Window.bind("<F5>", lambda event: Show_Info("Update Notes", Update_Note_Information))

# Putting the start screen in a mainloop
Window.mainloop()

# If the user clicks the exit button, terminate the program before creating the pygame screen
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

# Creating the pygame Window
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
Boss_Ship_Image = pygame.transform.scale(Boss_Ship_Image, (270, 90))

# Setting a variable to control frame rate
Frame_Rate = pygame.time.Clock()

# Setting Initial Position of Player Ship
Player_x = 485
Player_y = 690

# Creating lists for storing boss, its components, star, thei speed and size, enemies, its speed and missiles for both Player and Enemies and Number of missiles available as an int
Enemies = []
Enemy_Speed = []
Player_Missiles = []
Enemy_Missiles = []
Boss_Ships = []
Boss_Ship_Speed = []
Boss_Hitpoints = []
Lasers = []
Direct_Lasers = []
Laser_Direction = []
Target_Rings = []
Stars = []
Stars_Speed = []
Stars_Size = []
Number_of_Stars = 36
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

# Mover enemies vertically (Downwards)
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

# Function to fire player missiles
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
    if y1 <= 0 or Collision_Occurs_Enemy_Missiles(Missile) or Player_Missile_Boss_Collision(Missile):
        
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
            
    # Returning False, don't if collision occurs
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
    
    Missile = pygame.draw.rect(Window, "BLUE", pygame.Rect(x + 10, y + 10, 10, 10))
    Window.blit(Enemy_Missile_Image, Missile)
    
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
                Alert.showerror("Error", "An error occured while saving the highscore in the file \nMake sure that the file 'Space_Shooter_Highscore.txt' is not changed, try deleting the file and try again! \nError: " + str(Error))

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

# Function to create a boss ship
def Create_Boss_Ship():
    
    Boss_Ship = pygame.draw.rect(Window, "RED", pygame.Rect(5, 63, 270, 90))
    
    # Adding boss, its hitpoints and speed in the lists
    Boss_Ships.append(Boss_Ship)
    Boss_Hitpoints.append(10)
    Boss_Ship_Speed.append(numpy.random.choice([-3, 3]))
    
    # Calling it's firing it it exists
    if Game_Running and Boss_Ships:
        Boss_Laser_Timer = Timer(5, Start_Boss_Laser)
        Boss_Laser_Timer.start()
    
    if Game_Running and Boss_Ships:
        Show_Target_Timer = Timer(5, Show_Laser_Target)
        Show_Target_Timer.start()
    
    if Game_Running and Boss_Ships:
        Shoot_Laser_Timer = Timer(8, Shoot_Boss_Laser)
        Shoot_Laser_Timer.start()
    
    if Game_Running and Boss_Ships:
        Fire_Boss_Timer = Timer(3, Fire_Boss_Missiles)
        Fire_Boss_Timer.start()

# Move the boss ship
def Move_Boss_Ship(Boss_Ship):
    
    x1 = Boss_Ship.left
    x2 = Boss_Ship.right
    
    # Changing the boss' direction it it reaches the edge of the screen
    if x1 <= 0 or x2 > 999:
        Boss_Ship_Speed[Boss_Ships.index(Boss_Ship)] = -Boss_Ship_Speed[Boss_Ships.index(Boss_Ship)]
    
    # Creating a Boss ship with new position
    New_Boss_Ship = pygame.draw.rect(Window, "RED", pygame.Rect(x1 + Boss_Ship_Speed[Boss_Ships.index(Boss_Ship)], 63, 270, 90))
    Window.blit(Boss_Ship_Image, New_Boss_Ship)
    
    # Calling a function to show Boss' hitpoints
    Show_Boss_Hitpoints(Boss_Ship)
    
    # Overwriting the older boss with new boss with new position
    Boss_Ships[Boss_Ships.index(Boss_Ship)] = New_Boss_Ship

# Function to fire boss missiles at a set of 3
def Fire_Boss_Missiles():
    
    for Boss_Ship in Boss_Ships:
        
        Continous_Firing_Timer = Timer(0.5, Continous_Firing)
        Continous_Firing_Timer.start()
        
        Continous_Firing_Timer = Timer(1.0, Continous_Firing)
        Continous_Firing_Timer.start()
        
        Continous_Firing_Timer = Timer(1.5, Continous_Firing)
        Continous_Firing_Timer.start()
        
        if Game_Running and Boss_Ships:
            Fire_Boss_Timer = Timer(3, Fire_Boss_Missiles)
            Fire_Boss_Timer.start()

# Function to fire boss missiles
def Continous_Firing():
    
    Bx1, By1, Bx2, By2 = Boss_Ship.left, Boss_Ship.top, Boss_Ship.right, Boss_Ship.bottom
    
    Boss_Missile = pygame.draw.rect(Window, "BLUE", pygame.Rect(Bx1 + 30, By2 - 6, 10, 10))
    Window.blit(Enemy_Missile_Image, Boss_Missile)
    
    Enemy_Missiles.append(Boss_Missile)
    
    Boss_Missile = pygame.draw.rect(Window, "BLUE", pygame.Rect(Bx2 - 40, By2 - 6, 10, 10))
    Window.blit(Enemy_Missile_Image, Boss_Missile)
    
    Enemy_Missiles.append(Boss_Missile)

# Function to show boss' hitpoints as a rectangular bar over it
def Show_Boss_Hitpoints(Boss_Ship):
    
    x1 = Boss_Ship.left
    
    for i in range(0, Boss_Hitpoints[Boss_Ships.index(Boss_Ship)]):
        pygame.draw.rect(Window, "PURPLE", pygame.Rect(x1 + 85, 45, 10 + i*10, 3))

# Checking if Player's missile collides the boss
def Player_Missile_Boss_Collision(Missile):
    global Score
    
    Mx1, My1, Mx2, My2 = Missile.left, Missile.top, Missile.right, Missile.bottom
    
    for Boss in Boss_Ships:
        
        Ex1, Ey1, Ex2, Ey2 = Boss.left, Boss.top, Boss.right, Boss.bottom
        
        # Checking collision
        if Mx1 > Ex1 and Mx1 < Ex2 or Mx2 > Ex1 and Mx2 < Ex2:
            if My1 > Ey1 and My1 < Ey2 or My2 > Ey1 and My2 < Ey2:
                # ? If Collision happens...
                
                # Subtracting 1 hitpoints
                Boss_Hitpoints[Boss_Ships.index(Boss)] -= 1
                
                # If hitpoints reaches 0...
                if Boss_Hitpoints[Boss_Ships.index(Boss)] == 0:
                    
                    # ...Removing Boss, its hitpoints (0) and its speed from list
                    Boss_Ship_Speed.pop(Boss_Ships.index(Boss))
                    Boss_Hitpoints.pop(Boss_Ships.index(Boss))
                    Boss_Ships.pop(Boss_Ships.index(Boss))
                    
                    # Adding 100 to the score
                    Score += 100
                    
                    # Removing every element from the 'Target_Rings' list
                    for Target_Ring in Target_Rings:
                        Target_Rings.pop(Target_Rings.index(Target_Ring))
                    
                    # If any of the timer for boss to shoot missile/laser is active, cancel it
                    try:
                        Boss_Laser_Timer.cancel()
                    
                    except: pass
                    
                    try:
                        Show_Target_Timer.cancel()
                    
                    except: pass
                    
                    try:
                        Shoot_Laser_Timer.cancel()
                    
                    except: pass
                    
                    # Starting a new timer for the boss to appear
                    Boss_Coming = Timer(30, Create_Boss_Ship)
                    Boss_Coming.start()
                
                # Returing True
                return True
            
    # Returning False, if doesn't collision occurs
    return False

# Function to shoot boss laser till the bottom edge of the screen
def Start_Boss_Laser():
    
    for Boss_Ship in Boss_Ships:
        
        Bx1, By1, Bx2, By2 = Boss_Ship.left, Boss_Ship.top, Boss_Ship.right, Boss_Ship.bottom
        
        Laser = pygame.draw.line(Window, "CYAN", (Bx1 + 135, By2 - 15), (Bx1 + 135, 750))
        Lasers.append(Laser)
        
        # If the boss exists, start the timers to shoot laser again
        if Game_Running == True:
            Remove_Laser_Timer = Timer(3, Remove_Boss_Laser)
            Remove_Laser_Timer.start()
            
        if Game_Running and Boss_Ships:
            Boss_Laser_Timer = Timer(9, Start_Boss_Laser)
            Boss_Laser_Timer.start()

# Move the lasers according to the boss' position
def Move_Lasers(Laser):
    
    global Game_Running
    
    for Boss_Ship in Boss_Ships:
        
        Bx1, By1, Bx2, By2 = Boss_Ship.left, Boss_Ship.top, Boss_Ship.right, Boss_Ship.bottom
        
        Pre_Laser = Laser
        Laser = pygame.draw.line(Window, "CYAN", (Bx1 + 135, By2 - 15), (Bx1 + 135, 750))
        
        Lasers[Lasers.index(Pre_Laser)] = Laser
        
        Lx1, Ly1, Lx2, Ly2 = Laser.left, Laser.top, Laser.right, Laser.bottom
        Px1, Py1, Px2, Py2 = Player_Ship.left, Player_Ship.top, Player_Ship.right, Player_Ship.bottom
        
        if Lx1 >= Px1 and Lx1 <= Px2 or Lx2 >= Px1 and Lx2 <= Px2:
            # If true, quit the game
            
            Game_Running = False
            
            if Highscore < Score:
                
                try:
                    Highscore_File = open("Space_Shooter_Highscore.txt", "w")
                    Highscore_File.write(str(Score))
                
                except Exception as Error:
                    Alert.showerror("Error", "An error occured while saving the highscore in the file \nMake sure that the file 'Space_Shooter_Highscore.txt' is not changed, try deleting the file and try again! \nError: " + str(Error))

# Remove boss' laser
def Remove_Boss_Laser():
    
    for Laser in Lasers:
        
        Lasers.pop(Lasers.index(Laser))

# Function to show the target where the boss is going to fire
def Show_Laser_Target():
    
    Px, Py = Player_Ship.center
    
    Target_Ring = pygame.draw.circle(Window, "RED", (Px, Py), 25, width = 3)
    
    Target_Rings.append(Target_Ring)
    
    # If the boss exists, start the timers again
    if Game_Running and Boss_Ships:
        Show_Target_Timer = Timer(9, Show_Laser_Target)
        Show_Target_Timer.start()
    
    if Game_Running and Boss_Ships:
        Shoot_Laser_Timer = Timer(12, Shoot_Boss_Laser)
        Shoot_Laser_Timer.start()

# Shoot boss laser to the target ring
def Shoot_Boss_Laser():
    
    for Boss_Ship in Boss_Ships:
    
        Bx1, By1, Bx2, By2 = Boss_Ship.left, Boss_Ship.top, Boss_Ship.right, Boss_Ship.bottom
        
        for Target_Ring in Target_Rings:
            
            TRx, TRy = Target_Ring.center
            
            Direct_Laser = pygame.draw.line(Window, "CYAN", (Bx1 + 135, By2 - 15), (TRx, TRy))
            Direct_Lasers.append(Direct_Laser)
            
            if TRx < Bx1 + 135:
                Laser_Direction.append("Left")
            
            else:
                Laser_Direction.append("Right")
            
            # Check collision after 0.3 seconds
            Check_Collision_Timer = Timer(0.3, lambda: Check_Laser_Shoot(Target_Ring))
            Check_Collision_Timer.start()
            
# Checking if boss' target laser hits player
def Check_Laser_Shoot(Target_Ring):
    global Game_Running
    global Target_Rings
    
    TRx, TRy = Target_Ring.center
    Px1, Py2, Px2, Py2 = Player_Ship.left, Player_Ship.top, Player_Ship.right, Player_Ship.bottom
    
    if TRx >= Px1 and TRx <= Px2:
        # If true, quit the game
        Game_Running = False
        
        # If score is higher than highscore...
        if Highscore < Score:
            
            # Save the highscore in the external file
            try:
                Highscore_File = open("Space_Shooter_Highscore.txt", "w")
                Highscore_File.write(str(Score))
            
            # If an error occurs while saving the highscore, show the error
            except Exception as Error:
                Alert.showerror("Error", "An error occured while saving the highscore in the file \nMake sure that the file 'Space_Shooter_Highscore.txt' is not changed, try deleting the file and try again! \nError: " + str(Error))
                
    # Emptying the target rings and direct laser's lists
    Target_Rings = []
    
    for Direct_Laser in Direct_Lasers:
        Laser_Direction.pop(Direct_Lasers.index(Direct_Laser))
        Direct_Lasers.pop(Direct_Lasers.index(Direct_Laser))

# If 'No Stars' not defined as the value of 'Star_Appearence' in the JSON file, create Stars at random positions
if Configurations["Appearence"]["Game"]["Star_Appearence"] != "No Stars":

    for i in range(0, Number_of_Stars):
        
        x = numpy.random.randint(1, 990)
        y = numpy.random.randint(1, 747)
        Size = numpy.random.randint(0, 2)
        
        Star = pygame.draw.circle(Window, "WHITE",  (x, y), Size)
        
        Stars.append(Star)
        Stars_Size.append(Size)
        Stars_Speed.append(numpy.random.randint(1, 4))

# Function to move stars (takes place only if value of 'Star_Appearence' is 'Stars with Movement')
def Move_Stars(Star):
    
    x, y = Star.center
    Previous_Star = Stars.index(Star)

    New_Star = pygame.draw.circle(Window, "WHITE", (x, y + Stars_Speed[Stars.index(Star)]), Stars_Size[Stars.index(Star)])
    Stars[Stars.index(Star)] = New_Star
    
    x, y = Star.center
    
    # If a star reaches the bottom of the screen, pop it, its speed and size from the respective lists and create new star
    if y > 747:
        Stars_Size.pop(Previous_Star)
        Stars_Speed.pop(Previous_Star)
        Stars.pop(Previous_Star)
        Create_New_Star()

# Function to create new star
def Create_New_Star():
    
    x = numpy.random.randint(3, 990)
    y = 3
    Size = numpy.random.randint(0, 2)
    
    Star = pygame.draw.circle(Window, "WHITE", (x, y), Size)
    
    Stars.append(Star)
    Stars_Size.append(Size)
    Stars_Speed.append(numpy.random.randint(1, 4))

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

# Starting timer for boss to appear
Boss_Coming = Timer(30, Create_Boss_Ship)
Boss_Coming.start()

# Running main game loop
while Game_Running == True:
    
    # Setting game frame rate
    Frame_Rate.tick(90)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exiting game
            Game_Running = False
            Game_Quit = True
            Add_Missile.cancel()
            Boss_Coming.cancel()
            Gravity.cancel()
            Enemy_Fire.cancel()
            try:
                Fire_Boss_Timer.cancel()
                Show_Target_Timer.cancel()
                Boss_Laser_Timer.cancel()
            except:
                pass
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player_x -= 15
            if event.key == pygame.K_RIGHT:    
                Player_x += 15
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                if Missiles_Available:
                    Fire_Missile_Player()
                
    # Filling background colour as specied in the JSON file on the game window
    Window.fill(Configurations["Appearence"]["Game"]["Background_Colour"])
    
    # Moving the Player ship, horizontally
    Event = pygame.key.get_pressed()
    Player_x += Event[pygame.K_RIGHT]*Configurations["Game_Functionings"]["Player_Ship_Speed"] - Event[pygame.K_LEFT]*Configurations["Game_Functionings"]["Player_Ship_Speed"]
    Player_x += Event[pygame.K_d]*Configurations["Game_Functionings"]["Player_Ship_Speed"] - Event[pygame.K_a]*Configurations["Game_Functionings"]["Player_Ship_Speed"]
    # ? In above lines, Event[pygame.K_X] returns 0 if false and 1 if true (if the event occurs), multiplying this value with the player speed in the JSON file
    
    # Preventing Player ship to move out of game window
    if Player_x < 0:
        Player_x = 0
    if Player_x > 970:
        Player_x = 970
    
    # Moving each missile fired by player
    for Missile in Player_Missiles:
        Move_Missiles_Player(Missile)
    
    # If value of 'Star_Appearence' is 'Stars with Movement', call the function to move them
    if Configurations["Appearence"]["Game"]["Star_Appearence"] == "Stars with Movement":
        for Star in Stars:
            Move_Stars(Star)

    # Else, recreate each star (if the exists), at the same position
    else:
        for Star in Stars:
            
            x, y = Star.center
            pygame.draw.circle(Window, "WHITE", (x, y), Stars_Size[Stars.index(Star)])
    
    # Move Each Boss Ship
    for Boss_Ship in Boss_Ships:
        Move_Boss_Ship(Boss_Ship)
    
    # Moving Each missile fired by enemy
    for Missile in Enemy_Missiles:
        Move_Enemy_Missile(Missile)
    
    # Moving Each Laser with respect to the position of the boss
    for Laser in Lasers:
        Move_Lasers(Laser)
    
    # If any direct laser (target laser) exists, show then on screen
    for Direct_Laser in Direct_Lasers:
        Dx1, Dy1, Dx2, Dy2 = Direct_Laser.left, Direct_Laser.top, Direct_Laser.right, Direct_Laser.bottom
        
        if Laser_Direction[Direct_Lasers.index(Direct_Laser)] == "Right":
            pygame.draw.line(Window, "CYAN", (Dx1, Dy1), (Dx2, Dy2))
        
        else:
            pygame.draw.line(Window, "CYAN", (Dx2, Dy1), (Dx1, Dy2))
    
    # Moving each Enemy
    for Enemy in Enemies:
        Move_Enemies(Enemy)
        
        # Stopping the game if an enemy reaches the bottom edge of the screen
        if Enemy.bottom >= 747:
            Game_Running = False
        
    # Checking there are less than 3 enemies left, if so, recreate 3 more enemies
    if len(Enemies) < 3:
        Create_Enemies(3)
        # This prevents terminating the gtame without player's mistake by getting 0 enemies
    
    # Displaying number of missiles available
    Display_Number_Of_Missiles(Missiles_Available)
    
    # Creating and moving the Player ship and putting image on it
    Player_Ship = pygame.draw.rect(Window, "BLUE", pygame.Rect(Player_x, Player_y, 30, 30))
    Window.blit(Player_Ship_Image, Player_Ship)
    
    # If boss ship exists, show each target ring (if any) on the screen
    if Boss_Ships:
        for Target_Ring in Target_Rings:
            Tx, Ty = Target_Ring.center
            pygame.draw.circle(Window, 'RED', (Tx, Ty), 25, width = 3)
    
    # Putting Score panel on surface of the window
    Score_Text = Score_Font.render("Score: " + str(Score), True, "White")
    Window.blit(Score_Text, Score_Rectangle)
    
    # Putting Highscore panel on surface of the window
    Highscore_Text = Highscore_Font.render("Highscore: " + str(Highscore), True, "White")
    Window.blit(Highscore_Text, Highscore_Rectangle)
    
    # Updating game window
    pygame.display.flip()

# Cancel all the timers when the game ends
Add_Missile.cancel()
Boss_Coming.cancel()
Gravity.cancel()
Enemy_Fire.cancel()
try:
    Fire_Boss_Timer.cancel()
except: pass
try:
    Show_Target_Timer.cancel()
except: pass
try:
    Boss_Laser_Timer.cancel()
except: pass
try:
    Shoot_Laser_Timer.cancel()
except: pass
try:
    for i in range(3):
        Continous_Firing_Timer.cancel()
except: pass
try:
    Remove_Laer_Timer.cancel()
except: pass
try:
    Show_Laser_Timer.cancel()
except: pass

Window.fill(Configurations["Appearence"]["Game"]["Background_Colour"])

# Running another loop to show that the game ended
while Game_Quit == False:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Quit = True
            sys.exit()
    
    Window.blit(Text, Text_Rectangle)

    # Creating panel to show that the game is over
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
    
    # Updating the game screen
    pygame.display.flip()
    
    # Filling the background colour as specified in the JSON file
    Window.fill(Configurations["Appearence"]["Game"]["Background_Colour"])