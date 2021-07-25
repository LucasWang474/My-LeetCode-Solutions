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
