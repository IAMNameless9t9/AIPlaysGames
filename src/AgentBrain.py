
from SNAKE import *
from BreakoutGamev02 import *

#AGENT BRAIN

def GainGameInfoFrom_Snake(snake, food):

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
        
def GainGameInfoFrom_Breakout(paddle, ball):

    (x, y) , (dx, dy) = paddle.hitbox
    (bx, by), (bdx, bdy) = ball.hitbox

    if x > border.xMin and (x + 50) > bx:
        self.curSpeed = -self.baseSpeed
        self.body.move_ip(self.curSpeed, 0)
        self.hitbox = ((x + self.curSpeed, y),(dx + self.curSpeed, dy))
        
    elif dx < border.xMax and (dx - 50) < bdx:
        self.curSpeed = self.baseSpeed
        self.body.move_ip(self.curSpeed, 0)
        self.hitbox = ((x + self.curSpeed, y),(dx + self.curSpeed, dy))

def GainGameInfoFrom_PacMan(snake, food):
    pass
    
def PrintSomething():
    print("Hello")