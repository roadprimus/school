"""Module for sorting methods."""


def bubble(arr: list[int]) -> list:
    """Bubble sorting method."""
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
