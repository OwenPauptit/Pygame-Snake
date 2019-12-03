import random,time,pygame,keyboard

class Game:

    def __init__(self,boardSize,startingLength,fruitNum,speed):

        self.padding = 2 #gap between each block
        self.scale = 20 #multipolier from array index (+1) to get to pixel location
        self.boardSize = boardSize

        self.grid = [] # creating the array/grid
        for y in range(0,boardSize):
            temp = []
            for x in range(0,boardSize):
                temp.append(0)
            self.grid.append(temp)

        centre = int(boardSize/2 -1) #placing initial body of snake on the grid
        self.snakePos = []
        for i in range(0,startingLength):
            self.snakePos.append([centre,centre+i])

        for i in range(len(self.snakePos)): # setting values in grid array to 1 where snake is, so can easily detect collisions
            x = self.snakePos[i][0]
            y = self.snakePos[i][1]
            self.grid[y][x] = 1

        self.direction = "up"
        self.speed = speed
        self.fruitPos = []
        self.fruitNum = fruitNum
        self.placeFruit(self.fruitNum) #spawns the number of fruit chosen by player

    def move(self,screen):
        x = self.snakePos[0][0]
        y = self.snakePos[0][1]

        if self.direction == "up": # finding next coordinates depending on direction of movement
            y= y- 1
        elif self.direction =="down":
            y= y+ 1
        elif self.direction =="right":
            x=x+ 1
        elif self.direction == "left":
            x=x- 1

        if x < 0 or x > self.boardSize-1 or y < 0 or y > self.boardSize-1: #checks to see if snake collides with the edge of the board
            print ("hit side")
            self.gameover(screen)

        self.snakePos.insert(0,[x,y]) #adds new block onto 'head' of snake
        if self.grid[y][x] == 1:
            print ("Ate self")
            self.gameover(screen)
        elif self.grid[y][x] == 0:
            self.grid[self.snakePos[len(self.snakePos)-1][1]][self.snakePos[len(self.snakePos)-1][0]] = 0
            del self.snakePos[len(self.snakePos)-1] # removes last block of snake
        elif self.grid[y][x] == 2: #2 is the value of a fruit
            for i in range(0,len(self.fruitPos)):
                if self.fruitPos[i] == [x,y]: # gets rid of the fruit that was collided with
                    del self.fruitPos[i]
                    break
            self.placeFruit()
        self.grid[y][x] = 1

    def updateDisplay(self,screen):
        screen.fill((255,255,255))
        #Snake
        for i in range(0,len(self.snakePos)):
            x = self.scale * self.snakePos[i][0] + self.padding
            y = self.scale * self.snakePos[i][1] + self.padding
            Rect = (x,y,self.scale-self.padding,self.scale-self.padding)
            pygame.draw.rect(screen,(0,0,0),Rect)

        #Fruit
        for i in range(0,len(self.fruitPos)):
            x = self.scale * self.fruitPos[i][0] + self.padding
            y = self.scale * self.fruitPos[i][1] + self.padding
            Rect = (x,y,self.scale-self.padding,self.scale-self.padding)
            pygame.draw.rect(screen,(255,0,0),Rect)

        pygame.display.update()

    def placeFruit(self,amount=1): #spawning fruit on the grid
        for i in range(0,amount):
            while True:
                x = random.randint(0,self.boardSize-1)
                y = random.randint(0,self.boardSize-1)
                if self.grid[y][x] == 0:
                    self.grid[y][x] = 2
                    self.fruitPos.append([x,y])
                    break

    def gameover(self,screen):
        if self.boardSize < 15: # different text sizes depending on grid size - categorized
            largeSize = 18
            smallSize = 9
            textPad = 5
            lower = 30
        elif self.boardSize < 20:
            largeSize = 27
            smallSize = 14
            textPad = 10
            lower = 50
        elif self.boardSize < 30:
            largeSize = 45
            smallSize = 18
            textPad = 12
            lower = 70
        elif self.boardSize < 40:
            largeSize = 54
            smallSize = 27
            textPad = 20
            lower = 90
        else:
            largeSize = 63
            smallSize = 36
            textPad = 30
            lower = 110
        bigFont = pygame.font.Font("C:/Users/owenp/OneDrive/Good Python stuff/2048/8-BIT WONDER.ttf",largeSize)
        smallFont = pygame.font.Font("C:/Users/owenp/OneDrive/Good Python stuff/2048/8-BIT WONDER.ttf", smallSize)
        label_1 = bigFont.render("GAMEOVER",1,(0,0,0))
        label_2 = smallFont.render("Press Enter to restart",1,(0,0,0))
        label_3 = smallFont.render("Press s for setup",1,(0,0,0))

        screen.blit(label_1,(textPad,textPad))
        screen.blit(label_2,(textPad,lower))
        screen.blit(label_3,(textPad,self.boardSize*(self.scale-1)-textPad))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if keyboard.is_pressed('enter'):
                    main(self.boardSize,self.fruitNum,self.speed) # restart with same settings
                if keyboard.is_pressed('s'):
                    import SetUp #go to set-up menus
                    SetUp.initialSetup()


def main(boardSize=30,fruitNum=1,speed=3): #defaults if file is opened before setup
    pygame.init()
    game = Game(boardSize,3,fruitNum,speed)
    screen = pygame.display.set_mode((boardSize * game.scale, boardSize * game.scale))
    pygame.display.set_caption('Snake')
    screen.fill((0, 0, 0))
    game.updateDisplay(screen)
    time.sleep(2)
    playing = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                playing = True # so game only starts when player presses down on the keyboard
                if event.key == pygame.K_UP:
                    game.direction = "up"
                if event.key == pygame.K_DOWN:
                    game.direction = "down"
                if event.key == pygame.K_LEFT:
                    game.direction = "left"
                if event.key == pygame.K_RIGHT:
                    game.direction = "right"
                if event.key == pygame.K_UP:
                    game.direction = "up" # repeated so that user can press keys in vitually any order in the time before the snake moves
                if event.key == pygame.K_DOWN: # i.e. if the user presses down by mistake, then immediately presses up. the program will set direction to up
                    game.direction = "down"
                if event.key == pygame.K_LEFT:
                    game.direction = "left"
                if event.key == pygame.K_RIGHT:
                    game.direction = "right"
        if playing:
            game.move(screen)
            game.updateDisplay(screen)
            delay = 0.3 - speed * 0.05 #greater the speed, smaller the delay
            time.sleep(delay)

if __name__ == "__main__": #If file is opened via import, it will not start automatically - will wait until called
    main()