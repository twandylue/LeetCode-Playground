class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """time complexity: O(n)"""
        n: int = len(cost)
        dp: list[int] = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]


def test_minCostClimbingStairs_case_1():
    # arrange
    cost: list[int] = [10, 15, 20]
    expected: int = 15

    # act
    solution = Solution()
    actual: int = solution.minCostClimbingStairs(cost)

    # assert
    assert expected == actual


def test_minCostClimbingStairs_case_2():
    # arrange
    cost: list[int] = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    expected: int = 6

    # act
    solution = Solution()
    actual: int = solution.minCostClimbingStairs(cost)

    # assert
    assert expected == actual
