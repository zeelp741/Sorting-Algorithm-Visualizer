import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation


randArray = []

print("Start")

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

def drawGraph():
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.barh(randArray['value'])

    plt.show()

def main():
    # createRandArray()
    # selectionSort(len(randArray))
    # printArray()

    drawGraph()

if __name__ == "__main__":
    main()

