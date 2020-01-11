"""
    File name: QuickSort.py
    Description: An implementation of quick sort with user input
    Author: Emaz Khan
    Date created: 23/12/2019
    Version: 1.0
    Python Version: 2.7
"""
import Swap

numberArray = [4,6,32,75,2,23,1,3]

def partition(array, leftSide, rightSide):
    l = leftSide
    pivot = numberArray[(leftSide + rightSide) / 2]

    for i in range(leftSide, rightSide):
        if (array[i] <= pivot):
            Swap.startSwap(array, i, l)
            l += 1
    Swap.startSwap(array, l, rightSide)
    return (leftSide)

#Main selection sort function
def quickSort(numberArray, leftSide, rightSide):
    if (leftSide < rightSide):
        a = partition(numberArray, leftSide, rightSide)
        quickSort(numberArray, leftSide, a-1);
        quickSort(numberArray, a+1, rightSide);

quickSort(numberArray, 0, len(numberArray) -1)
print ("Sorted array: " + str(numberArray))
