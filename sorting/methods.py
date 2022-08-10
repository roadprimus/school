"""Module for sorting methods."""


def bubble(arr: list[int]) -> list:
    """Run Bubble sorting method."""
    length = len(arr)
    for i in range(1, length):
        for j in range(length - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

    return arr


def selection(arr: list[int]) -> list:
    """Run Selection sorting method."""
    length = len(arr)
    for i in range(length):
        m = arr[i]
        for j in range(i + 1, length):
            if arr[j] < m:
                m = arr[j]
        arr[i] = m

    return arr


def insertion(arr: list[int]) -> list:
    """Run Insertion sorting method."""
    length = len(arr)
    for i in range(length):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

    return arr


def _max(arr: list[int], length: int, a: int, b: int) -> int:
    """Find max between values at positions a and b."""
    return a if a < length and arr[a] > arr[b] else b


def swap(arr: list[int], root: int, length: int) -> None:
    """Reorder subtree from array to heap."""
    left = 2 * root + 1
    right = 2 * root + 2

    largest = _max(arr, length, right, _max(arr, length, left, root))
    if largest != root:
        arr[largest], arr[root] = arr[root], arr[largest]
        swap(arr, largest, length)


def heapsort(arr: list[int]) -> list:
    """Run Heapsort sorting method."""
    length = len(arr)
    for i in range(length, -1, -1):
        swap(arr, i, length)

    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swap(arr, 0, i)

    return arr
