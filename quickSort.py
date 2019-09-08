def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    j = low
    while j <= high - 1:
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        j += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):

    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    return arr


list = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92];
print(quickSort(list, 0, len(list) - 1))