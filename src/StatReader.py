
import turtle
import sys

from SNAKE import Snake_Main
from SNAKE import SETUP_SNAKE_AI
from SNAKE import SETUP_SNAKE_NEURAL
from BreakoutGamev03 import Breakout_Main
from BreakoutGamev03 import SETUP_BREAKOUT_AI
from BreakoutGamev03 import SETUP_BREAKOUT_NEURAL
from PacMan import PacMan_Main
from PacMan import SETUP_PACMAN_AI
from PacMan import SETUP_PACMAN_NEURAL

ENABLE_DARK_MODE = True

WINDOW = turtle.Screen()

#=============================
if ENABLE_DARK_MODE == False:
    WINDOW.bgcolor("white")
elif ENABLE_DARK_MODE == True:
    WINDOW.bgcolor("black")
#=============================

class Button:

    def __init__(self, RGB, text, location):
    
        self.textData = text
        
        self.Body = turtle.Turtle()
        self.Body.penup()
        self.Body.goto(location)
        self.Body.color(RGB)
        self.Body.shape("square")
        
        self.Text = turtle.Turtle()
        self.Text.penup()
        self.Text.goto(self.Body.xcor() + 20, self.Body.ycor() - 8)
        #=============================
        if ENABLE_DARK_MODE == True:
            self.Text.color("white")
        elif ENABLE_DARK_MODE == False:
            self.Text.color("black")
        #=============================
        self.Text.hideturtle()
        self.Text.write(self.textData, align="left", font=("Verdana", 10, "bold"))
        
        
class Cursor:

    def __init__(self, location, movement, maxup, maxdown):
    
        self.MoveSpeed = movement
        self.Selection = False
        
        self.MaxUp = maxup
        self.MaxDown = maxdown
    
        self.Body = turtle.Turtle()
        self.Body.penup()
        self.Body.goto(location)
        self.Body.color("grey")
        self.Body.shape("triangle")
        self.Body.shapesize(.5, .5, None)
        
    def GoUp(self):
        if not self.Body.ycor() == self.MaxUp:
            self.Body.goto(self.Body.xcor(), self.Body.ycor() + self.MoveSpeed)
        
    def GoDown(self):
        if not self.Body.ycor() == self.MaxDown:
            self.Body.goto(self.Body.xcor(), self.Body.ycor() - self.MoveSpeed)
        
    def MakeSelection(self):
        self.Selection = True
        
    def SelectionMade(self):
        return self.Selection
        
    def UndoSelection(self):
        self.Selection = False
    
XPos = -300
YPos = 250
Dist = 50

ButtonColor = "white"
TitleColor = "black"
instButtonColor = "grey"
#=============================
if ENABLE_DARK_MODE == False:
    ButtonColor = "black"
    TitleColor = "white"
elif ENABLE_DARK_MODE == True:
    ButtonColor = "white"
    TitleColor = "black"
#=============================

Title_Button = Button(TitleColor, "          AI Learns to Play Retro Video Games\nAustin Brown, Nathanael L. Mann, Cooper Martin", (XPos + 100,YPos))
  
Game_Cursor = Cursor((-325,YPos-Dist), Dist, YPos-Dist, YPos-Dist*4)  
Breakout_Button = Button("blue", "Start Breakout", (XPos,YPos - Dist))
Snake_Button = Button("green", "Start Snake", (XPos,YPos - Dist * 2))
PacMan_Button = Button("gold", "Start PacMan", (XPos,YPos - Dist * 3))
QuitButton = Button("red", "Quit Program", (XPos,YPos - Dist * 4))

AI_Cursor = Cursor((-325, YPos-Dist*5), Dist, (YPos-Dist*5), (YPos-Dist*7))
AI_Button = Button(ButtonColor, "Start As Agent", (XPos,YPos - Dist * 5))
NN_Button = Button(ButtonColor, "Start As Neural Network", (XPos,YPos - Dist * 6))
User_Button = Button(ButtonColor, "Start As User", (XPos,YPos - Dist * 7))

Instructions_Button_Games = Button(instButtonColor, "Use Up And Down Arrows To Choose Game", (XPos,YPos - Dist * 8))
Instructions_Button_AIToggle = Button(instButtonColor, "Press 1 and 0 To Go Up And Down AI Menu", (XPos,YPos - Dist * 9))
Instructions_Button_Selection = Button(instButtonColor, "Press Enter To Execute Game", (XPos,YPos - Dist * 10))

def MAIN(): 
    
    turtle.listen()
    turtle.onkey(Game_Cursor.GoUp, "Up")
    turtle.onkey(Game_Cursor.GoDown, "Down")
    turtle.onkey(AI_Cursor.GoUp, 1)
    turtle.onkey(AI_Cursor.GoDown, 0)
    turtle.onkey(Game_Cursor.MakeSelection, 'Return')

    while True:
    
        if (Game_Cursor.Body.ycor() == Snake_Button.Body.ycor() and Game_Cursor.SelectionMade() == True):
            if (AI_Cursor.Body.ycor() == AI_Button.Body.ycor()):
                SETUP_SNAKE_AI(True)
            elif (AI_Cursor.Body.ycor() == NN_Button.Body.ycor()):
                SETUP_SNAKE_NEURAL(True)
            Snake_Main()
            
            
        if (Game_Cursor.Body.ycor() == Breakout_Button.Body.ycor() and Game_Cursor.SelectionMade() == True):
            if (AI_Cursor.Body.ycor() == AI_Button.Body.ycor()):
                SETUP_BREAKOUT_AI(True)
            elif (AI_Cursor.Body.ycor() == NN_Button.Body.ycor()):
                SETUP_BREAKOUT_NEURAL(True)
            else:
                SETUP_BREAKOUT_AI(False)
                SETUP_BREAKOUT_NEURAL(False)
            Breakout_Main()
            
            
        if (Game_Cursor.Body.ycor() == PacMan_Button.Body.ycor() and Game_Cursor.SelectionMade() == True):
            if (AI_Cursor.Body.ycor() == AI_Button.Body.ycor()):
                SETUP_PACMAN_AI(True)
            elif (AI_Cursor.Body.ycor() == NN_Button.Body.ycor()):
                SETUP_PACMAN_NEURAL(True)
            PacMan_Main()
            
        if (Game_Cursor.Body.ycor() == QuitButton.Body.ycor() and Game_Cursor.SelectionMade() == True):
            sys.exit(1)

        Game_Cursor.UndoSelection()
        WINDOW.update()
        
    
MAIN()
