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
    for i in range(N):
        for j in reversed(range(i)):
            if a[j + 1] < a[j]:
                a[j + 1], a[j] = a[j], a[j + 1]
            else:
                break
