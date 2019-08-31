def spinal_case(string):
    workingString = list(string)

    i = 0
    length = len(string)
    while i < length:
        if workingString[i] == " ":
            workingString[i] = "-"

        i += 1

    return ''.join(workingString).lower()

string = "Spinal case this sentence"
print(spinal_case(string))
