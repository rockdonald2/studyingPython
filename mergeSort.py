import math


def merge(arr, l, m, r):

    temp = []

    w = 0
    while w < (r - l + 1):
        temp.insert(w, 0)
        w += 1

    i = l
    j = m + 1
    k = 0

    while i <= m and j <= r:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= m:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= r:
        temp[k] = arr[j]
        k += 1
        j += 1

    i = l
    while i <= r:
        arr[i] = temp[i - l]
        i += 1

    return arr


def mergeSort(arr, l, r):

    if l < r:
        m = math.floor((l + r) / 2)

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)

    return arr


list = [12, 11, 13, 5, 6]
print(mergeSort(list, 0, len(list) - 1))