"""
    File name: main.py
    Description: An implementation of selection sort with user input
    Author: Emaz Khan
    Date created: 22/12/2019
    Version: 1.0
    Python Version: 2.7
"""

arrayLength = 0
numberArray = list()


# Swap function for swaping the index in the array
def swap(array, index, number):
    swapObject = array[index]
    array[index] = array[number]
    array[number] = swapObject


# Main selection sort function
def selectionSort(numberList):
    for i in range(len(numberList)):

        minimumIndex = i

        for l in range(i + 1, len(numberList)):
            if numberList[minimumIndex] > numberList[l]:
                minimumIndex = l

        swap(numberList, i, minimumIndex)


arrayLength = int(input("How many numbers would you like sorting? "))
print("Enter the numbers")

# For loop to allow the input for the amount of numbers the user wants sorting
for i in range(arrayLength):
    a = raw_input("Number " + str(i + 1) + (": "))
    numberArray.append(int(a))

selectionSort(numberArray)
print ("Sorted array: " + str(numberArray))
