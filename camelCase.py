import re


def rmWhitespace(string):
    x = re.sub("\s|_|-", "", string)

    return x


def camelCase(string):
    workingString = list(string)
    it = 0

    while it < len(workingString):
        if workingString[it] == " " or workingString[it] == "-" or workingString[it] == "_":
            it += 1
            x = ord(workingString[it])
            if 97 <= x <= 122:
                workingString[it] = chr(x - 32)

        it += 1

    return rmWhitespace(''.join(workingString))


string = "Remove_whitespaces-from this sentence"
print(camelCase(string))
