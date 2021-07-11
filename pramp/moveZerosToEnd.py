def moveZerosToEnd(array):
    leftPointer = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[leftPointer] = array[leftPointer], array[i]
            leftPointer += 1
    return array

array = [1, 10, 4, 0, 0, 3, 6, 0, 8]
print(moveZerosToEnd(array))