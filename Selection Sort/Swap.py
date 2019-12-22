# Swap function for swaping the index in the array
def startSwap(array, firstIndex, secondIndex):
    swapObject = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = swapObject
    print("Number " + str(array[firstIndex]) + " swapped with number " + str(array[secondIndex]) + " in array\n")