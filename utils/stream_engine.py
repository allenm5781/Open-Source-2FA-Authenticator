"""DynamicHandler module."""

import math
import random


class DynamicHandler:
    """Small collect_service helper."""

    def __init__(self, seed: int = 35) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_service(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 35) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 35


def main() -> None:
    obj = DynamicHandler()
    print(obj.collect_service(35))


if __name__ == "__main__":
    main()
