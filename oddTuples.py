def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    result = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            result += (aTup[i],)

    return result

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))
