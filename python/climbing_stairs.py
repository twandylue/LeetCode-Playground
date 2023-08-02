class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        f: int = 1
        s: int = 1
        result: int = 0
        for _ in range(0, n - 1):
            result = f + s
            s = f
            f = result

        return result


def test_climbStairs_case_1():
    # arrange
    n: int = 2
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.climbStairs(n)

    # assert
    assert expected == actual


def test_climbStairs_case_2():
    # arrange
    n: int = 3
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.climbStairs(n)

    # assert
    assert expected == actual
