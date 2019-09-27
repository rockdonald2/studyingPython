def permute(str, l, r, temp):
    array = list(str)

    if l == r:
        temp.append(str)
    else:
        j = l
        while j <= r:
            array[l], array[j] = array[j], array[l]

            permute(''.join(array), l + 1, r, temp)

            array[l], array[j] = array[j], array[l]

            j += 1


def noRepeats(str):
    if len(str) == 1:
        return 1

    count = 0
    i = 0
    while i < len(str) - 1:
        if str[i] == str[i + 1]:
            count += 1

        i += 1

    if count == len(str) - 1:
        return 0

    temp = []
    permute(str, 0, len(str) - 1, temp)

    numberOfNoRepeats = 0
    k = 0
    while k < len(temp):
        w = 0
        repeat = False
        while w < len(temp[k]) - 1:
            c = temp[k][w]

            if temp[k][w + 1] == c:
                repeat = True

            if repeat:
                break

            w += 1

        if not repeat:
            numberOfNoRepeats += 1

        k += 1

    return numberOfNoRepeats


str = "abfdefa"
print(noRepeats(str))
