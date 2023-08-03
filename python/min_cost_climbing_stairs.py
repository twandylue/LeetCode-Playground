class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        for i in reversed(range(0, len(cost) - 3, 1)):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])


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
