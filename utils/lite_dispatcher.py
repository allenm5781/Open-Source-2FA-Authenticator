"""LocalParser module."""

import math
import random


class LocalParser:
    """Small encode_processor helper."""

    def __init__(self, seed: int = 76) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_processor(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 76) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 76


def main() -> None:
    obj = LocalParser()
    print(obj.encode_processor(76))


if __name__ == "__main__":
    main()
