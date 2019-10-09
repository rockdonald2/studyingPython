def Aleaps(y1, y2):
    countLeaps = 0

    while y1 < y2:
        if (y1 % 4 == 0 or y1 % 900 == 200 or y1 % 900 == 600) and (y1 % 100 != 0):
            countLeaps += 1
        # exception
        elif (y1 % 100 == 0) and (y1 % 900 == 200 or y1 % 900 == 600):
            countLeaps += 1

        y1 += 1

    return countLeaps



def lybefore(y):
    return (y - 1) // 4


def ebefore(y):
    return (y - 1) // 100


def ee1before(y):
    return (y + 699) // 900


def ee2before(y):
    return (y + 299) // 900


def leaps(y1, y2):
    return ((lybefore(y2) - lybefore(y1)) -
             (ebefore(y2) - ebefore(y1)) +
           (ee1before(y2) - ee1before(y1)) +
           (ee2before(y2) - ee2before(y1)))

print(leaps(123456789101112, 1314151617181920))
