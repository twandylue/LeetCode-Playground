from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self._count_map: dict[tuple[int, int], int] = defaultdict(int)
        self._points: list[tuple[int, int]] = []

    def add(self, point: list[int]) -> None:
        """time complexity: O(1)"""
        self._count_map[tuple(point)] += 1
        self._points.append(tuple(point))

    def count(self, point: list[int]) -> int:
        """time complexity: O(n)"""
        result: int = 0
        px, py = point
        for x, y in self._points:
            if abs(x - px) != abs(y - py) or px == x or py == y:
                continue
            result += self._count_map[(x, py)] * self._count_map[(px, y)]
        return result


def test_CountSquares_case_1():
    detectSquares: DetectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    assert 1 == detectSquares.count([11, 10])
    assert 0 == detectSquares.count([14, 8])
    detectSquares.add([11, 2])
    assert 2 == detectSquares.count([11, 10])
