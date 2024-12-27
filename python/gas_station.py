class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """time complexity: O(n)"""
        if sum(gas) < sum(cost):
            return -1

        result: int = 0
        total: int = 0
        for i in range(0, len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                result = i + 1

        return result


def test_canCompleteCircuit_case_1():
    # arrange
    gas: list[int] = [1, 2, 3, 4, 5]
    cost: list[int] = [3, 4, 5, 1, 2]
    expected: int = 3

    # act
    actual = Solution().canCompleteCircuit(gas, cost)

    # assert
    assert actual == expected


def test_canCompleteCircuit_case_2():
    # arrange
    gas: list[int] = [2, 3, 4]
    cost: list[int] = [3, 4, 3]
    expected: int = -1

    # act
    actual = Solution().canCompleteCircuit(gas, cost)

    # assert
    assert actual == expected
