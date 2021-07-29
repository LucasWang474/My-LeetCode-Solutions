def sort(arr):
    for i in range(len(arr)):
        swim(arr, i)

    for i in reversed(range(1, len(arr))):
        swap(arr, 0, i)
        sink(arr, 0, i - 1)


def sink(arr, k, last):
    while (k * 2 + 1) <= last:
        j = k * 2 + 1
        if j < last and arr[j] < arr[j + 1]:
            j += 1

        if arr[k] >= arr[j]:
            break
        swap(arr, k, j)
        k = j


def swim(arr, k):
    def parent(k):
        return (k - 1) // 2

    while k > 0 and arr[k] > arr[parent(k)]:
        swap(arr, k, parent(k))
        k = parent(k)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
