"""
    File name: SortingGUI.py
    Description: An implementation of selection sort with a GUI
    Author: Emaz Khan
    Date created: 22/12/2019
    Version: 1.1
    Python Version: 2.7
"""
import random

from tkinter import *

import Swap

numberArray = list()

def buttonEnabler():
    if (len(numberArray) >= 2):
        sortButton.config(state="active")

def arrayList(number):
    arrayListEntry.delete(0, END)
    numberArray.append(number)
    valueArrayLabel.config(text=str(numberArray))
    buttonEnabler()
    print numberArray

def randomiser():
    for i in range(10):
        numberArray.append(random.randint(1,100))
        valueArrayLabel.config(text=str(numberArray))
        print numberArray
    buttonEnabler()

def reset():
    valueArrayLabel.configure(text="[Empty]")
    minIndexLabel.configure(text="Minimum Index: none")
    del numberArray[:]

# Main selection sort function
def sort(numberList):
    if (dropVar.get() == "Selection"):
        for i in range(len(numberList)):

            minimumIndex = i
            print("\nMinimum index: " + str(minimumIndex))
            minIndexLabel.configure(text="Minimum Index: " + str(minimumIndex))

            for l in range(i + 1, len(numberList)):
                if numberList[minimumIndex] > numberList[l]:
                    minimumIndex = l
            print(numberArray)
            Swap.startSwap(numberList, i, minimumIndex)
            valueArrayLabel.config(text=str(numberArray))
            root.update()
            root.after(1000)
            valueArrayLabel.config(text=str(numberArray))
    else:
        print "Quicksort"

width = 300
height = 250

root = Tk()
root.title("Sorting Algorithm")
frame = Frame(root, width=width, height=height)


sortingAlgorithms = ["Selection", "Quicksort"]
dropVar = StringVar()

sortingCombo = OptionMenu(root, dropVar, "Selection", "Quicksort", command=lambda: sort(numberArray))
dropVar.set("Select")
sortingCombo.grid(row=0, column=1, sticky="ew")

valueArrayLabel = Label(root, text="[Empty]")
valueArrayLabel.grid(row=3, column=1)

minIndexLabel = Label(root, text="Minimum Index: none")
minIndexLabel.grid(row=2, column=1)


arrayListLabel = Label(root, text="Value")
arrayListLabel.grid(row=1, column=0)

arrayListEntry = Entry(root)
arrayListEntry.grid(row=1, column=1, sticky="ew")

arrayListButton = Button(root, text="Enter", command=lambda: arrayList(arrayListEntry.get()))
arrayListButton.grid(row=1, column=3)

sortButton = Button(root, text="Sort", command=lambda: sort(numberArray), state="disable")
sortButton.grid(row=4, column=1)

randomButton = Button(root, text="Randomise", command=lambda: randomiser())
randomButton.grid(row=5, column=1)

arrayListButton = Button(root, text="Reset", command=lambda: reset())
arrayListButton.grid(row=5, column=3)

root.mainloop()