def spinal_case(string):
    workingString = list(string)

    i = 0
    length = len(string)
    while i < length:
        if workingString[i] == " " or workingString[i] == "_":
            workingString[i] = "-"
        if 65 <= ord(workingString[i]) <= 90 and i != 0 and workingString[i - 1] != "-":
            workingString.insert(i, "-")
            i += 1
        i += 1

    return ''.join(workingString).lower()


string = "The_Andy_Griffith_Show"
print(spinal_case(string))
