# Swap function for swaping the index in the array
def startSwap(array, index, number):
    swapObject = array[index]
    array[index] = array[number]
    array[number] = swapObject