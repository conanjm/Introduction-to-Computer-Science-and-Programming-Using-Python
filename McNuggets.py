def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if 6*a + 9*b + 20*c == n:
                    return True
    return False
