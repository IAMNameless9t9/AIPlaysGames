

#Imports Functions From All 3 Games
from SNAKE import SETUP_SNAKE_AI
from SNAKE import Snake_Main
from BreakoutGamev02 import SETUP_BREAKOUT_AI
from BreakoutGamev02 import Breakout_Main
#from Pac-Man import *

#Ask User Which Game To Play
answer = int(input("Which Game Do You Want To Play?\nBreakout = 1\nPac-Man = 2\nSnake = 3\n"))
answerAI = int(input("Would You Like It To Has AI(0) Or No AI(1)?\n"))
print("\n")

if answer == 1: #Play Breakout
    print("Breakout Loading...")
    if answerAI == 0:
        print("Loading AI...")
        SETUP_BREAKOUT_AI(True)
    Breakout_Main()
    
    
if answer == 2: #Play Pac-Man
    print("Pac-Man Loading...")
    if answerAI == 0:
        print("Loading AI...")
    #Call PacMan's Main
    
    
if answer == 3: #Play Snake
    print("Snake Loading...")
    if answerAI == 0:
        print("Loading AI...")
        SETUP_SNAKE_AI(True)
    Snake_Main()

