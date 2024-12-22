class Solution:
    def climbStairs(self, n: int) -> int:
        """time complexity: O(n)"""
        if n <= 2:
            return n
        dp: list[int] = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


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
