#Cooper Martin

import pygame
import time
import random

pygame.init()

mult = 20 #size of game. lower is smaller, also speeds up game when smaller
height = 31
width = 28
x = int(width*mult)
y = int(height*mult)
#screen = pygame.display.set_mode([x,y+mult])
#font = pygame.font.Font(pygame.font.get_default_font(), mult)
counter = 0 #counts every frame the game moves
mode = 0 #0 for normal, 1 when pacman can eat ghosts
modeCt = 0 #counter when mode == 1, goes to 1000
speed = 1 #make this higher to control game speed
steps = int(0.05*mult) #number of pixels pacman/ghosts move every iteration (value must go into mult or problems may occur)
running = True
reset = False #true when game resets on win/lose
score = 0 #number of eaten pellets on one life
highScore = 0 #highest score achieved during session
wins = 0 #number of times all pellets have been eaten on one life
moveSync = 0 #only lets pacman & ghosts change direction every mult steps, prevents desync
learnRate = 0.001
randomness = 1 #1 for fully random, 0 for fully smart. decrements based on learnRate
dotX = random.randint(0,width-1) #these are coordinates for a pellet for pacman to seek
dotY = random.randint(0,height-1)
reflex_agent = False #true to have ai play, false to play the game as a human
neural_network = False #true to have nn play, false to play the game as a human or agent

#below is the initial board state. each number corresponds to a particular entity
#0: empty
#1: wall
#2: pellet
#3: super pellet
#4: unused
#5: pacman
#6: inky
#7: blinky
#8: pinky
#9: clyde
#================================
def SETUP_PACMAN_NEURAL(Setting):
    
    global neural_network
    if Setting == True:
        neural_network = True
    else:
        neural_network = False
#================================
#================================
def SETUP_PACMAN_AI(Setting):

    global reflex_agent
    if Setting == True:
        reflex_agent = True
    else:
        reflex_agent = False
