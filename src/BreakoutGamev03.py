import sys
import pygame
import time
import random
import math
import numpy as np
from datetime import datetime

SCREEN_HEIGHT = 560
SCREEN_WIDTH = 820
GAME_RUNNING = True
GAME_OVER = False
SCORE = 0
HIGHSCORE = 0
DEATHS = 0

SIMPLE_REFLEX_AGENT = False
NEURAL_NETWORK_ACTIVE = False

#================================
def SETUP_BREAKOUT_NEURAL(Setting):
    
    global NEURAL_NETWORK_ACTIVE
    global SIMPLE_REFLEX_AGENT
    if Setting:
        NEURAL_NETWORK_ACTIVE = True
        SIMPLE_REFLEX_AGENT = True
    else:
        NEURAL_NETWORK_ACTIVE = False
#================================

def SETUP_BREAKOUT_AI(Setting):

    global SIMPLE_REFLEX_AGENT
    if Setting:
        SIMPLE_REFLEX_AGENT = True
        NEURAL_NETWORK_ACTIVE = False
    else:
        SIMPLE_REFLEX_AGENT = False

def sigmoid(x):
    s = 1.0/(1+np.exp(-x))
    return s

def sigmoid_derivative(x):
    s = sigmoid(x)
    ds = s*(1.0-s)
    return ds

class PADDLE(object):

    def __init__(self, rgb):
        self.width = 100
        self.position = (((SCREEN_WIDTH / 2) - (self.width / 2)), (7 * (SCREEN_HEIGHT / 8)))
        self.color = (rgb, rgb, rgb)
        self.baseSpeed = 5
        self.curSpeed = 0
        self.body = pygame.Rect(self.position, (self.width, 10))
        self.rightDown = False
        self.leftDown = False

        x, y = self.position
        self.bottomRight = (x + self.width, y + 10)
        self.hitbox = (self.position, self.bottomRight)
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.body)
        
    def move(self, border, ball):
        (x, y) , (dx, dy) = self.hitbox
        (bx, by), (bdx, bdy) = ball.hitbox

        if SIMPLE_REFLEX_AGENT == True:
            if x > border.xMin and (x + 50) > bx:
                self.curSpeed = -self.baseSpeed
                self.body.move_ip(self.curSpeed, 0)
                self.hitbox = ((x + self.curSpeed, y),(dx + self.curSpeed, dy))
            elif dx < border.xMax and (dx - 50) < bdx:
                self.curSpeed = self.baseSpeed
                self.body.move_ip(self.curSpeed, 0)
                self.hitbox = ((x + self.curSpeed, y),(dx + self.curSpeed, dy))
        else:
            if x > border.xMin and self.leftDown:
                self.body.move_ip(self.curSpeed, 0)
                self.hitbox = ((x + self.curSpeed, y),(dx + self.curSpeed, dy))
            elif dx < border.xMax and self.rightDown:
                self.body.move_ip(self.curSpeed, 0)
                self.hitbox = ((x + self.curSpeed, y),(dx + self.curSpeed, dy))

    def smartMove(self, border, decision):
        (x, y) , (dx, dy) = self.hitbox
        
        if x > border.xMin and decision[0][0] > 1.5 * decision[0][1]:
            self.curSpeed = -self.baseSpeed
            self.body.move_ip(self.curSpeed, 0)
            self.hitbox = ((x + self.curSpeed, y),(dx + self.curSpeed, dy))
        elif dx < border.xMax and 1.5 * decision[0][0] < decision[0][1]:
            self.curSpeed = self.baseSpeed
            self.body.move_ip(self.curSpeed, 0)
            self.hitbox = ((x + self.curSpeed, y),(dx + self.curSpeed, dy))

    def handleKeys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                ##sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.curSpeed = -self.baseSpeed
                    self.leftDown = True
                    self.rightDown = False
                elif event.key == pygame.K_RIGHT:
                    self.curSpeed = self.baseSpeed
                    self.rightDown = True
                    self.leftDown = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and not self.rightDown:
                    self.curSpeed = 0
                    self.leftDown = False
                elif event.key == pygame.K_RIGHT and not self.leftDown:
                    self.curSpeed = 0
                    self.rightDown = False

