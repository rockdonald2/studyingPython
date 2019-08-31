def title_case(string):
    i = 0
    length = len(string)

    workingString = list(string)

    while i < length:
        ch = ord(string[i])

        if 65 <= ch <= 90:
            if workingString[i - 1] != " " and i != 0:
                workingString[i] = chr(ch + 32)

        elif 97 <= ch <= 122 and i != 0:
            if string[i - 1] == " ":
                workingString[i] = chr(ch - 32)

        i += 1

    return ''.join(workingString)


string = "I'm a little tea pot"
print(title_case(string))