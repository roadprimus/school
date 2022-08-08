"""Objects for creating data for sorting (for test only)."""
from random import randint
from typing import Optional


def g_data(length: int, a: Optional[int] = 0, b: Optional[int] = 100) -> list:
    """Create list of random numbers."""
    return [randint(a, b) for _ in range(length)]


if __name__ == '__main__':
    print(g_data(10))