class BORDER(object):

    def __init__(self):
        self.thickness = 20
        
        self.xMin = self.thickness 
        self.xMax = SCREEN_WIDTH - self.thickness
        self.yMin = self.thickness
        self.yMax = SCREEN_HEIGHT - self.thickness
        self.color = (50,50,50)
    
        self.leftBody = pygame.Rect((0, 0), (self.thickness, SCREEN_HEIGHT))
        self.rightBody = pygame.Rect((self.xMax, 0), (self.thickness, SCREEN_HEIGHT))
        self.topBody = pygame.Rect((0, 0), (SCREEN_WIDTH, self.thickness))
        
        self.bodies = (self.leftBody, self.rightBody, self.topBody)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.leftBody)
        pygame.draw.rect(surface, self.color, self.rightBody)
        pygame.draw.rect(surface, self.color, self.topBody)

class BRICK(object):

    def __init__(self, startX, startY):
        r = 255
        g = 255
        b = 255
        if startY <= 60:
            r = 205
            g = 0
            b = 0
        elif startY <= 80:
            r = 255
            g = 102
            b = 0
        elif startY <= 100:
            r = 255
            g = 153
            b = 0
        elif startY <= 120:
            r = 255
            g = 204
            b = 0
        elif startY <= 140:
            r = 153
            g = 204
            b = 0
        elif startY <= 160:
            r = 0
            g = 128
            b = 0
        elif startY <= 180:
            r = 0
            g = 128
            b = 128
        elif startY <= 200:
            r = 0
            g = 102
            b = 204
        elif startY <= 220:
            r = 128
            g = 0
            b = 128
        elif startY <= 240:
            r = 100
            g = 0
            b = 200

        self.color1 = (r, g, b)
        self.color2 = (r/2, g/2, b/2)
        self.position = (startX, startY)
        self.body1 = pygame.Rect(self.position, (60, 20))
        self.body2 = pygame.Rect((startX+3, startY+3), (53, 13))
        
        self.bottomright = (startX + 60, startY + 20)
        self.hitbox = (self.position, self.bottomright)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color1, self.body1)
        pygame.draw.rect(surface, self.color2, self.body2)


