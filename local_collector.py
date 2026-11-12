"""BatchRegistry module."""

import math
import random


class BatchRegistry:
    """Small collect_adapter helper."""

    def __init__(self, seed: int = 76) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_adapter(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 76) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 76


def main() -> None:
    obj = BatchRegistry()
    print(obj.collect_adapter(76))


if __name__ == "__main__":
    main()
