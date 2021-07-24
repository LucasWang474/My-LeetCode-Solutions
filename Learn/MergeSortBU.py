def sort(a):
    """
    >>> import os
    >>> files = os.listdir('/home/lucas')
    >>> expected = sorted(files)
    >>> sort(files)
    >>> files == expected
    True
    """
    N = len(a)
    aux = [0] * N

    size = 1
    while size < N:
        for lo in range(0, N, size * 2):
            merge(a, aux, lo, lo + size - 1, min(N - 1, lo + size * 2 - 1))
        size *= 2


def merge(a, aux, lo, mid, hi):
    for i in range(lo, hi + 1):
        aux[i] = a[i]

    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if j > hi or i <= mid and aux[i] <= aux[j]:
            a[k] = aux[i]
            i += 1
        else:
            a[k] = aux[j]
            j += 1
