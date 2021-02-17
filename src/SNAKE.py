#Important Packages
import pygame
import sys
import random

#Creation Of The Snake Class
class SNAKE(object):

    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        self.dead = 0

    def getHeadPosition(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.getHeadPosition()
        x, y = self.direction
        new = (((cur[0] + (x*GRIDSIZE)) % SCREEN_WIDTH) , ((cur[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT))
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.dead = 1
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)
                             

    def handleKeys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                    
#Creation Of The Food Class
class FOOD(object):

    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomizePosition()

    def randomizePosition(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


def DrawGrid(surface):

    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (84, 194, 205), rr)               

#Important Global Variables

SCREEN_HEIGHT = 480
SCREEN_WIDTH = 480

GRIDSIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():


    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = SNAKE()
    food = FOOD()

    myfont = pygame.font.SysFont("monospace", 16)

    score = 0
    highscore = 0
    while(True):
        
        clock.tick(10)
        
        snake.handleKeys()
        
        DrawGrid(surface)
        snake.move()

        sx, sy = snake.getHeadPosition()
        fx, fy = food.position


        #Basic Bot
        if sx > fx: #Go Left
            snake.turn(LEFT)
        elif sx < fx: #Go Right
            snake.turn(RIGHT)
        elif sy < fy: #Go Down
            snake.turn(DOWN)
        elif sy > fy: #Go Up
            snake.turn(UP)

        #resets score when snake dies
        if snake.dead == 1:
            snake.dead = 0
            if score >= highscore:
                highscore = score
            score = 0
        

        if snake.getHeadPosition() == food.position:
            snake.length += 1
            score += 1
            food.randomizePosition()
            
        snake.draw(surface)
        food.draw(surface)
        
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))


        hstext = myfont.render("High Score {0}".format(highscore), 1, (0, 0, 0))
        screen.blit(hstext, (SCREEN_WIDTH-145, 10))
        
        pygame.display.update()


main()

        