class BALL(object):

    def __init__(self):
        self.color1 = (0, 255, 0)
        self.color2 = (200, 200, 200)
        randomStartPos = random.randint(50, SCREEN_WIDTH-50)
        self.position = (((randomStartPos)-8),(7 * (SCREEN_HEIGHT / 8)-17))
        self.body1 = pygame.Rect(self.position, (16, 16))
        x, y = self.position
        self.body2 = pygame.Rect((x+4, y+4),(8, 8))

        self.bottomright = (x + 16, y + 16)
        self.hitbox = (self.position, self.bottomright)

        choices = [-1, 1]
        choice = random.randint(0, 1)
        self.yVel = -1
        self.xVel = choices[choice]

    def draw(self, surface):
        self.color1 = (min(255, SCORE/50), max(0, 255-(SCORE/50)), 0)
        pygame.draw.rect(surface, self.color1, self.body1)
        pygame.draw.rect(surface, self.color2, self.body2)

    def move(self, border, paddle, bricks):
        (x,y),(dx,dy) = self.hitbox
        (px, py),(pdx, pdy) = paddle.hitbox

        global SCORE

        if  x <= border.xMin:
            self.xVel = -1 * self.xVel
        elif dx >= border.xMax:
            self.xVel = -1 * self.xVel
        elif y <= border.yMin:
            self.yVel = -1 * self.yVel
        elif dy+20 >= border.yMax:
            global GAME_OVER
            GAME_OVER = True
        elif dy == py and dx > (px + 25) and x < (pdx - 25):
            self.yVel = -1 * self.yVel
        elif dy == py and dx >= px and x <= (px + 25):
            self.yVel = -1 * self.yVel
            self.xVel = -1 * abs(self.xVel)
        elif dy == py and dx >= (pdx - 25) and x <= pdx:
            self.yVel = -1 * self.yVel
            self.xVel = abs(self.xVel)

        index = 0
        for brick in bricks:
            (bx, by), (bdx, bdy) = brick.hitbox
            if x == bdx and y < bdy and dy > by:
                self.xVel = -1 * self.xVel
                del bricks[index]
                SCORE += 100
                break
            elif y == bdy and x < bdx and dx > bx:
                self.yVel = -1 * self.yVel
                del bricks[index]
                SCORE += 100
                break
            elif dx == bx and y < bdy and dy > by:
                self.xVel = -1 * self.xVel
                del bricks[index]
                SCORE += 100
                break
            elif dy == by and x < bdx and dx > bx:
                self.yVel = -1 * self.yVel
                del bricks[index]
                SCORE += 100
                break
            index += 1
                
        self.body1.move_ip(self.xVel, self.yVel)
        self.body2.move_ip(self.xVel, self.yVel)
        self.hitbox = ((x + self.xVel, y + self.yVel),(dx + self.xVel, dy + self.yVel))

class NeuralNetwork:

    def __init__(self):
        self.IHWeights = np.random.rand(8,8)
        self.HOWeights = np.random.rand(8,2)
        self.output = np.zeros(2)

    def feedForward(self, x):
        self.hiddenLayer = sigmoid(np.dot(x,self.IHWeights))
        self.output = sigmoid(np.dot(self.hiddenLayer, self.HOWeights))

    def backPropagate(self, y):
        d_HOWeights = np.dot(self.hiddenLayer.T, (2*(y - self.output) * sigmoid_derivative(self.output))) + 0.01
        d_IHWeights = np.dot(self.hiddenLayer.T, (np.dot(2*(y - self.output) * sigmoid_derivative(self.output), self.HOWeights.T) * sigmoid_derivative(self.hiddenLayer))) + 0.01

        self.HOWeights += d_HOWeights
        self.IHWeights += d_IHWeights

