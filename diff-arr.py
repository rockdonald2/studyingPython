def diffArray(arr1, arr2):
    finalArr = list()

    lengthArr1 = len(arr1)
    lengthArr2 = len(arr2)

    if lengthArr1 > lengthArr2:
        i = 0
        while i < lengthArr1:
            elem = arr1[i]

            if elem not in arr1:
                finalArr.append(elem)
            i += 1

    elif lengthArr2 > lengthArr1:
        i = 0
        while i < lengthArr2:
            elem = arr2[i]

            if elem not in arr1:
                finalArr.append(elem)
            i += 1

    return finalArr


firstArray = [1, 2, 3, 5]
secondArray = [1, 2, 3, 4, 5]
print(diffArray(firstArray, secondArray))