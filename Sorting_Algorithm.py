"""
 * Author: Zeel P
 * Date: July 19, 2020 
 * Project: Sorting Algorithm Visualizer
 * Description: An interactive program which allows the user to see and learn how different sorting algorithms sort random lists
"""


import random
import time
import pygame


#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 240, 0)
RED = (240, 0, 0)

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
size = 250

def createRandArray():
    num = 0 
    for i in range(size):
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
        #Merge Sort Button
    pygame.draw.rect(screen, GREEN, (170, 210, BUTTON_WIDTH, BUTTON_HEIGHT))
        #Quick Sort Button
    pygame.draw.rect(screen,GREEN, (20, 295, BUTTON_WIDTH, BUTTON_HEIGHT))
        #Heap Sort Button
    pygame.draw.rect(screen, GREEN,(170, 295, BUTTON_WIDTH, BUTTON_HEIGHT))
        #Bucket Sort Button
    pygame.draw.rect(screen, GREEN,(20, 380, BUTTON_WIDTH, BUTTON_HEIGHT))
        #Radix Sort Button
    pygame.draw.rect(screen, RED,(170, 380, BUTTON_WIDTH, BUTTON_HEIGHT))
    
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
        #Merge Sort Text
    text = font.render('Merge Sort', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (240, 250)
    screen.blit(text, textRect)
        #Quick Sort Text
    text = font.render('Quick Sort', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (90, 335)
    screen.blit(text, textRect)
        #Heap Sort Text
    text = font.render('Heap Sort', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (240, 335)
    screen.blit(text, textRect)
        #Shell Sort Text
    text = font.render('Shell Sort', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (90, 420)
    screen.blit(text, textRect)
        #Radix Sort Text
    text = font.render('Radix Sort', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (240, 420)
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

# Implements the bubble sort algorithm to sort an array
def bubbleSort(length):
    #Goes through all Array Elements
    for i in range (length -1):
        #Last i th element is already in place
        for j in range(0, length - i -1):
            #Goes through the array from 0 to length - 1 -i
            if Array[j] > Array[j+1]:       #Swaps if the number found is greater than the next element
                Array[j] , Array[j+1] = Array[j+1], Array[j]
                update()

# Implements the selection sort algorithm to sort an array
def selectionSort(length):
    #Goes through all Array Elements
    for i in range (length):
        #Finds the minimum value in unsorted array
        min = i
        for j in range(i + 1, length):
            if Array[j] < Array[min]:
                min = j
                update()
        #swaps the minimum elements with the first unswapped array element
        Array[min], Array[i] = Array[i], Array[min]
        update()

#Implents the Insertion Sort Algorithm   
def insertionSort(Array):
    #Goes through all array elements
    for i in range(len(Array)):
        key = Array[i]
        hold = i

        #Moves elements of Array[0...n-1] that are larger than the key to one position ahead of their current position
        while hold > 0 and Array[hold-1] > key:
            Array[hold] = Array[hold-1]
            hold -= 1
            update()
        Array[hold] = key
        update()
    return Array

#Implements the Merge Sort Algorithm
def mergeSort(arr,left,right): 
    if left < right: 
  
        m = (left+(right-1))//2
  
        # Sorts the left and right halves
        mergeSort(arr, left, m)
        update() 
        mergeSort(arr, m+1, right) 
        update()
        #Merge halves together
        merge(arr, left, m, right) 
               
def merge(arr, left, middle, right): 
    n1 = middle - left + 1
    n2 = right- middle 
  
    #Creates temp arrays
    Left = [0] * (n1) 
    Right = [0] * (n2) 
  
    #Copies data to temp arrays
    for i in range(0 , n1): 
        Left[i] = arr[left + i] 
  
    for j in range(0 , n2): 
        Right[j] = arr[middle + 1 + j] 
  
    #Merge the temp arrays back into the array
    i = j = 0       #Initial index for first and second subarray
    k = left        #Initial index of merged subarray
  
    while i < n1 and j < n2 : 
        if Left[i] <= Right[j]: 
            arr[k] = Left[i] 
            i += 1
        else: 
            arr[k] = Right[j] 
            j += 1
        k += 1 
    update()

    #Copies the data from Left side
    while i < n1: 
        arr[k] = Left[i] 
        i += 1
        k += 1
        update()

    #Copies the data from the Right side
    while j < n2: 
        arr[k] = Right[j] 
        j += 1
        k += 1
        update()

#Implements the Quick Sort Algorithm
def quickSort(Array, low, high):
    #Selects an element in the array as the pivot point. Elements larger than the pivot point are put 
    # to the right of the pivot, smaller elements are put to the left of the pivot. Repeat 
    if low < high:
        part = partition(Array, low, high)

        #Sorts elements before and after the pivot point
        update()
        quickSort(Array, low, part-1)
        update()
        quickSort(Array, part+1, high)
        update()

#Function takes the last element as the pivot point and then places it in 
#the correct place in the sorted array and places all smaller than the 
#pivot to the left of the larger to the right
def partition(Array, low, high):
    i = low - 1             #Indexs the smaller element
    pivot = Array[high]     #Sets the Pivot point     
   
    for j in range (low, high):
        #Checks if current element is larger or smaller than the pivot
       if Array[j] <= pivot:
           #Increments index of the smaller element
           i += 1
           Array[i], Array[j] = Array[j], Array[i]
           update()
    Array[i+1], Array[high] = Array[high], Array[i+1]
    update()
    return (i+1)

#Implements the Heap Sort Algorithm
def heapSort(Array, length):
    #Sets the Max Heap
    
    #Sets the last parent location
    for i in range(length // 2 - 1, -1, -1):
        heapify(Array, length, i)

    #Extracts elements one by one
    for i  in range(length - 1, 0, -1):
        Array[i], Array[0] = Array[0], Array[i]
        heapify(Array, i, 0)
        update()
    
def heapify(arr, n , i):
    #Initalizes largest root
    largest = i 
    left = 2 * i + 1 
    right = 2 * i + 2

    # See if left child of root exists and is greater than root 
    if left < n and arr[i] < arr[left]:
        largest = left
    # See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right 

    #Changes root if neccassary
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        update()
        heapify(arr, n , largest)       
        update()

#Implements the Shell Sort Algorithm
def shellSort(Array, length):
    #Start off with a gap that is n /2. The elements in the array are 
    # compared to other elements that are the gap away instead of adjacent 
    # values. Keep reducing the gap by n/2 until array is sorted
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            #Add Array[i] to the elements that have been gap sorted. Save Array[i] in temp and make a hole at position i 
            temp = Array[i]
            #Keep shifting gapsorted elements until position is found
            j = i
            while j >= gap and Array[j - gap] > temp:
                Array[j] = Array[j - gap]
                j -= gap

            #Puts temp in its correct location
            Array[j] = temp
            update()

        gap //= 2

def radixSort():
    #In Progress 
    print('In Progess')


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
        #Updates the screen
    update()
        #Length of the array
    length = len(Array)
        # imports and sets logo for window
    icon = pygame.image.load("logo.png")
    pygame.display.set_icon(icon)
    
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
                bubbleSort(length)
        if mouse[0] < 170 + BUTTON_WIDTH and mouse[0] > 170 and mouse[1] < 125 + BUTTON_HEIGHT and mouse[1] > 125:
            if click[0] == 1:
                selectionSort(length)
        if mouse[0] < 20 + BUTTON_WIDTH and mouse[0] > 20 and mouse[1] < 210 + BUTTON_HEIGHT and mouse[1] > 210:
            if click[0] == 1:
                insertionSort(Array)
        if mouse[0] < 170 + BUTTON_WIDTH and mouse[0] > 170 and mouse[1] < 210 + BUTTON_HEIGHT and mouse[1] > 210:
            if click[0] == 1:
                mergeSort(Array, 0,length -1 )   
        if mouse[0] < 20 + BUTTON_WIDTH and mouse[0] > 20 and mouse[1] < 295 + BUTTON_HEIGHT and mouse[1] > 295:
            if click[0] == 1:
                quickSort(Array, 0, length - 1)
        if mouse[0] < 170 + BUTTON_WIDTH and mouse[0] > 170 and mouse[1] < 295 + BUTTON_HEIGHT and mouse[1] > 295:
            if click[0] == 1:
                heapSort(Array,length)
        if mouse[0] < 20 + BUTTON_WIDTH and mouse[0] > 20 and mouse[1] < 380 + BUTTON_HEIGHT and mouse[1] > 380:
            if click[0] == 1:
                shellSort(Array, length)
        if mouse[0] < 170 + BUTTON_WIDTH and mouse[0] > 170 and mouse[1] < 380 + BUTTON_HEIGHT and mouse[1] > 380:
            if click[0] == 1:
                radixSort()

            
            #Sets the frame rate of the program
        clock.tick(60)
            
            #Update Screen
        pygame.display.update()
    
if __name__ == "__main__":
    main()
    print("Starting")

