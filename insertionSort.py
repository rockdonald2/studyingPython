def insertionSort(array):
    itI = 1
    while itI < len(array):
        itJ = 0
        while itJ <= itI - 1:
            if array[itJ] > array[itI]:
                array.insert(itJ, array[itI])
                array.pop(itI + 1)
                break

            itJ += 1

        itI += 1

    return array


array = [12, 11, 13, 5, 6]
print(insertionSort(array))
