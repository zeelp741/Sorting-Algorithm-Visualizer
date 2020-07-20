import random
import time
import pygame

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

def printArray():
    for i in range (len(randArray)):
        print(randArray[i])

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
        #Fits graph to screen ratio
    spacing = 5

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

        #Fills the screen to black
        screen.fill(BLACK)

        #Draws a bar graph for the random array
        for i in range (len(randArray)):
            pygame.draw.rect(screen, WHITE, (spacing * i, 512, 0, -5 * randArray[i]))
            

        #Update Screen
        pygame.display.flip()
        pygame.display.update()
    #insertionSort(len(randArray))
    #printArray()

    
if __name__ == "__main__":
    main()

