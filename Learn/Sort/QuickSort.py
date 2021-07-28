def select(arr, k):
    """
    >>> arr = [3, 2, 1, -1, -2, -3, 4, 5, 6, 9, 8, 7]
    >>> select(arr, 5)
    3
    """
    lo, hi = 0, len(arr) - 1

    while hi > lo:
        j = partition(arr, lo, hi)
        if k < j:
            hi = j - 1
        elif k > j:
            lo = j + 1
        else:
            break
    return arr[k]


def sort(arr):
    """
    >>> import os
    >>> files = os.listdir('/home/lucas')
    >>> expected = sorted(files)
    >>> sort(files)
    >>> files == expected
    True
    """
    import random
    random.shuffle(arr)
    sort_recur(arr, 0, len(arr) - 1)


def sort_recur(arr, lo, hi):
    if lo >= hi:
        return

    j = partition(arr, lo, hi)
    sort_recur(arr, lo, j - 1)
    sort_recur(arr, j + 1, hi)


def partition(arr, lo, hi):
    i, j, pivot = lo, hi + 1, arr[lo]
    while True:
        i += 1
        while arr[i] < pivot and i < hi:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if j <= i:
            break

        arr[i], arr[j] = arr[j], arr[i]

    arr[lo], arr[j] = arr[j], arr[lo]
    return j
