def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False
    if len(aStr) == 1:
        if char == aStr[:]:
            return True
        else:
            return False

    m = len(aStr) / 2
    if char == aStr[m]:
        return True
    elif char > aStr[m]:
        return isIn(char, aStr[m:])
    else:
        return isIn(char, aStr[0:m])
