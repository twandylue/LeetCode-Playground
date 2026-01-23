class Solution:
    def isConvex(self, points: list[list[int]]) -> bool:
        # Time complexity: O(n)
        if len(points) < 3:
            return False

        def cross(o: tuple[int, int], a: tuple[int, int], b: tuple[int, int]) -> int:
            # (a[0] - o[0]), (a[1] - o[1])
            # (b[0] - o[0]), (b[1] - o[1])
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        sign: int = 0
        n: int = len(points)
        for i in range(n):
            c: int = cross(points[i], points[(i + 1) % n], points[(i + 2) % n])
            if c == 0:
                continue
            if sign == 0:
                sign = 1 if c > 0 else -1
            elif c * sign < 0:
                return False
        return True


def test_isConvex_case_1():
    # assert
    points: list[list[int]] = [[0, 0], [0, 1], [1, 1], [1, 0]]
    expected: bool = True

    # act
    actual: list[list[int]] = Solution().isConvex(points)

    # assert
    assert expected == actual


def test_isConvex_case_2():
    # assert
    points: list[list[int]] = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]
    expected: bool = False

    # act
    actual: list[list[int]] = Solution().isConvex(points)

    # assert
    assert expected == actual
