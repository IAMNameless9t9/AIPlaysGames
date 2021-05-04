#Important Packages
import pygame
import sys
import random
import numpy as np
from datetime import datetime

HAS_SNAKE_AI = False
SCORE = 0
HIGHSCORE = 0
GENERATION = 0
ALLOW_EXPORTING = False

ENABLE_DATA_TOOLS = True
GOAL_SCORE = 20

DEATHS = 0
CURRENT_AVERAGE = 0
#================================
def SETUP_SNAKE_NEURAL(Setting):
    
    global ALLOW_EXPORTING
    if Setting == True:
        ALLOW_EXPORTING = True
    else:
        ALLOW_EXPORTING = False
#================================
def SETUP_SNAKE_AI(Setting):

    global HAS_SNAKE_AI
    if Setting == True:
        HAS_SNAKE_AI = True
    else:
        HAS_SNAKE_AI = False
#================================

def sigmoid(x):
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

class NN:
    def __init__(self, numOfInput, numOfOutput):
        self.NumOfInputs = numOfInput
        self.NumOfOutputs = numOfOutput
        self.IHWeights = np.random.rand(self.NumOfInputs,self.NumOfInputs)
        self.HOWeights = np.random.rand(self.NumOfInputs,self.NumOfOutputs)
        self.output = np.zeros(self.NumOfOutputs)

    def feedForward(self, x):
        self.hiddenLayer = sigmoid(np.dot(x + 0.1,self.IHWeights))
        self.output = sigmoid(np.dot(self.hiddenLayer, self.HOWeights))

    def backPropagate(self, y):
        d_HOWeights = np.dot(self.hiddenLayer.T, (4*(y - self.output) * sigmoid_derivative(self.output)))
        d_IHWeights = np.dot(self.hiddenLayer.T, (np.dot(4*(y - self.output) * sigmoid_derivative(self.output), self.HOWeights.T) * sigmoid_derivative(self.hiddenLayer)))

        self.HOWeights += d_HOWeights
        self.IHWeights += d_IHWeights

#Creation Of The Snake Class
class SNAKE(object):

    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (0, 255, 0)
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
            pygame.draw.rect(surface, (0, 255, 0), r, 1)
            
    def SNAKE_RIGHT(self):
        self.turn(RIGHT)
        
    def SNAKE_LEFT(self):
        self.turn(LEFT)
        
    def SNAKE_UP(self):
        self.turn(UP)
        
    def SNAKE_DOWN(self):
        self.turn(DOWN)
                             

    def handleKeys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if HAS_SNAKE_AI == False and ALLOW_EXPORTING == False:
                if event.type == pygame.KEYDOWN:
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
        self.color = (255, 0, 0)
        self.randomizePosition()

    def randomizePosition(self):
        self.position = (random.randint(3, GRID_WIDTH-3) * GRIDSIZE, random.randint(3, GRID_HEIGHT-3) * GRIDSIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (255, 0, 0), r, 1)


def DrawGrid(surface):

    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (255, 255, 255), r)
                
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (255, 255, 255), rr)  

def DrawBoarder(surface):

    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if y == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (0, 0, 0), r)  
            elif y == GRID_HEIGHT - 1:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (0, 0, 0), r)  
            elif x == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (0, 0, 0), r)  
            elif x == GRID_WIDTH - 1:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (0, 0, 0), r)  

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

CurrentSnakeAndFood = ()

def SetSnakeAndFood(snake, food):
    CurrentSnakeAndFood = (snake, food)

def GetCurrentSnakeAndFood():
    return CurrentSnakeAndFood

