def leftRotate(array, numberofrotates):
    while numberofrotates != 0:
        temp = array[0]
        for x in range(0, len(array) - 1):
            array[x] = array[x + 1]

        array[len(array) - 1] = temp

        numberofrotates -= 1

    return array


a = list([1, 2, 3, 4, 5])
d = 4
print(leftRotate(a, d))
