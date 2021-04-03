# Sorting-Algorithm-Visualizer
A sorting algorithm visualizer using Pygame. Creates a random array and then sorts it using different sorting algorithms. 

## Instructions
![alt text](https://github.com/zeelp741/Sorting-Algorithm-Visualizer/blob/master/Sorting-Visualizer.png?raw=true)
When the program initlizly runs it will show a randomized array. Click on one of the six sorting Algorithms. Click randomize array after array is sorted. 
Press __'ESC'__ Key to exit the program

## Bubble Sort 
Starts on the left and compares adjacent elements in an array and swaps them if they are in the wrong place. Keeps passing through the list until list is sorted

### Time Complexity
Best: O(n)
Average: O(n^2)
Worst: O(n^2)

## Selection Sort
Travers through entire list and finds the minimum value. After the minimum value is found it puts it to the front of the array

### Time Complexity
Best: O(n^2)
Average: O(n^2)
Worst: O(n^2)

## Insertion Sort
This array is similair to way you would sort playing cards in your hand. The array is split into 2 parts: sorted and unsorted part. Travers through unsorted array part and finds the largest value and puts it the front of the sorted array part. 

### Time Complexity
Best: O(n)
Average: O(n^2)
Worst: O(n^2)

## Merge Sort
This is a divide and conquer alogirthm that uses recursion. 
 1. Finds the middle point of the array to divide it into two halves
 2. Calls Mergesort for first half
 3. Cals Mergesort for second half
 4. Merge the two halfs after sorted 

### Time Complexity
Best: O(n log(n))
Average: O(n log(n))
Worst: O(n log(n))

##Quick Sort
This is a divide and conquer algorithm alorithm that uses recusion
1. Pick a number that is considered the pivot 
2. All number that are less than the pivot are moved to the right while all greater are moved to the right 
3. Repeat and sort

### Time Complexity
Best: O(n log(n))
Average: O(n log(n))
Worst: O(n^2)


##Heap Sort
1. Build a max heap from the input data
2. The largest item is stored at the root of the heap. Replace it with the last item in the heap while also reducing the size of the heap by 1 
3. heapify the root of the tree
4. repeat until size of heap is greater than 1

### Time Complexity
Best: O(n log(n))
Average: O(n log(n))
Worst: O(n log(n))



Author: Zeel P
