def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    if s1 == '':
        return s2
    if s2 == '':
        return s1
    result = ''
    if len(s1) == len(s2):
        for i in range(len(s1)):
            result += s1[i]+s2[i]
    elif len(s1) > len(s2):
        for i in range(len(s2)):
            result += s1[i]+s2[i]
        result += s1[i+1:]
    else:
        for i in range(len(s1)):
            result += s1[i]+s2[i]
        result += s2[i+1:]
    return result
