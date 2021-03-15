import time
import sys

def min_sort(array):
    """
    Sort the given array using the MinSort algorithm.

    >>> min_sort([17, 4, 32, 19, 8, 65, 19, 44])
    [4, 8, 17, 19, 19, 32, 44, 65]

    """

    n = len(array)
    for i in range(0, n - 1):

        # Find the minimum in array[i..n -1]
        minimum = array[i]
        minimum_index = i
        for j in range(i + 1, n):
            if array[j] < minimum:
                minimum = array[j]
                minimum_index = j

        # Swap the minimum to the front
        array[i], array[minimum_index] = array[minimum_index], array[i]

    return array


    
if __name__ == "__main__":
    """ A small performance measurement """
    for n in range(500, 10001, 500):
        array = [k for k in range(n-1, 0, -1)]
        start_time = time.monotonic()
        min_sort(array)
        end_time = time.monotonic()
        duration_msecs = (end_time - start_time) * 1000
        print("%d\t%d" %(n, duration_msecs))
        sys.stdout.flush()

        # Call via Terminal with following command: python3 min_sort.py
    
