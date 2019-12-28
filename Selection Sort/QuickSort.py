"""
    File name: QuickSort.py
    Description: An implementation of quick sort with user input
    Author: Emaz Khan
    Date created: 23/12/2019
    Version: 1.0
    Python Version: 2.7
"""
# Imports the swap method
import Swap

arrayLength = 0
#numberArray = list()
numberArray = [4,6,32,75,2,23,1,3]

def compare (value, other):


# Main selection sort function
def quickSort(numberArray, leftSide, rightSide):

    l = leftSide
    r = rightSide
    pivot = numberArray[(leftSide + rightSide)/2]

    while (l <= r):
        while (numberArray[l] < 0):
            ++l
        while (numberArray[r] > 0):
            --r
        if (l <= r):
            Swap.startSwap(numberArray, l, r)
            ++l
            --r

    if (leftSide < r):
        sort(array, leftSide, r);
    if (l < rightSide):
        sort(array, l, rightSide);
    return array;

quickSort(numberArray)
print ("Sorted array: " + str(numberArray))
