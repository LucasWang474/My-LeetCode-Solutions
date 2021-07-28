def sort(a):
    """
    >>> import os
    >>> files = os.listdir('/home/lucas')
    >>> expected = sorted(files)
    >>> sort(files)
    >>> files == expected
    True
    """
    aux = [0] * len(a)
    sort_recur(a, aux, 0, len(a) - 1)


def sort_recur(a, aux, lo, hi):
    if lo >= hi:
        return

    mid = (lo + hi) // 2
    sort_recur(a, aux, lo, mid)
    sort_recur(a, aux, mid + 1, hi)
    merge(a, aux, lo, mid, hi)


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
