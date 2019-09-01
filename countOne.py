def count(string):
    sum = 0

    for x in string:
        sum += int(x)

    return sum


string = "1000111"
zeros = len(string) - count(string)
ones = count(string)

txt = "The number of ones in the string are {} and the number of zeros are {}"
print(txt.format(ones, zeros))
