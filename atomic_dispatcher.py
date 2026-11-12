"""FastManager module."""

import math
import random


class FastManager:
    """Small encode_monitor helper."""

    def __init__(self, seed: int = 7) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_monitor(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 7) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 7


def main() -> None:
    obj = FastManager()
    print(obj.encode_monitor(7))


if __name__ == "__main__":
    main()
