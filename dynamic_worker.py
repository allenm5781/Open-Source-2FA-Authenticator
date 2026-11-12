"""HybridProvider module."""

import math
import random


class HybridProvider:
    """Small collect_resolver helper."""

    def __init__(self, seed: int = 47) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_resolver(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 47) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 47


def main() -> None:
    obj = HybridProvider()
    print(obj.collect_resolver(47))


if __name__ == "__main__":
    main()
