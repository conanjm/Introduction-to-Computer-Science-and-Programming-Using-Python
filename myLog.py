def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2
    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    res = 0
    while pow(b, res) <= x:
        res += 1
    return res - 1
