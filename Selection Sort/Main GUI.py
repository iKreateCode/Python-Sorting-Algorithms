"""
    File name: main.py
    Description: An implementation of selection sort with user input
    Author: Emaz Khan
    Date created: 22/12/2019
    Version: 1.0
    Python Version: 2.7
"""

from tkinter import *

import Swap

numberArray = list()

def arrayList(number):
    current = e.get()
    e.delete(0, END)
    arrayListEntry.delete(0, END)
    e.insert(0, str(current) +  str(number))
    numberArray.append(number)
    print numberArray


# Main selection sort function
def selectionSort(numberList):
    for i in range(len(numberList)):

        minimumIndex = i

        for l in range(i + 1, len(numberList)):
            if numberList[minimumIndex] > numberList[l]:
                minimumIndex = l

        Swap.startSwap(numberList, i, minimumIndex)
        e.delete(0, END)
        e.insert(0, numberArray)
        print numberArray

width = 300
height = 250

root = Tk()
frame = Frame(root, width=width, height=height)
frame.grid(row=0, column=0, columnspan=3)

e = Entry(root)
e.grid(row=1, column=1, columnspan=3)


arrayListLabel = Label(frame, text="Array List")
arrayListEntry = Entry(frame)
arrayListButton = Button(root, text="Enter", command=lambda: arrayList(arrayListEntry.get()))
arrayListButton.grid(row=0, column=3)

sortButton = Button(root, text="Sort", command=lambda: selectionSort(numberArray))
sortButton.grid(row=2, column=3)

arrayListLabel.grid(row=0, column=1)
arrayListEntry.grid(row=0, column=2)

root.mainloop()