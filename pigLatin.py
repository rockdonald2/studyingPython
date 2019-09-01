def pigLatin(string):
    workingString = list(string)

    i = 0
    length = len(string)
    while i < length:
        if workingString[i] != "a" and workingString[i] != "e" and workingString[i] != "o" and workingString[i] != "u" \
                and workingString[i] != "i":
            workingString.insert(length, workingString[i])
            workingString.remove(workingString[i])
            i -= 1
        elif i == 0 and string[i] == "a" or string[i] == "e" or string[i] == "o" or string[i] == "u" or string[i] == "i":
            workingString.insert(length, "w")
            workingString.insert(length + 1, "a")
            workingString.insert(length + 2, "y")
            return ''.join(workingString)
        else:
            break

        i += 1

    workingString.insert(length, "a")
    workingString.insert(length + 1, "y")

    return ''.join(workingString)


string = "eight"
print(pigLatin(string))