#================================                                 
board = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,6,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,7,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
         [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
         [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
         [0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0],
         [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,3,2,2,1,1,2,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,1,1,2,2,3,1],
         [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
         [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
         [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
         [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
         [1,8,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,9,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#below is a list of all junctions found in board. ghosts can only change direction on these junctions
nodes = [1*width+1,1*width+6,1*width+12,1*width+15,1*width+21,1*width+26,
    5*width+1,5*width+6,5*width+9,5*width+12,5*width+15,5*width+18,5*width+21,5*width+26,
    8*width+1,8*width+6,8*width+9,8*width+12,8*width+15,8*width+18,8*width+21,8*width+26,
    11*width+9,11*width+12,11*width+15,11*width+18,
    14*width+6,14*width+9,14*width+18,14*width+21,
    17*width+9,17*width+18,
    20*width+1,20*width+6,20*width+9,20*width+12,20*width+15,20*width+18,20*width+21,20*width+26,
    23*width+1,23*width+3,23*width+6,23*width+9,23*width+12,23*width+15,23*width+18,23*width+21,23*width+24,23*width+26,
    26*width+1,26*width+3,26*width+6,26*width+9,26*width+12,26*width+15,26*width+18,26*width+21,26*width+24,26*width+26,
    29*width+1,29*width+12,29*width+15,29*width+26]

class Pacman:
    def __init__(self,ch):
        self.type = ch #types correspond to same values found in board
        if self.type == 5:
            self.pacX = 13*mult + int(mult/2) #starting drawn position
            self.pacY = 23*mult + int(mult/2)
            self.color = (255,255,0)
            self.old = 0 #holds value based on what pacman/ghost is on top of if anything
            self.point = [23,13] #starting board position
        elif self.type == 6:
            self.pacX = 1*mult + int(mult/2)
            self.pacY = 1*mult + int(mult/2)
            self.color = (0,255,255)
            self.old = 2
            self.point = [1,1]
        elif self.type == 7:
            self.pacX = 26*mult + int(mult/2)
            self.pacY = 1*mult + int(mult/2)
            self.color = (255,0,0)
            self.old = 2
            self.point = [1,26]
        elif self.type == 8:
            self.pacX = 1*mult + int(mult/2)
            self.pacY = 29*mult + int(mult/2)
            self.color = (255,184,255)
            self.old = 2
            self.point = [29,1]
        elif self.type == 9:
            self.pacX = 26*mult + int(mult/2)
            self.pacY = 29*mult + int(mult/2)
            self.color = (255,184,82)
            self.old = 2
            self.point = [29,26]
        self.dirX = 0 #starting direction is neutral
        self.dirY = 0
        self.bufX = 0 #starting input buffer is neutral
        self.bufY = 0

    def move(self,ch):
        #return a move based on ch
        #0: up
        #1: left
        #2: down
        #3: right
        if ch == 0:
            self.bufX = 0
            self.bufY = -1*steps
        elif ch == 1:
            self.bufX = -1*steps
            self.bufY = 0
        elif ch == 2:
            self.bufX = 0
            self.bufY = 1*steps
        elif ch == 3:
            self.bufX = 1*steps
            self.bufY = 0

    def calcMove(self,px,py):
        #calculate move for ghost based on pacman location
        x = self.pacX - px #distance from pacman on both axes
        y = self.pacY - py
        p = random.randint(0,20) #current setup is 50% calculated move, 50% random move
        if p < 5: #move in x direction
            if x > 0:
                ch = 1
            else:
                ch = 3
        elif p < 10: #move in y direction
            if y > 0:
                ch = 0
            else:
                ch = 2
        else: #make completely random move
            ch = random.randint(0,3)
        if mode == 1: #run opposite direction if pacman can eat ghosts
            ch = ch + 2
            if ch > 3:
                ch = ch - 4
        self.move(ch)

    def updatePos(self,screen):
        #updates the position of pacman/ghost on board both visually and internally
        global mode
        global modeCt
        global height
        global width
        global reset
        global score
        global wins
        global highScore
        global dotX
        global dotY
        global moveSync
        global randomness
        global learnRate
        global steps
        found = False
        for i in range(0,x,mult):
            for j in range(0,y,mult):
                p = board[int(j/mult)][int(i/mult)]
                if p == self.type and not found: #perform operations when pacman/ghost has been found in board
                    if (int(i/mult+int(self.bufX/steps)) < width and int(i/mult+int(self.bufX/steps)) > 0 and
                        board[int(j/mult+int(self.bufY/steps))][int(i/mult+int(self.bufX/steps))] != 1 and
                        self.pacX % mult == int(mult/2) and
                        self.pacY % mult == int(mult/2) and moveSync == 0): #only change direction when new location is inbounds and not a wall. also must be fully on a block for synchronization
                        if self.type == 5 or int(j/mult)*width+int(i/mult) in nodes: #pacman can change directions on any block, ghosts only can at junctions
                            self.dirX = self.bufX #update current direction with current input buffer
                            self.dirY = self.bufY
                    if board[int(j/mult+int(self.dirY/steps))][int(i/mult+int(self.dirX/steps))] != 1: #if next pixel is not a wall, perform update operations
                        self.pacX = self.pacX + self.dirX #update drawn position
                        self.pacY = self.pacY + self.dirY
                        if (self.pacX % mult == int(mult/2) and
                            self.pacY % mult == int(mult/2)): #perform additional operation if pacman/ghost is fully on block
                            if self.type == 5: #pacman eats whatever was on block before or dies to ghost. always left empty afterwards
                                board[int(j/mult)][int(i/mult)] = 0
                            else: #if ghosts previously covered pellet or another ghost, restore that pellet/ghost
                                board[int(j/mult)][int(i/mult)] = self.old
                            self.old = board[int(j/mult+int(self.dirY/steps))][int(i/mult+int(self.dirX/steps))] #save next block item for later
                            if self.old == 5 and mode == 1: #if pacman is able to eat ghosts, make sure he eats the ghost and not the other way around and move to next block
                                board[int(j/mult+int(self.dirY/steps))][int(i/mult+int(self.dirX/steps))] = 5
                                self.old = 0
                            else: #move pacman/ghost to next block
                                board[int(j/mult+int(self.dirY/steps))][int(i/mult+int(self.dirX/steps))] = self.type
                            self.point[0] = self.point[0] + int(self.dirY/steps) #update board position
                            self.point[1] = self.point[1] + int(self.dirX/steps)
                            if self.point[1] >= width-1: #these only pass when pacman/ghost teleport from one side of the board to the other
                                self.point[1] = self.point[1] - (width-2)
                            elif self.point[1] <= 0:
                                self.point[1] = self.point[1] + (width-2)
                            if int(i/mult+int(self.dirX/steps)) == width-1: #perform right to left teleport
                                if self.type == 5:
                                    board[int(j/mult+int(self.dirY/steps))][int(i/mult+int(self.dirX/steps))] = 0
                                else:
                                    board[int(j/mult+int(self.dirY/steps))][int(i/mult+int(self.dirX/steps))] = self.old
                                self.old = board[int(j/mult+int(self.dirY/steps))][1]
                                board[int(j/mult+int(self.dirY/steps))][1] = self.type
                                self.pacX = self.pacX - (width-2)*mult
                            elif int(i/mult+int(self.dirX/steps)) == 0: #perform left to right teleport
                                if self.type == 5:
                                    board[int(j/mult+int(self.dirY/steps))][int(i/mult+int(self.dirX/steps))] = 0
                                else:
                                    board[int(j/mult+int(self.dirY/steps))][int(i/mult+int(self.dirX/steps))] = self.old
                                self.old = board[int(j/mult+int(self.dirY/steps))][width-2]
                                board[int(j/mult+int(self.dirY/steps))][width-2] = self.type
                                self.pacX = self.pacX + (width-2)*mult
                    pygame.draw.circle(screen,self.color,(self.pacX,self.pacY),0.4*mult) #draws pacman/ghost in precise location
                    if (((self.old > 4 and self.type == 5) or
                        (self.old == 5 and self.type > 4))
                        and mode == 0): #if pacman and ghost run into each other while pacman is not invincible, game over
                        reset = True
                        if score > highScore: #save new highscore
                            highScore = score
                        score = 0
                        wins = 0
                        return
                    if not any(2 in x for x in board): #if all pellets are eaten, pacman wins and plays again with accumulating score & wins
                        if reset == False: #ensures update only increments once in case this block is reached more than once during reset
                            wins = wins + 1
                        reset = True
                        return
                    if self.type == 5 and self.old == 3: #if pacman eats a super pellet, he becomes invincible and can eat ghosts
                        self.old = 0
                        mode = 1
                        modeCt = 0
                        self.color = (255,255,255)
                    found = True #operations complete, do not seek anymore

def findDot(p5x,p5y):
    #finds a pellet for pacman to chase when not directly near one
    global dotX
    global dotY
    itX = random.randint(0,1) #randomly increment or decrement when searching
    if itX == 0:
        itX = -1
    itY = random.randint(0,1)
    if itY == 0:
        itY = -1
    xy = random.randint(0,1)
    if xy == 0: #search row first when xy == 0, else search column first
        for i in range(len(board[0])):
            if board[p5y][(i+p5x)%width] == 2: #pellet is found, return pellet location
                dotX = (i+p5x)%width
                dotY = p5y
                return
        for i in range(len(board)):
            if board[(i+p5y)%height][p5x] == 2:
                dotX = p5x
                dotY = (i+p5y)%height
                return
    else:
        for i in range(len(board)):
            if board[(i+p5y)%height][p5x] == 2:
                dotX = p5x
                dotY = (i+p5y)%height
                return
        for i in range(len(board[0])):
            if board[p5y][(i+p5x)%width] == 2:
                dotX = (i+p5x)%width
                dotY = p5y
                return
    jt = random.randint(0,len(board)-1) #no pellet in same row/column as pacman, search board randomly for pellet
    it = random.randint(0,len(board[jt])-1)
    cnt = 0 #used to break loop
    while True: #loops until every index in board has been checked
        if board[jt%height][it%width] == 2: #if pellet found, return pellet location
            dotX = it%width
            dotY = it%height
            return
        it = it + 1
        jt = jt + 1
        if cnt == width*height: #only passes if no pellets are left
            dotY = random.randint(0,len(board)-1)
            dotX = random.randint(0,len(board[dotY]-1))
            return

def updateBoard(screen):
    #updates the board visually for everything that isn't pacman or ghosts
    screen.fill((0,0,0))
    for i in range(0,x,mult):
        for j in range(0,y,mult):
            p = board[int(j/mult)][int(i/mult)]
            if p == 0: #empty block
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
            elif p == 1: #wall
                pygame.draw.rect(screen,(33,33,222),(i,j,mult-1,mult-1))
            elif p == 2: #pellet
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
                pygame.draw.circle(screen,(255,255,255),
                                   (i+int(mult/2),j+int(mult/2)),0.1*mult)
            elif p == 3: #super pellet
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
                pygame.draw.circle(screen,(255,255,0),
                                   (i+int(mult/2),j+int(mult/2)),0.2*mult)
            elif p == 4: #unused
                pygame.draw.rect(screen,(255,255,255),(i,j,mult-1,mult-1))

def resetBoard():
    #resets the board when game over or win happens
    global board
    board = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,6,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,7,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,3,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,3,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
         [1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
         [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
         [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
         [0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0],
         [1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
         [1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
         [1,3,2,2,1,1,2,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,1,1,2,2,3,1],
         [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
         [1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
         [1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
         [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
         [1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
         [1,8,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,9,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

def countScore():
    #counts all pellets and super pellets left in the board and returns score based on how many are missing
    global board
    s = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2 or board[i][j] == 3:
                s = s + 1
    return 241 - s

def pacmanAgent(pac,g1,g2,g3,g4):
    #reflex agent, controls what the ai does rather than having a human player
    global randomness
    global learnRate
    choice = random.random()
    if choice < randomness: #make random decisions based on how smart the ai is
        randomness = randomness - learnRate #every random decision reduces randomness by learnRate
        return random.randint(0,3)
    px = pac.point[0] #take all passed in objects (pacman & all ghosts) and put useful variables into new easy to access variables/arrays
    py = pac.point[1]
    gp = [g1.point[0],g1.point[1],g2.point[0],g2.point[1],g3.point[0],g3.point[1],g4.point[0],g4.point[1]]
    for i in range(0,len(gp),2): #if a ghost is already eaten, set its point far out of bounds to prevent unusual behavior
        if not any(6+i-int(i/2) in x for x in board):
            gp[i] = 100000
            gp[i+1] = 100000
    ch = [] #array to hold possible choices ai can make and not hit a wall
    if py == 0 or py == width-1: #only passes when pacman teleports, return to avoid possible out of bounds exception
        return random.randint(0,3)
    if board[px+1][py] != 1:
        ch.append([px+1,py,2])
    if board[px-1][py] != 1:
        ch.append([px-1,py,0])
    if board[px][py+1] != 1:
        ch.append([px,py+1,3])
    if board[px][py-1] != 1:
        ch.append([px,py-1,1])
    random.shuffle(ch) #shuffle choices to prevent pacman from trending to a single direction
    max2 = [-1,-1] #holds the direction that maximizes the distance between pacman and the closest ghost
    for i in range(len(ch)):
        min1 = 9999
        for j in range(4):
            temp = abs(ch[i][0]-gp[2*j])+abs(ch[i][1]-gp[2*j+1]) #distance between pacman and ghost
            if temp < min1: #find closest ghost
                min1 = temp
        if min1 > max2[0]: #find best choice
            max2[0] = min1
            max2[1] = i
    if max2[0] <= 5 and (mode == 0 or modeCt > 900): #return found choice if pacman is at risk of getting eaten, else carry on
        return ch[max2[1]][2]
    ch2 = [] #array to hold possible choices ai can make and collect a pellet
    if board[px+1][py] != 1 and board[px+1][py] < 4 and (board[px+1][py] == 3 or board[px+1][py] == 2):
        ch2.append([px+1,py,2])
    if board[px-1][py] != 1 and board[px-1][py] < 4 and (board[px-1][py] == 3 or board[px-1][py] == 2):
        ch2.append([px-1,py,0])
    if board[px][py+1] != 1 and board[px][py+1] < 4 and (board[px][py+1] == 3 or board[px][py+1] == 2):
        ch2.append([px,py+1,3])
    if board[px][py-1] != 1 and board[px][py-1] < 4 and (board[px][py-1] == 3 or board[px][py-1] == 2):
        ch2.append([px,py-1,1])
    if len(ch2) == 0: #if pacman is not adjacent to a pellet, seek out distant pellet on the board
        pxy = px*width+py
        if pxy in nodes: #only change direction when at a junction to prevent excessive zigzagging
            if abs(px-dotY)+abs(py-dotX) > width+height or (board[dotY][dotX] != 2 and board[dotY][dotX] != 3): #if current pellet location does not hold a pellet anymore, find new pellet location
                findDot(py,px)
            eps = random.random()
            if eps < 0.9: #10% chance pacman makes a random move to prevent getting stuck if possible
                xory = random.randint(0,1)
                if xory == 0: #if xory == 0 move in x direction first, then y direction. else, do the opposite
                    if py-dotX < 0:
                        if board[px][py+1] != 1: #only add choice if it doesn't make pacman run into a wall
                            ch2.append([px,py+1,3])
                    elif py-dotX > 0:
                        if board[px][py-1] != 1:
                            ch2.append([px,py-1,1])
                    if px-dotY < 0:
                        if board[px+1][py] != 1:
                            ch2.append([px+1,py,2])
                    elif px-dotY > 0:
                        if board[px-1][py] != 1:
                            ch2.append([px-1,py,0])
                else:
                    if px-dotY < 0:
                        if board[px+1][py] != 1:
                            ch2.append([px+1,py,2])
                    elif px-dotY > 0:
                        if board[px-1][py] != 1:
                            ch2.append([px-1,py,0])
                    if py-dotX < 0:
                        if board[px][py+1] != 1:
                            ch2.append([px,py+1,3])
                    elif py-dotX > 0:
                        if board[px][py-1] != 1:
                            ch2.append([px,py-1,1])
                if len(ch2) >= 1: #return the first choice found. randomness of xory prevents trending to either direction
                    return ch2[0][2]
                return random.randint(0,3) #if no choice that minimizes distance was found, return random choice
            return random.randint(0,3) #10% random choice
        if pac.bufX == 1*steps or pac.bufY == 1*steps: #pacman isn't at a junction, return the direction that keeps pacman moving forward
            if pac.bufX == 1*steps:
                return 3
            else:
                return 2
        else:
            if pac.bufX == -1*steps:
                return 1
            else:
                return 0
    ch = random.randint(0,len(ch2)-1) #pacman is adjacent to at least one pellet. randomly select pellet to move to if more than one
    return ch2[ch][2]
def PacMan_Main():

    pygame.init()
    
    global x
    global y
    global mult
    global moveSync
    screen = pygame.display.set_mode([x,y+mult])

    updateBoard(screen) #initialize board

    pacman = Pacman(5) #initialize pacman/ghosts
    inky = Pacman(6)
    blinky = Pacman(7)
    pinky = Pacman(8)
    clyde = Pacman(9)

    global running
    while running: #main loop

        for event in pygame.event.get(): #read WASD keys or arrow keys for input
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and reflex_agent == False: #don't read keys when ai is active
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    pacman.move(0)
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    pacman.move(1)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pacman.move(2)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    pacman.move(3)
                elif event.key == pygame.K_ESCAPE: #escape key exits the game
                    running = False
            elif event.type == pygame.KEYDOWN and reflex_agent == True:
                if event.key == pygame.K_ESCAPE:
                    running = False

        global counter                  
        counter = counter + 1
        if counter % speed == 0: #speed is used to slow down the game for ease of playing
            if counter % int(1000/steps) == 0: #occasionally update the seeked pellet location randomly to prevent getting stuck if possible
                findDot(-1,-1)
            if reflex_agent == True and moveSync == 0: #calculate ai move
                res = pacmanAgent(pacman,inky,blinky,pinky,clyde)
                pacman.move(res)
            updateBoard(screen)
            pacman.updatePos(screen)
            inky.calcMove(pacman.pacX,pacman.pacY)
            inky.updatePos(screen)
            blinky.calcMove(pacman.pacX,pacman.pacY)
            blinky.updatePos(screen)
            pinky.calcMove(pacman.pacX,pacman.pacY)
            pinky.updatePos(screen)
            clyde.calcMove(pacman.pacX,pacman.pacY)
            clyde.updatePos(screen)
            global mode
            global modeCt
            moveSync = moveSync + steps
            if moveSync >= mult: #moveSync remains in sync based on mult
                moveSync = 0
            if mode == 1: #case when pacman is invincible
                if modeCt == 0: #mode is just activated, recolor ghosts
                    inky.color = (25,25,166)
                    blinky.color = (25,25,166)
                    pinky.color = (25,25,166)
                    clyde.color = (25,25,166)
                modeCt = modeCt + steps
                if modeCt > 1000: #mode lasts for 1000 iterations, then reverts back to normal mode
                    mode = 0
                    modeCt = 0
                    pacman.color = (255,255,0)
                    inky.color = (0,255,255)
                    blinky.color = (255,0,0)
                    pinky.color = (255,184,255)
                    clyde.color = (255,184,82)
            global score
            global wins
            global highScore                    
            old = score
            score = (wins * 241) + countScore()
            if score < old: #used to ensure score doesn't decrease when ghosts hover over pellets
                score = old
            outScore = "Score: " + str(score) + "     Highscore: " + str(highScore)
            font = pygame.font.SysFont('aerial', mult)                                  
            text = font.render(outScore,True,(255,255,255))
            textRect = text.get_rect()
            textRect.center = (x/2,y+(mult/2))
            screen.blit(text,textRect)
        
            global reset            
            if reset == True: #reset all game assets
                score = 0
                mode = 0
                reset = False
                pacman = Pacman(5)
                inky = Pacman(6)
                blinky = Pacman(7)
                pinky = Pacman(8)
                clyde = Pacman(9)
                resetBoard()
                updateBoard(screen)
        if counter > 999999999: #prevent counter from going too high
            counter = 0
        pygame.display.flip()

    pygame.quit()
