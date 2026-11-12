"""LiteHandler module."""

import math
import random


class LiteHandler:
    """Small compute_worker helper."""

    def __init__(self, seed: int = 79) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_worker(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 79) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 79


def main() -> None:
    obj = LiteHandler()
    print(obj.compute_worker(79))


if __name__ == "__main__":
    main()
