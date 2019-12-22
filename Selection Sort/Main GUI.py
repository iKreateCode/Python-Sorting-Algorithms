"""
    File name: main.py
    Description: An implementation of selection sort with user input
    Author: Emaz Khan
    Date created: 22/12/2019
    Version: 1.0
    Python Version: 2.7
"""
import random

from tkinter import *

import Swap

numberArray = list()

def arrayList(number):
    arrayListEntry.delete(0, END)
    numberArray.append(number)
    e.config(text=str(numberArray))
    print numberArray

def randomiser():
    for i in range(10):
        numberArray.append(random.randint(1,100))
        e.config(text=str(numberArray))
        print numberArray


# Main selection sort function
def selectionSort(numberList):
    for i in range(len(numberList)):

        minimumIndex = i
        print("\nMinimum index: " + str(minimumIndex))

        for l in range(i + 1, len(numberList)):
            if numberList[minimumIndex] > numberList[l]:
                minimumIndex = l
        print(numberArray)
        Swap.startSwap(numberList, i, minimumIndex)
        e.config(text=str(numberArray))
        root.update()
        root.after(1000)
        e.config(text=str(numberArray))


width = 300
height = 250

root = Tk()
frame = Frame(root, width=width, height=height)
frame.grid(row=3, column=0, columnspan=3)

e = Label(root, text="Arraylist")
e.grid(row=1, column=1)


arrayListLabel = Label(root, text="Array List")
arrayListEntry = Entry(root)
arrayListButton = Button(root, text="Enter", command=lambda: arrayList(arrayListEntry.get()))
arrayListButton.grid(row=0, column=3)

sortButton = Button(root, text="Sort", command=lambda: selectionSort(numberArray))
sortButton.grid(row=2, column=1)

randomButton = Button(root, text="Randomise", command=lambda: randomiser())
randomButton.grid(row=3, column=1)

arrayListLabel.grid(row=0, column=0)
arrayListEntry.grid(row=0, column=1)

root.mainloop()