def zero_one_sort(array):
    """
    Sort the given array, assuming that its entries are only 0 and 1.

    >>> zero_one_sort([0, 0, 1, 0, 1, 0, 0, 1])
    [0, 0, 0, 0, 0, 1, 1, 1]
    """

    #Count the number of 1s.
    num_ones = 0
    for x in array:
        num_ones += x
    num_zeroes = len(array) - num_ones

    #Output num_zeroes 0s followed by num_ones 1s
    result = []
    # looping zeroes
    # next step
    for i in range(0, num_zeroes):
        result.append(0)
    # looping ones
    for i in range(0, num_ones):
        result.append(1)
    return result

