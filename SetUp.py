import pygame,keyboard

def selectBoardSize(screen,minCoords,maxCoords,textCoords):
    font = pygame.font.Font("C:/Users/owenp/OneDrive/Good Python stuff/2048/8-BIT WONDER.ttf", 27)
    background = pygame.image.load("Select Grid Size.png")
    greyedout = pygame.image.load("Greyed Out Rectangle.png")
    boardSize = 30

    while True:
        screen.blit(background,(0,0))
        label = font.render(str(boardSize),1,(0,0,0))
        screen.blit(label,textCoords) #displays current board size
        if boardSize == 10:
            screen.blit(greyedout,minCoords) # stops user from exceeding boundaries for board size: 10 <= x <= 50
        elif boardSize == 50:
            screen.blit(greyedout,maxCoords)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos() # records mouse position when clicked
                if x > 201 and x < 274 and y > 185 and y < 229: #compares mouse position with button area
                    if boardSize > 10:
                        boardSize = boardSize - 1
                elif x > 290 and x < 363 and y > 185 and y < 229:
                    if boardSize < 50:
                        boardSize = boardSize + 1
            if keyboard.is_pressed('enter'):
                return boardSize #Goes to next menu when enter is pressed

def selectFruitNum(screen,minCoords,maxCoords,textCoords): #All three select functions use the same principle - should have been one function but realised too late... and couldn't be bothered
    font = pygame.font.Font("C:/Users/owenp/OneDrive/Good Python stuff/2048/8-BIT WONDER.ttf", 27)
    background = pygame.image.load("Select Amount of Fruit.png")
    greyedout = pygame.image.load("Greyed Out Rectangle.png")
    fruitNum = 1

    while True:
        screen.blit(background,(0,0))
        label = font.render(str(fruitNum),1,(0,0,0))
        screen.blit(label,textCoords)
        if fruitNum == 1:
            screen.blit(greyedout,minCoords)
        elif fruitNum == 5:
            screen.blit(greyedout,maxCoords)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 201 and x < 274 and y > 185 and y < 229:
                    if fruitNum > 1:
                        fruitNum = fruitNum - 1
                elif x > 290 and x < 363 and y > 185 and y < 229:
                    if fruitNum < 5:
                        fruitNum = fruitNum + 1
            if keyboard.is_pressed('enter'):
                return fruitNum

def selectSpeed(screen,minCoords,maxCoords,textCoords):
    font = pygame.font.Font("C:/Users/owenp/OneDrive/Good Python stuff/2048/8-BIT WONDER.ttf", 27)
    background = pygame.image.load("Select Player Speed.png")
    greyedout = pygame.image.load("Greyed Out Rectangle.png")
    speed = 3

    while True:
        screen.blit(background,(0,0))
        label = font.render(str(speed),1,(0,0,0))
        screen.blit(label,textCoords)
        if speed == 1:
            screen.blit(greyedout,minCoords)
        elif speed == 5:
            screen.blit(greyedout,maxCoords)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 201 and x < 274 and y > 185 and y < 229:
                    if speed > 1:
                        speed = speed - 1
                elif x > 290 and x < 363 and y > 185 and y < 229:
                    if speed < 5:
                        speed = speed + 1
            if keyboard.is_pressed('enter'):
                return speed

def initialSetup():
    minCoords = (201,185)
    maxCoords = (290,185) # Coordinates for the 2 buttons and location of numbers
    textCoords = (130,190)

    pygame.init()
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption('Snake Set-up')
    boardSize = selectBoardSize(screen,minCoords,maxCoords,textCoords)
    fruitNum = selectFruitNum(screen,minCoords,maxCoords,textCoords) #Collects user's chosen variables
    speed = selectSpeed(screen,minCoords,maxCoords,textCoords)


    import SnakeCode
    SnakeCode.main(boardSize,fruitNum,speed) # starts the game with chosen variables

initialSetup()