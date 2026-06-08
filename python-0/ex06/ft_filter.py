def ft_filter(func, iterable):
    '''filter(function or None, iterable) --> filter object
Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    if func is None:
        return (x for x in iterable if x)
    newlist = (x for x in iterable if func(x))
    return newlist


if __name__ == "__main__":
    ages = [5, 12, 17, 18, 24, 32]

    def myFunc(x):
        if x < 18:
            return False
        else:
            return True
    adults = ft_filter(None, ages)
    for x in adults:
        print(x)
