import pygame
import time
import random

mult = 20
height = 31
width = 28
x = int(width*mult)
y = int(height*mult)
#screen = pygame.display.set_mode([x,y])
#screen = None
counter = 0
mode = 0
modeCt = 0
hidden = False
speed = 1 #make this higher to control game speed
running = True
reset = False
score = 0
highScore = 0
wins = 0     
reflex_agent = False

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
        self.type = ch
        if self.type == 5:
            self.pacX = 13*mult + int(mult/2)
            self.pacY = 23*mult + int(mult/2)
            self.color = (255,255,0)
            self.old = 0
            self.point = [23,13]
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
        self.dirX = 0
        self.dirY = 0
        self.bufX = 0
        self.bufY = 0
        self.alive = True
        self.timer = 0

    def move(self,ch):
        if ch == 0:
            self.bufX = 0
            self.bufY = -1
        elif ch == 1:
            self.bufX = -1
            self.bufY = 0
        elif ch == 2:
            self.bufX = 0
            self.bufY = 1
        elif ch == 3:
            self.bufX = 1
            self.bufY = 0

    def calcMove(self,px,py):
        x = self.pacX - px
        y = self.pacY - py
        p = random.randint(0,20)
        if p < 5:
            if x > 0:
                ch = 1
            else:
                ch = 3
        elif p < 10:
            if y > 0:
                ch = 0
            else:
                ch = 2
        else:
            ch = random.randint(0,3)
        if mode == 1:
            ch = ch + 2
            if ch > 3:
                ch = ch - 4
        self.move(ch)

    def updatePos(self, screen):
        global mode
        global modeCt
        global height
        global width
        global reset
        global score
        global wins
        global highScore  
        found = False
        for i in range(0,x,mult):
            for j in range(0,y,mult):
                p = board[int(j/mult)][int(i/mult)]
                if p == self.type and not found:
                    if (int(i/mult+self.bufX) < 28 and int(i/mult+self.bufX) > 0 and
                        board[int(j/mult+self.bufY)][int(i/mult+self.bufX)] != 1 and
                        self.pacX % mult == int(mult/2) and
                        self.pacY % mult == int(mult/2)):
                        if self.type == 5 or int(j/mult)*width+int(i/mult) in nodes:
                            self.dirX = self.bufX
                            self.dirY = self.bufY
                    if board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] != 1:
                        self.pacX = self.pacX + self.dirX
                        self.pacY = self.pacY + self.dirY
                        if (self.pacX % mult == int(mult/2) and
                            self.pacY % mult == int(mult/2)):
                            if self.type == 5:
                                board[int(j/mult)][int(i/mult)] = 0
                            else:
                                board[int(j/mult)][int(i/mult)] = self.old
                            self.old = board[int(j/mult+self.dirY)][int(i/mult+self.dirX)]
                            if self.old == 5 and mode == 1:
                                board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = 5
                                self.old = 0
                                self.alive = False
                            else:
                                board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = self.type
                            self.point[0] = self.point[0] + self.dirY
                            self.point[1] = self.point[1] + self.dirX
                            if self.point[1] >= 27:
                                self.point[1] = self.point[1] - 26
                            elif self.point[1] <= 0:
                                self.point[1] = self.point[1] + 26
                            if int(i/mult+self.dirX) == 27:
                                if self.type == 5:
                                    board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = 0
                                else:
                                    board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = self.old
                                self.old = board[int(j/mult+self.dirY)][1]
                                board[int(j/mult+self.dirY)][1] = self.type
                                self.pacX = self.pacX - 26*mult
                            elif int(i/mult+self.dirX) == 0:
                                if self.type == 5:
                                    board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = 0
                                else:
                                    board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = self.old
                                self.old = board[int(j/mult+self.dirY)][26]
                                board[int(j/mult+self.dirY)][26] = self.type
                                self.pacX = self.pacX + 26*mult
                    pygame.draw.circle(screen,self.color,(self.pacX,self.pacY),8)
                    if (((self.old > 4 and self.type == 5) or
                        (self.old == 5 and self.type > 4))
                        and mode == 0):
                        reset = True
                        if score > highScore:
                            highScore = score
                        score = 0
                        wins = 0                      
                        return                        
                    if not any(2 in x for x in board):
                        if reset == False:
                            wins = wins + 1
                        reset = True
                        return
                    if self.type == 5 and self.old == 3:
                        self.old = 0
                        mode = 1
                        modeCt = 0
                        self.color = (255,255,255)
                    found = True

