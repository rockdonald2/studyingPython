def selection_sort(array):
    length = len(array)
    startIndex = 0
    while startIndex < length - 1:
        smallestIndex = startIndex

        currentIndex = startIndex + 1
        while currentIndex < length:
            if array[currentIndex] < array[smallestIndex]:
                smallestIndex = currentIndex
            currentIndex += 1

        array[startIndex], array[smallestIndex] = array[smallestIndex], array[startIndex]
        startIndex += 1

    return array


array = [30, 50, 20, 10, 40]
print(selection_sort(array))
