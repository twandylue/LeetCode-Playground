class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l: int = 0
        r: int = num // 2 + 1
        while l <= r:
            mid: int = (l + r) // 2
            if mid**2 == num:
                return True
            if mid**2 > num:
                r = mid - 1
            else:
                l = mid + 1

        return False


def test_isPerfectSquare_case_1():
    # arrange
    num: int = 16
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isPerfectSquare(num)

    # assert
    assert expected == actual


def test_isPerfectSquare_case_2():
    # arrange
    num: int = 14
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isPerfectSquare(num)

    # assert
    assert expected == actual
