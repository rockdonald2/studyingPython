def multipleof3and5(value):
    sum = 0
    iter = 3

    while iter < value:
        if iter % 3 == 0 or iter % 5 == 0:
            sum += iter

        iter += 1

    return sum


print(multipleof3and5(1000))
