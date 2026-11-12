"""DynamicMonitor module."""

import math
import random


class DynamicMonitor:
    """Small resolve_factory helper."""

    def __init__(self, seed: int = 53) -> None:
        self._state = seed
        self._items: list[int] = []

    def resolve_factory(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 53) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 53


def main() -> None:
    obj = DynamicMonitor()
    print(obj.resolve_factory(53))


if __name__ == "__main__":
    main()
