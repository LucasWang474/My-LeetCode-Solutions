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
        min_i = i
        for j in range(i + 1, N):
            if a[j] < a[min_i]:
                min_i = j
        if i != min_i:
            a[i], a[min_i] = a[min_i], a[i]
