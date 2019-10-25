def isValid(ID):
    lettersInOrder = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

    letter = list(ID).pop()
    numbers = list(ID)
    numbers.pop()
    numbers = int(''.join(numbers))
    if letter == lettersInOrder[numbers % 23]:
        return True
    else:
        return False


print(isValid('43685091H'))
