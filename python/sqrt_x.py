class Solution:
    def mySqrt(self, x: int) -> int:
        l: int = 0
        r: int = x // 2 + 1
        result: int = 0
        while l <= r:
            mid: int = (l + r) // 2
            result = mid
            if mid**2 == x:
                return mid
            if mid**2 > x:
                r = mid - 1
            else:
                l = mid + 1

        return result if result**2 < x else result - 1

    def mySqrt2(self, x: int) -> int:
        l: int = 1
        r: int = x + 1
        while l < r:
            mid: int = l + (r - l) // 2
            if self.feasible(mid, x):
                r = mid
            else:
                l = mid + 1
        return l - 1

    def feasible(self, n: int, x: int) -> bool:
        return n * n > x


def test_mySqrt_case_1():
    # arrange
    x: int = 4
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.mySqrt(x)

    # assert
    assert expected == actual


def test_mySqrt_case_2():
    # arrange
    x: int = 8
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.mySqrt(x)

    # assert
    assert expected == actual
