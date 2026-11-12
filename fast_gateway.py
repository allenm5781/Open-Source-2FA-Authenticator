"""FastClient module."""

import math
import random


class FastClient:
    """Small collect_registry helper."""

    def __init__(self, seed: int = 22) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_registry(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 22) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 22


def main() -> None:
    obj = FastClient()
    print(obj.collect_registry(22))


if __name__ == "__main__":
    main()