def Snake_Main():


    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = SNAKE()
    food = FOOD()
    #neuralNet = NN(12, 4)
    neuralNet = NN(12, 4)

    myfont = pygame.font.SysFont("monospace", 16)
    
    if ENABLE_DATA_TOOLS:
        startTime = datetime.now()
        currentTime = startTime.strftime("%H:%M:%S")
        print("==========\nStart Time: " + str(currentTime))

    while(True):
        
        clock.tick(15)
        
        snake.handleKeys()
        
        DrawGrid(surface)
        DrawBoarder(surface)
        snake.move()
        
        ######################################
        #GET SNAKE INFO TO EXPORT FOR TRAINING
        ######################################
        if ALLOW_EXPORTING == True:
            
            SnakeHeadX, SnakeHeadY = snake.getHeadPosition()
            TailX, TailY = snake.positions[snake.length - 1]
            FoodX, FoodY = food.position
            
            Above_Head = 0
            Below_Head = 0
            Left_Head = 0       #Where The Food Is In Relation To Player 
            Right_Head = 0      #1 Meaning It Exists in that Direction
                                #0 Meaning It Doesnt
            Head_Up = 0
            Head_Down = 0
            Head_Left = 0       #Direction The Player Is Currently Facing
            Head_Right = 0
            
            Tail_Up = 0
            Tail_Down = 0       #Direction The Tail is Facing in relation to the player
            Tail_Left = 0
            Tail_Right = 0
            
            State = []          #Takes in all 12 inputs and puts them into a state
            
            #Get The 4 Directions The Snake Can See And
            #Whether or not there is food in that direction
            
            if SnakeHeadY > FoodY: #To The Up
                Above_Head = 1
                Below_Head = 0
                Left_Head = 0
                Right_Head = 0
            if SnakeHeadY < FoodY: #To The Down
                Above_Head = 0
                Below_Head = 1
                Left_Head = 0
                Right_Head = 0
            if SnakeHeadX > FoodX: #To The Left
                Above_Head = 0
                Below_Head = 0
                Left_Head = 1
                Right_Head = 0
            if SnakeHeadX < FoodX: #To The Right
                Above_Head = 0
                Below_Head = 0
                Left_Head = 0
                Right_Head = 1
                                #The above and below code is calculating where the 
                                #food is and which direction should take priority 
                                #and then assigns a 1 to that direction
                                
            if SnakeHeadY == FoodY and SnakeHeadX > FoodX: #Go Left
                Above_Head = 0
                Below_Head = 0
                Left_Head = 1
                Right_Head = 0
            if SnakeHeadY == FoodY and SnakeHeadX < FoodX: #Go Right
                Above_Head = 0
                Below_Head = 0
                Left_Head = 0
                Right_Head = 1
            if SnakeHeadX == FoodX and SnakeHeadY > FoodY: #Go Up
                Above_Head = 1
                Below_Head = 0
                Left_Head = 0
                Right_Head = 0
            if SnakeHeadX == FoodX and SnakeHeadY < FoodY: #Go Down
                Above_Head = 0
                Below_Head = 1
                Left_Head = 0
                Right_Head = 0
            
            
            #Get The Current Head Directions
            if snake.direction == UP:
                Head_Up = 1
                Head_Down = 0
                Head_Left = 0
                Head_Right = 0
            if snake.direction == DOWN:
                Head_Up = 0
                Head_Down = 1
                Head_Left = 0
                Head_Right = 0
            if snake.direction == LEFT:
                Head_Up = 0
                Head_Down = 0
                Head_Left = 1
                Head_Right = 0
            if snake.direction == RIGHT:
                Head_Up = 0
                Head_Down = 0
                Head_Left = 0
                Head_Right = 1
                
                
            if Head_Up == 1 and Below_Head == 1: #Food is behind snake below
                Above_Head = 0
                Below_Head = 1
                Left_Head = 1
                Right_Head = 1
            elif Head_Down == 1 and Above_Head == 1: #Food is behind snake above
                Above_Head = 1
                Below_Head = 0
                Left_Head = 1
                Right_Head = 1
            elif Head_Left == 1 and Right_Head == 1: #Food is behind snake right
                Above_Head = 1
                Below_Head = 1
                Left_Head = 0
                Right_Head = 1
            elif Head_Right == 1 and Left_Head == 1: #Food is behind snake left
                Above_Head = 1
                Below_Head = 1
                Left_Head = 1
                Right_Head = 0
                
            #elif Head_Up == 1 and Above_Head == 1: #Food is front snake up
                #Above_Head = 1
                #Below_Head = 0
                #Left_Head = 0
                #Right_Head = 0
            #elif Head_Down == 1 and Below_Head == 1: #Food is front snake down
                #Above_Head = 0
                #Below_Head = 1
                #Left_Head = 0
                #Right_Head = 0
            #elif Head_Left == 1 and Left_Head == 1: #Food is front snake left
                #Above_Head = 0
                #Below_Head = 0
                #Left_Head = 0
                #Right_Head = 1
            #elif Head_Right == 1 and Right_Head == 1: #Food is front snake right
                #Above_Head = 0
                #Below_Head = 0
                #Left_Head = 0
                #Right_Head = 1
            
            #Get The Current Tail Directions using head as a reference
            if TailX >= SnakeHeadX and TailY >= SnakeHeadY: #Going Up
                Tail_Up = 1
                Tail_Down = 0
                Tail_Left = 0
                Tail_Right = 0
            if TailX >= SnakeHeadX and TailY <= SnakeHeadY: #Going Down
                Tail_Up = 0
                Tail_Down = 1
                Tail_Left = 0
                Tail_Right = 0
            if TailX <= SnakeHeadX and TailY >= SnakeHeadY: #Going Up
                Tail_Up = 1
                Tail_Down = 0
                Tail_Left = 0
                Tail_Right = 0
            if TailX <= SnakeHeadX and TailY <= SnakeHeadY: #Going Down
                Tail_Up = 0
                Tail_Down = 1
                Tail_Left = 0
                Tail_Right = 0
            if TailX == SnakeHeadX: #Following Head X
                Tail_Up = 0
                Tail_Down = 0
                Tail_Left = Head_Left
                Tail_Right = Head_Right
            if TailY == SnakeHeadY: #Following Head Y
                Tail_Up = Head_Up
                Tail_Down = Head_Down
                Tail_Left = 0
                Tail_Right = 0
                
            #Calculate The Answer
            
            #Put all your inputs into a state array like below.
            #State = [Above_Head, Below_Head, Left_Head, Right_Head, Head_Up, Head_Down, Head_Left, Head_Right, Tail_Up, Tail_Down, Tail_Left, Tail_Right]
            State = np.array([[Above_Head, Below_Head, Left_Head, Right_Head, Head_Up, Head_Down, Head_Left, Head_Right, Tail_Up, Tail_Down, Tail_Left, Tail_Right]])
            Output = np.array([[Above_Head,Below_Head,Left_Head,Right_Head]])
            
            #input the state into feedforward
            neuralNet.feedForward(State)
            
            #for bp you can choose whatever, i made food more important
            neuralNet.backPropagate(Output)
            
            currentMax = 0
            currentMaxIndex = 0
            counter = 0
            
            out = neuralNet.output
            
            for i in out:
                ##print(i)
                for j in i:
                    if j > currentMax:          #This code calculates which prediction was the largest and keeps the index
                        currentMax = j
                        currentMaxIndex = counter
                    counter+=1
                counter = 0
            
            if currentMaxIndex == 0:
                snake.SNAKE_UP()
            if currentMaxIndex == 1:
                snake.SNAKE_DOWN()              #This uses the found index to move the snake.
            if currentMaxIndex == 2:
                snake.SNAKE_LEFT()
            if currentMaxIndex == 3:
                snake.SNAKE_RIGHT()
            
            #print("=========")
            #for i in State:
            #    print(i)
            #print("=========")
            #Export To Neural Network
            
        
        #print(snake.direction)


        if HAS_SNAKE_AI == True:
        
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
                
        ##SnakeHead_X, SnakeHead_Y = snake.getHeadPosition()
        ##print("SNAKE X: " + str(SnakeHead_X) + "\tSNAKE Y: " + str(SnakeHead_Y))

        #resets score when snake dies
        if snake.dead == 1:
            global DEATHS
            DEATHS += 1
            snake.dead = 0
            global SCORE
            global HIGHSCORE
            if SCORE >= HIGHSCORE:
                HIGHSCORE = SCORE
            SCORE = 0
            
            global CURRENT_AVERAGE
            CURRENT_AVERAGE + CURRENT_AVERAGE * DEATHS
            CURRENT_AVERAGE += SCORE
            CURRENT_AVERAGE = CURRENT_AVERAGE / DEATHS
        
        #Wall Collisions
        SnakeHeadX, SnakeHeadY = snake.getHeadPosition()
        global GENERATION
        if (SnakeHeadX == 0):
            GENERATION += 1
            snake.reset()
        elif (SnakeHeadX == 440 + GRIDSIZE):
            GENERATION += 1
            snake.reset()
        elif (SnakeHeadY == 0):
            GENERATION += 1
            snake.reset()
        elif (SnakeHeadY == 440 + GRIDSIZE):
            GENERATION += 1
            snake.reset()

        if snake.getHeadPosition() == food.position:
            snake.length += 1
            SCORE += 1
            food.randomizePosition()
            
        if ENABLE_DATA_TOOLS:
            global GOAL_SCORE
            if HIGHSCORE >= GOAL_SCORE:
                endTime = datetime.now()
                duration = (endTime - startTime)
                currentEndTime = endTime.strftime("%H:%M:%S")
                print("End Time: " + str(currentEndTime))
                print("Time Taken: " + str(duration))
                print("EPOCHS TAKEN: " + str(GENERATION) + "\nGOAL SCORE: " + str(GOAL_SCORE) + "\nFINAL SCORE: " + str(HIGHSCORE) + "\n==========")
                    
                SCORE = 0
                GENERATION = 0
                HIGHSCORE = 0
                Snake_Main()
            
        snake.draw(surface)
        food.draw(surface)
        
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(SCORE), 1, (0, 0, 0))
        screen.blit(text, (35, 25))
        
        text = myfont.render("Iteration {0}".format(GENERATION), 1, (0, 0, 0))
        screen.blit(text, ((SCREEN_WIDTH/3), 25))

        hstext = myfont.render("High Score {0}".format(HIGHSCORE), 1, (0, 0, 0))
        screen.blit(hstext, (SCREEN_WIDTH-165, 25))
        
        pygame.display.update()


##Snake_Main()

        