def updateBoard(screen):
    screen.fill((0,0,0))
    for i in range(0,x,mult):
        for j in range(0,y,mult):
            p = board[int(j/mult)][int(i/mult)]
            if p == 0:
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
            elif p == 1:
                pygame.draw.rect(screen,(33,33,222),(i,j,mult-1,mult-1))
            elif p == 2:
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
                pygame.draw.circle(screen,(255,255,255),
                                   (i+int(mult/2),j+int(mult/2)),2)
            elif p == 3:
                pygame.draw.rect(screen,(0,0,0),(i,j,mult-1,mult-1))
                pygame.draw.circle(screen,(255,255,0),
                                   (i+int(mult/2),j+int(mult/2)),4)
            elif p == 4:
                pygame.draw.rect(screen,(255,255,255),(i,j,mult-1,mult-1))

def resetBoard():
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
    global board
    s = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2 or board[i][j] == 3:
                s = s + 1
    return 241 - s
    
def pacmanAgent(pac,g1,g2,g3,g4):
    px = pac.point[0]
    py = pac.point[1]
    gh = [g1.pacX,g1.pacY,g2.pacX,g2.pacY,g3.pacX,g3.pacY,g4.pacX,g4.pacY]
    gp = [g1.point[0],g1.point[1],g2.point[0],g2.point[1],g3.point[0],g3.point[1],g4.point[0],g4.point[1]]
    ch = []
    if py == 0 or py == 27:
        return random.randint(0,3)
    if board[px+1][py] != 1:
        ch.append([px+1,py,2])
    if board[px-1][py] != 1:
        ch.append([px-1,py,0])
    if board[px][py+1] != 1:
        ch.append([px,py+1,3])
    if board[px][py-1] != 1:
        ch.append([px,py-1,1])
    max2 = [-1,-1]
    for i in range(len(ch)):
        min1 = 9999
        for j in range(4):
            temp = abs(ch[i][0]-gp[2*j])+abs(ch[i][1]-gp[2*j+1])
            if temp < min1:
                min1 = temp
        if min1 > max2[0] and mode == 0:
            max2[0] = min1
            max2[1] = i
    if max2[0] <= 5 and mode == 0 or modeCt > 900:
        return ch[max2[1]][2]
    ch2 = []
    if board[px+1][py] != 1 and board[px+1][py] < 4 and (board[px+1][py] == 3 or board[px+1][py] == 2):
        ch2.append([px+1,py,2])
    if board[px-1][py] != 1 and board[px-1][py] < 4 and (board[px-1][py] == 3 or board[px-1][py] == 2):
        ch2.append([px-1,py,0])
    if board[px][py+1] != 1 and board[px][py+1] < 4 and (board[px][py+1] == 3 or board[px][py+1] == 2):
        ch2.append([px,py+1,3])
    if board[px][py-1] != 1 and board[px][py-1] < 4 and (board[px][py-1] == 3 or board[px][py-1] == 2):
        ch2.append([px,py-1,1])
    if len(ch2) == 0:
        pxy = px*width+py
        if pxy in nodes:
            return random.randint(0,3)
        if pac.bufX == 1 or pac.bufY == 1:
            if pac.bufX == 1:
                return 3
            else:
                return 2
        else:
            if pac.bufX == -1:
                return 1
            else:
                return 0
    ch = random.randint(0,len(ch2)-1)
    return ch2[ch][2]
    
def PacMan_Main():

    pygame.init()
    
    global x
    global y
    global mult
    screen = pygame.display.set_mode([x,y+mult])

    updateBoard(screen)

    pacman = Pacman(5)
    inky = Pacman(6)
    blinky = Pacman(7)
    pinky = Pacman(8)
    clyde = Pacman(9)

    global running
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and reflex_agent == False:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    pacman.move(0)
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    pacman.move(1)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    pacman.move(2)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    pacman.move(3)
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYDOWN and reflex_agent == True:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
        #screen.fill((255,255,255))
        global counter
        counter = counter + 1
        if counter % speed == 0:
            if reflex_agent == True:
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
            if mode == 1:
                if modeCt == 0:
                    inky.color = (25,25,166)
                    blinky.color = (25,25,166)
                    pinky.color = (25,25,166)
                    clyde.color = (25,25,166)
                modeCt = modeCt + 1
                if modeCt > 1000:
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
            if score < old:
                score = old
            outScore = "Score: " + str(score) + "     Highscore: " + str(highScore)
            font = pygame.font.SysFont('aerial', mult)
            text = font.render(outScore,True,(255,255,255))
            textRect = text.get_rect()
            textRect.center = (x/2,y+(mult/2))
            screen.blit(text,textRect)
        
            global reset
            if reset == True:
                score = 0
                reset = False
                pacman = Pacman(5)
                inky = Pacman(6)
                blinky = Pacman(7)
                pinky = Pacman(8)
                clyde = Pacman(9)
                resetBoard()
                updateBoard(screen)
        if counter > 999999999:
            counter = 0
        pygame.display.flip()

    pygame.quit()
