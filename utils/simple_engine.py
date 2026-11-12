"""AsyncFactory module."""

import math
import random


class AsyncFactory:
    """Small build_service helper."""

    def __init__(self, seed: int = 14) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_service(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 14) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 14


def main() -> None:
    obj = AsyncFactory()
    print(obj.build_service(14))


if __name__ == "__main__":
    main()
