import random
import time
import pygame

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 240, 0)

#Sets the screen 
SCREEN_WIDTH = 1355
SCREEN_HEIGHT = 500

#Sets the Button 
BUTTON_WIDTH = 140
BUTTON_HEIGHT = 75

# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

#Initializes an array
Array = []

def createRandArray():
    num = 0 
    for i in range(250):
        num += 1
        Array.append(num)
    random.shuffle(Array)

def randomizeArray():
    random.shuffle(Array)
    update()


def drawButtons():
    #Draws the Buttons
        #Randomize Array Button
    pygame.draw.rect(screen, GREEN, (20, 20, (BUTTON_WIDTH *2) + 10, BUTTON_HEIGHT))
        #Bubble Sort Button
    pygame.draw.rect(screen, GREEN, (20, 125, BUTTON_WIDTH, BUTTON_HEIGHT))
        #Selectin Sort Button
    pygame.draw.rect(screen, GREEN, (170, 125, BUTTON_WIDTH, BUTTON_HEIGHT))
        #Insertion Sort Button
    pygame.draw.rect(screen, GREEN, (20, 210, BUTTON_WIDTH, BUTTON_HEIGHT))
    
    #Draws the text for Buttons
    font = pygame.font.Font('freesansbold.ttf', 20)
        #Randomize Array Text
    text = font.render('Randomize Array', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (160, 60)
    screen.blit(text, textRect)
        #Bubble Sort Text
    text = font.render('Bubble Sort', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (90, 165)
    screen.blit(text, textRect)
        #Selection Sort Text
    text = font.render('Selection Sort', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (240, 165)
    screen.blit(text, textRect)
        #Insertion Sort Text
    text = font.render('Insertion Sort', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (90, 250)
    screen.blit(text, textRect)

def checkEvents():
    #Checks to see if program has been quit
    for event in pygame.event.get():
        #Allows user to quit application
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #Presses Escape also quits application
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()


def bubbleSort(length):
    # Implements the bubble sort algorithm to sort an array
    for i in range (length -1):
        for j in range(0, length - i -1):
            if Array[j] > Array[j+1]:
                Array[j] , Array[j+1] = Array[j+1], Array[j]
                update()

def selectionSort(length):
    # Implements the selection sort algorithm to sort an array
    for i in range (length):
        min = i
        for j in range(i + 1, length):
            if Array[j] < Array[min]:
                min = j
                update()
        Array[min], Array[i] = Array[i], Array[min]
        update()
        

def insertionSort(length):
    for i in range(length):
        key = Array[i]
        hold = i

        while hold > 0 and Array[hold-1] > key:
            Array[hold] = Array[hold-1]
            hold -= 1
            update()
        Array[hold] = key
        update()

def update():
    #Fills the screen to black
    screen.fill(BLACK)
    for i in range (len(Array)):
        pygame.draw.rect(screen, WHITE, ((4 * i) + 350, 512, 0, -2 * Array[i]))
    checkEvents()
    pygame.display.update()


def main():
        #Initialize pygame
    pygame.init()
        #Loops till the program is stopped
    running = True
        #Generates a Random Array
    createRandArray()
        # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    update()

    while running:
            #Gets the position of the mouse
        mouse = pygame.mouse.get_pos()
            #Checks to see if mouse has been clicked
        click = pygame.mouse.get_pressed()  
            #Checks to see if program has been quit
        checkEvents()
            #Draws all the buttons to the screen
        drawButtons()
        

        #Button Logic
        if mouse[0] < 20 + (BUTTON_WIDTH*2)+10 and mouse[0] > 20 and mouse[1] < 20 + BUTTON_HEIGHT and mouse[1] > 20:
            if click[0] == 1:
                randomizeArray()
        if mouse[0] < 20 + BUTTON_WIDTH and mouse[0] > 20 and mouse[1] < 125 + BUTTON_HEIGHT and mouse[1] > 125:
            if click[0] == 1:
                bubbleSort(len(Array))
        if mouse[0] < 170 + BUTTON_WIDTH and mouse[0] > 170 and mouse[1] < 125 + BUTTON_HEIGHT and mouse[1] > 125:
            if click[0] == 1:
                selectionSort(len(Array))
        if mouse[0] < 20 + BUTTON_WIDTH and mouse[0] > 20 and mouse[1] < 210 + BUTTON_HEIGHT and mouse[1] > 210:
            if click[0] == 1:
                insertionSort(len(Array))
            
        
            #Sets the frame rate of the program
        clock.tick(60)
            #Update Screen

        pygame.display.update()

    #insertionSort(len(randArray))
    #printArray()

    
if __name__ == "__main__":
    main()

