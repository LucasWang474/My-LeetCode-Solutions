def sort(arr):
    """
    >>> import os
    >>> files = os.listdir('/home/lucas')
    >>> expected = sorted(files)
    >>> sort(files)
    >>> files == expected
    True
    """
    sort_recur(arr, 0, len(arr) - 1)


def sort_recur(arr, lo, hi):
    if lo >= hi:
        return

    lt, gt = lo, hi
    pivot = arr[lo]

    i = lo + 1
    while i <= gt:
        if arr[i] < pivot:
            swap(arr, i, lt)
            i += 1
            lt += 1
        elif arr[i] > pivot:
            swap(arr, i, gt)
            gt -= 1
        else:
            i += 1

    sort_recur(arr, lo, lt - 1)
    sort_recur(arr, gt + 1, hi)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
