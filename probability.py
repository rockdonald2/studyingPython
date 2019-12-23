from itertools import combinations


def func():
    elements = [1, 2, 3, 4, 5, 6, 7]

    combinated = list(combinations(elements, 4))

    counter = 1
    for elem in combinated:
        print(elem, counter)
        counter += 1

    return None


func()
