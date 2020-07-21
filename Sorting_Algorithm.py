import random
import time
import pygame

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 240, 0)

#Sets the screen 
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 512

# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

#Initializes an array
randArray = []

def createRandArray():
    num = 0 
    for i in range(100):
        num += 1
        randArray.append(num)

    random.shuffle(randArray)

def randomizeArray():
    random.shuffle(randArray)

def printArray():
    #Fits graph to screen ratio
    spacing = 5
    for i in range (len(randArray)):
        pygame.draw.rect(screen, WHITE, (spacing * i, 512, 0, -5 * randArray[i]))

def drawButtons():
    #Draws the Buttons
        #Randomize Array Button
    pygame.draw.rect(screen, GREEN, (710, 30, 130, 75))
        #Bubble Sort Button
    pygame.draw.rect(screen, GREEN, (550, 135, 130, 75))
        #Selectin Sort Button
    pygame.draw.rect(screen, GREEN, (710, 135, 130, 75))
        #Insertion Sort Button
    pygame.draw.rect(screen, GREEN, (870, 135, 130, 75))


def bubbleSort(length):
    # Implements the bubble sort algorithm to sort an array
    for i in range (length -1):
        for j in range(0, length - i -1):
            if randArray[j] > randArray[j+1]:
                randArray[j] , randArray[j+1] = randArray[j+1], randArray[j]

def selectionSort(length):
    # Implements the selection sort algorithm to sort an array
    for i in range (length-1):
        min = i
        for j in range(i + 1, length):
            if randArray[j] < randArray[min]:
                min = j
        randArray[i], randArray[min] = randArray[min], randArray[i]

def insertionSort(length):
    for i in range(1, length):
        key = randArray[i]

        j = i - 1

        while j >= 0 and key < randArray[j]:
            randArray[j+1] = randArray[j]
            j -= 1
        randArray[j+1] = key



def main():
        #Initialize pygame
    pygame.init()
        #Loops till the program is stopped
    running = True
        #Generates a Random Array
    createRandArray()
        
        # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            #Allows user to quit application
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                #Presses Escape also quits application
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

            #Gets the position of the mouse
        mouse = pygame.mouse.get_pos()
            #Checks to see if mouse has been clicked
        click = pygame.mouse.get_pressed()
            #Fills the screen to black
        screen.fill(BLACK)
            #Draws Array to Screen
        printArray()
        
        drawButtons()
        

        #Check to see if mouse is in the position
        if mouse[0] < 840 and mouse[0] > 710 and mouse[1] < 105 and mouse[1] > 30:
            if click[0] == 1:
                randomizeArray()
            
        
            #Sets the frame rate of the program
        clock.tick(15)
            #Update Screen
        pygame.display.flip()
        pygame.display.update()
    #insertionSort(len(randArray))
    #printArray()

    
if __name__ == "__main__":
    main()

