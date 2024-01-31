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
