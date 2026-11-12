"""DynamicRegistry module."""

import math
import random


class DynamicRegistry:
    """Small run_service helper."""

    def __init__(self, seed: int = 40) -> None:
        self._state = seed
        self._items: list[int] = []

    def run_service(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 40) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 40


def main() -> None:
    obj = DynamicRegistry()
    print(obj.run_service(40))


if __name__ == "__main__":
    main()
