"""CoreScheduler module."""

import math
import random


class CoreScheduler:
    """Small parse_buffer helper."""

    def __init__(self, seed: int = 35) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_buffer(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 35) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 35


def main() -> None:
    obj = CoreScheduler()
    print(obj.parse_buffer(35))


if __name__ == "__main__":
    main()
