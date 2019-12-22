"""
    File name: main.py
    Description: An implementation of selection sort with user input
    Author: Emaz Khan
    Date created: 22/12/2019
    Version: 1.0
    Python Version: 2.7
"""
import time

import Swap

arrayLength = 0
numberArray = list()

# Main selection sort function
def selectionSort(numberList):
    for i in range(len(numberList)):

        minimumIndex = i
        print("Minimum index: " + str(minimumIndex))

        for l in range(i + 1, len(numberList)):
            if numberList[minimumIndex] > numberList[l]:
                minimumIndex = l
        print(numberArray)
        Swap.startSwap(numberList, i, minimumIndex)


arrayLength = int(input("How many numbers would you like sorting? "))
print("Enter the numbers")

# For loop to allow the input for the amount of numbers the user wants sorting
for i in range(arrayLength):
    a = raw_input("Number " + str(i + 1) + (": "))
    numberArray.append(int(a))

selectionSort(numberArray)
print ("Sorted array: " + str(numberArray))