#=========================================================================#
#
# BREAKOUT v0.3
# By: Nathanael L. Mann
#
#=========================================================================#
def Breakout_Main():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    ghost = PADDLE(50)
    paddle = PADDLE(200)
    border = BORDER()
    ball = BALL()
    neuralNetwork = NeuralNetwork()
    bricksX = int ((SCREEN_WIDTH - (border.thickness * 2)) / 60)
    bricksY = int (((SCREEN_WIDTH - (border.thickness * 2)) / 60) - 3)
    bricksGap = 40
    NumberofBricks = bricksX * bricksY
    bricks = [BRICK(border.thickness, border.thickness + bricksGap)] * NumberofBricks
    ballSpeed = 1

    i = border.thickness
    k = 0
    while i < 60 * bricksX:
        j = bricksGap + border.thickness
        while j < (20 * bricksY) + bricksGap + border.thickness:
            bricks[k] = BRICK(i, j)
            k += 1
            j += 20
        i += 60

    myfont = pygame.font.SysFont("broadway", 24)

    global GAME_RUNNING
    global GAME_OVER
    global SCORE
    global HIGHSCORE
    global DEATHS
    while GAME_RUNNING:

        if len(bricks) == 0:
            GAME_RUNNING = False
        
        screen.fill((0, 0, 0))

        global SETUP_BREAKOUT_AI
        global SETUP_BREAKOUT_NEURAL
        if NEURAL_NETWORK_ACTIVE == True:
            ghost.draw(screen)
        paddle.draw(screen)
        border.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)

        paddle.handleKeys()
        
        if NEURAL_NETWORK_ACTIVE:
            (bx, by), (bdx, bdy) = ball.hitbox
            bxv = ball.xVel
            byv = ball.yVel
            (px, py), (pdx, pdy) = paddle.hitbox
                        
            inputs = np.array([[bx/10, bdx/10, by/10, bdy/10, bxv, byv, px/10, pdx/10]])
            neuralNetwork.feedForward(inputs)
            decision = np.array(neuralNetwork.output)
            paddle.smartMove(border, decision)

            #UPDATE NEURAL NETWORK EVERY STEP
            if px > bx:
                correctAnswer = np.array([[1.0, 0.0]])
            elif pdx < bdx:
                correctAnswer = np.array([[0.0, 1.0]])
            else:
                correctAnswer = np.array([[0.0, 0.0]])
            neuralNetwork.backPropagate(correctAnswer)
        else:
            paddle.move(border, ball)

        ghost.move(border, ball)

        step = 0
        while step < ballSpeed:
            ball.move(border, paddle, bricks)
            step += 1

        ballSpeed = min(5, (int(SCORE / 2500) + 1))

        if SCORE > HIGHSCORE:
            HIGHSCORE = SCORE
            now = datetime.now()
            currentTime = now.strftime("%H:%M:%S")
            print(currentTime, "| New High Score:", HIGHSCORE, "in", DEATHS, "deaths.")

        text = myfont.render("Score: {0}".format(SCORE), 1, (255, 255, 255))
        screen.blit(text, (30, SCREEN_HEIGHT-30))
        text = myfont.render("High Score: {0}".format(HIGHSCORE), 1, (255, 255, 255))
        screen.blit(text, (300, SCREEN_HEIGHT-30))
        text = myfont.render("Deaths: {0}".format(DEATHS), 1, (255, 255, 255))
        screen.blit(text, (620, SCREEN_HEIGHT-30))
        #probL = neuralNetwork.output[0][0]
        #probR = neuralNetwork.output[0][1]
        #confidence = abs(probL - probR)
        #text = myfont.render("Confidence: {0}".format(confidence), 1, (255, 255, 255))
        #screen.blit(text, (30, 30))
        
        
        pygame.display.update()

        clock.tick(120)

        if(GAME_OVER):

            #UPDATE NEURAL NETWORK ONLY ON DEATH
            #if px > bx:
                #correctAnswer = np.array([[1.0, 0.0]])
            #elif pdx < bdx:
                #correctAnswer = np.array([[0.0, 1.0]])
            #else:
                #correctAnswer = np.array([[0.0, 0.0]])
            #neuralNetwork.backPropagate(correctAnswer)
            
            time.sleep(0.25)
            ghost = PADDLE(50)
            paddle = PADDLE(200)
            ball = BALL()
            bricks = [BRICK(border.thickness, border.thickness + bricksGap)] * NumberofBricks
            ballSpeed = 1
            GAME_OVER = False
            SCORE = 0
            DEATHS += 1
            
            i = border.thickness
            k = 0
            while i < 60 * bricksX:
                j = bricksGap + border.thickness
                while j < (20 * bricksY) + bricksGap + border.thickness:
                    bricks[k] = BRICK(i, j)
                    k += 1
                    j += 20
                i += 60

    myfont = pygame.font.SysFont("broadway", 32)
    if len(bricks) == 0:
        text = myfont.render("YOU WIN", 1, (0, 255, 0))
        screen.blit(text, ((SCREEN_WIDTH/2)-84, (SCREEN_HEIGHT/2)-16))
    else:
        text = myfont.render("GAME OVER", 1, (255, 0, 0))
        screen.blit(text, ((SCREEN_WIDTH/2)-108, (SCREEN_HEIGHT/2)-16))
    pygame.display.update()

    #time.sleep(5)
    #pygame.quit()
    #sys.exit()

##Breakout_Main()
