
from SNAKE import *

#AGENT BRAIN

def GainGameInfo(snake, food):

    #Get Snake Head
    SnakeHead_X, SnakeHead_Y = snake.getHeadPosition()
    
    #Get Food Position
    Food_X, Food_Y = food.position
        
    if SnakeHead_X > Food_X: #Go Left
        snake.SNAKE_LEFT()
    elif SnakeHead_X < Food_X: #Go Right
        snake.SNAKE_RIGHT()
    elif SnakeHead_Y < Food_Y: #Go Down
        snake.SNAKE_DOWN()
    elif SnakeHead_Y > Food_Y: #Go Up
        snake.SNAKE_UP()
    

    