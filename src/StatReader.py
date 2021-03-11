
import turtle
import sys

from SNAKE import Snake_Main
from SNAKE import SETUP_SNAKE_AI
from BreakoutGamev02 import Breakout_Main
from BreakoutGamev02 import SETUP_BREAKOUT_AI
from PacMan import PacMan_Main
from PacMan import SETUP_PACMAN_AI

ENABLE_DARK_MODE = True

WINDOW = turtle.Screen()

#=============================
if ENABLE_DARK_MODE == False:
    WINDOW.bgcolor("white")
else:
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
        if ENABLE_DARK_MODE == False:
            self.Text.color("black")
        else:
            self.Text.color("white")
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
#=============================
if ENABLE_DARK_MODE == False:
    ButtonColor = "black"
else:
    ButtonColor = "white"
#=============================
    
Snake_Button = Button("green", "Start Snake", (XPos,YPos))
Breakout_Button = Button("blue", "Start Breakout", (XPos,YPos - Dist))
PacMan_Button = Button("gold", "Start PacMan", (XPos,YPos - Dist * 2))
QuitButton = Button("red", "Quit Program", (XPos,YPos - Dist * 3))

AI_Button = Button(ButtonColor, "Start As AI", (XPos,YPos - Dist * 5))
User_Button = Button(ButtonColor, "Start As User", (XPos,YPos - Dist * 6))

Instructions_Button_Games = Button(ButtonColor, "Use Up And Down Arrows To Choose Game", (XPos,YPos - Dist * 8))
Instructions_Button_AIToggle = Button(ButtonColor, "Press 1 For AI, Press 0 For User", (XPos,YPos - Dist * 9))
Instructions_Button_Selection = Button(ButtonColor, "Press Enter To Execute Game", (XPos,YPos - Dist * 10))

Game_Cursor = Cursor((-325,250), Dist, YPos, YPos-Dist*3)
AI_Cursor = Cursor((-325, YPos-Dist*5), Dist, (YPos-Dist*5), (YPos-Dist*6))

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
            Snake_Main()
            
            
        if (Game_Cursor.Body.ycor() == Breakout_Button.Body.ycor() and Game_Cursor.SelectionMade() == True):
            if (AI_Cursor.Body.ycor() == AI_Button.Body.ycor()):
                SETUP_BREAKOUT_AI(True)
            Breakout_Main()
            
            
        if (Game_Cursor.Body.ycor() == PacMan_Button.Body.ycor() and Game_Cursor.SelectionMade() == True):
            if (AI_Cursor.Body.ycor() == AI_Button.Body.ycor()):
                SETUP_PACMAN_AI(True)
            PacMan_Main()
            
        if (Game_Cursor.Body.ycor() == QuitButton.Body.ycor() and Game_Cursor.SelectionMade() == True):
            sys.exit(1)

        Game_Cursor.UndoSelection()
        WINDOW.update()
        
    
MAIN()