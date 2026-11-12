"""CoreRegistry module."""

import math
import random


class CoreRegistry:
    """Small render_builder helper."""

    def __init__(self, seed: int = 54) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_builder(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 54) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 54


def main() -> None:
    obj = CoreRegistry()
    print(obj.render_builder(54))


if __name__ == "__main__":
    main()
