def bubbleSort(array):
    it = 0
    swap = False

    while True:
        swap = False
        it = 0
        while it < len(array):
            if array[it] > array[it + 1]:
                array[it], array[it + 1] = array[it + 1], array[it]
                swap = True

            it += 1

        if not swap:
            break

    return array


list = [12, 1, 5, 3, 91, 43, 47, 85, 97, 4, 7]
print(bubbleSort(list))
