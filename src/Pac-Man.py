import pygame
import time
import random

pygame.init()

mult = 20
x = int(28*mult)
y = int(31*mult)
screen = pygame.display.set_mode([x,y])
counter = 0
mode = 0
modeCt = 0
running = True

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

class Pacman:
    def __init__(self,ch):
        self.type = ch
        if self.type == 5:
            self.pacX = 13*mult + int(mult/2)
            self.pacY = 23*mult + int(mult/2)
            self.color = (255,255,0)
            self.old = 0
        elif self.type == 6:
            self.pacX = 1*mult + int(mult/2)
            self.pacY = 1*mult + int(mult/2)
            self.color = (0,255,255)
            self.old = 2
        elif self.type == 7:
            self.pacX = 26*mult + int(mult/2)
            self.pacY = 1*mult + int(mult/2)
            self.color = (255,0,0)
            self.old = 2
        elif self.type == 8:
            self.pacX = 1*mult + int(mult/2)
            self.pacY = 29*mult + int(mult/2)
            self.color = (255,184,255)
            self.old = 2
        elif self.type == 9:
            self.pacX = 26*mult + int(mult/2)
            self.pacY = 29*mult + int(mult/2)
            self.color = (255,184,82)
            self.old = 2
        self.dirX = 0
        self.dirY = 0
        self.bufX = 0
        self.bufY = 0

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

    def calcMove(self):
        ch = random.randint(0,3)
        self.move(ch)

    def updatePos(self):
        found = False
        for i in range(0,x,mult):
            for j in range(0,y,mult):
                p = board[int(j/mult)][int(i/mult)]
                if p == self.type and not found:
                    if (int(i/mult+self.bufX) < 28 and int(i/mult+self.bufX) > 0 and
                        board[int(j/mult+self.bufY)][int(i/mult+self.bufX)] != 1 and
                        self.pacX % mult == int(mult/2) and
                        self.pacY % mult == int(mult/2)):
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
                            board[int(j/mult+self.dirY)][int(i/mult+self.dirX)] = self.type
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
                    global mode
                    if (((self.old > 4 and self.type == 5) or
                        (self.old == 5 and self.type > 4))
                        and mode == 0):
                        print("Game over!")
                        time.sleep(5)
                        running = False
                        pygame.quit()
                    if not any(2 in x for x in board):
                        print("You win!")
                        time.sleep(5)
                        running = False
                        pygame.quit()
                    if self.type == 5 and self.old == 3:
                        mode = 1
                        self.color = (255,255,255)
                    found = True

def updateBoard():
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

updateBoard()

pacman = Pacman(5)
inky = Pacman(6)
blinky = Pacman(7)
pinky = Pacman(8)
clyde = Pacman(9)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pacman.move(0)
            elif event.key == pygame.K_a:
                pacman.move(1)
            elif event.key == pygame.K_s:
                pacman.move(2)
            elif event.key == pygame.K_d:
                pacman.move(3)
            
    #screen.fill((255,255,255))

    counter = counter + 1
    if counter > 0:
        updateBoard()
        pacman.updatePos()
        inky.calcMove()
        inky.updatePos()
        blinky.calcMove()
        blinky.updatePos()
        pinky.calcMove()
        pinky.updatePos()
        clyde.calcMove()
        clyde.updatePos()
        counter = 0
        if mode == 1:
            modeCt = modeCt + 1
            if modeCt > 500:
                mode = 0
                modeCt = 0
                pacman.color = (255,255,0)
    pygame.display.flip()

pygame.quit()
