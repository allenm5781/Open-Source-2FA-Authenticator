"""LocalCache module."""

import math
import random


class LocalCache:
    """Small handle_client helper."""

    def __init__(self, seed: int = 92) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_client(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 92) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 92


def main() -> None:
    obj = LocalCache()
    print(obj.handle_client(92))


if __name__ == "__main__":
    main()
